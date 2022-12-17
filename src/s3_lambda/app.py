import os
import boto3
import requests

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import FlexSendMessage

# libからインポート
from lib.rekognition.util import (
    emotion_flexmessage,
    emo_json,
    emotions_conv,
    get_dynamo_table
)

channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
table_name = os.getenv('DYNAMODB_TABLE_NAME', None)

line_bot_api = LineBotApi(channel_access_token)

# Headerの生成
HEADER = {
    'Content-type':
    'application/json',
    'Authorization':
    'Bearer ' + channel_access_token
}


def lambda_handler(event, context):

    records = event['Records']

    # Webhookの接続確認用
    if len(records) == 0:
        return {
            'statusCode': 200,
            'body': ''
        }
    # S3からバケット名を取得
    images_bucket = records[0]['s3']['bucket']['name']

    # S3からオブジェクト名を取得
    image_key = str(records[0]['s3']['object']['key'])

    # ファイル名にはuser_idが付与される想定
    file_extend = image_key.split('.')
    user_id = file_extend[0].split('_')[1]
    image_id = file_extend[0].split('_')[0]

    # Rekognition を実行
    try:

        rekognition = boto3.client('rekognition')
        reko_response = rekognition.detect_faces(
            Image={
                'S3Object': {
                    'Bucket': images_bucket,
                    'Name': image_key,
                },
            },
            Attributes=['ALL']
        )
        print(reko_response)
        len_face_details = len(reko_response['FaceDetails'])

        if len_face_details == 0:

            messages = TextSendMessage(text='顔がありません！')
            line_bot_api.push_message(
                to=user_id,
                messages=messages
            )

        else:
            face_details = reko_response['FaceDetails'][0]
            emotions = face_details['Emotions']

            # 返信用FlexMessage を作成する
            flex_message = emotion_flexmessage(emotions)
            flex_message_obj = FlexSendMessage(
                alt_text='alt_text',
                # contentsパラメタに, dict型の値を渡す
                contents=flex_message
            )
            # 送信するFlexMessage を作成
            line_bot_api.push_message(user_id, flex_message_obj)

            profile = requests.get(
                'https://api.line.me/v2/bot/profile/{0}'.format(user_id), headers=HEADER)
            profile_json = profile.json()
            user_name = profile_json['displayName']

            # DynamoDBにRekognition の結果を保存
            emo = {}
            emo['Emotions'] = emotions_conv(emotions)
            emotion_items = emo_json(emo['Emotions'])

            print("DyanmoDB 登録")
            item = {}
            item = emotion_items
            item['user_name'] = user_name
            item['object_id'] = image_key
            item['image_id'] = image_id

            # レコード登録
            dynamo_table = get_dynamo_table(table_name)
            dynamo_table.put_item(Item=item)

    except Exception as e:
        print(e)
        return
