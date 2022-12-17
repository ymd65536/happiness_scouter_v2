
import os
import json

from decimal import Decimal
from boto3.session import Session


# FlexMessage Image
flex_ref_image = os.getenv('IMAGE_URL', None)

# 戦闘力の倍率
level = 5500
target_score = 5000 * 100.0


def emotion_flexmessage(emotions):

    message = """
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "margin": "lg",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "感情",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "割合",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "スコア",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "幸せ",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "穏やか",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "驚き",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "恐れ",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "困惑",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "嫌悪",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "怒り",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "悲しみ",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "戦闘力",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "align": "start",
                "contents": []
              },
              {
                "type": "text",
                "text": "====",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "測定完了！！",
            "align": "center",
            "contents": []
          }
        ]
      }
    ]
  }
}
"""

    original_message = """
{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "label": "Line",
      "uri": "https://google.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "margin": "lg",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "感情",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "割合",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "スコア",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "幸せ",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "穏やか",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "驚き",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "恐れ",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "困惑",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "嫌悪",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "怒り",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "悲しみ",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "戦闘力",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "align": "start",
                "contents": []
              },
              {
                "type": "text",
                "text": "=======>",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "align": "start",
                "contents": []
              },
              {
                "type": "text",
                "text": "0.0",
                "size": "md",
                "color": "#000000FF",
                "flex": 1,
                "contents": []
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "新郎新婦と同じくらい幸せです！！",
            "align": "center",
            "contents": []
          }
        ]
      }
    ]
  }
}
"""

    combat_power = 0.0
    for emotion in emotions:
        emotion_type = emotion['Type']
        emotion_value = round(emotion['Confidence'], 3)
        emotion_confidence = str(emotion_value)
        emotion_score = str(emotion_value*level)
        if emotion_type == 'HAPPY':
            emotion_happy = emotion_confidence
            happy_score = emotion_score
            combat_power = emotion_value * level
        elif emotion_type == 'SAD':
            emotion_sad = emotion_confidence
            sad_score = emotion_score
        elif emotion_type == 'ANGRY':
            emotion_angry = emotion_confidence
            angry_score = emotion_score
        elif emotion_type == 'SURPRISED':
            emotion_surprised = emotion_confidence
            surprised_score = emotion_score
        elif emotion_type == 'DISGUSTED':
            emotion_disgusted = emotion_confidence
            disgusted_score = emotion_score
        elif emotion_type == 'CALM':
            emotion_calm = emotion_confidence
            calm_score = emotion_score
        elif emotion_type == 'CONFUSED':
            emotion_confused = emotion_confidence
            confused_score = emotion_score
        elif emotion_type == 'FEAR':
            emotion_fear = emotion_confidence
            fear_score = emotion_score

    # 戦闘力がtarget_score 以上であれば、返信メッセージを変更する

    if combat_power >= target_score:
        print("特別なメッセージで対応")
        flex_message_json_dict = json.loads(original_message)
        flex_message_json_dict['hero']['url'] = flex_ref_image
        flex_message_json_dict['hero']['action']['uri'] = flex_ref_image
    else:
        print("通常のメッセージで対応")
        flex_message_json_dict = json.loads(message)

    combat_power = str(combat_power)
    flex_message_json_dict['body']['contents'][0]['contents'][1]['contents'][1]['text'] = emotion_happy
    flex_message_json_dict['body']['contents'][0]['contents'][2]['contents'][1]['text'] = emotion_calm
    flex_message_json_dict['body']['contents'][0]['contents'][3]['contents'][1]['text'] = emotion_surprised
    flex_message_json_dict['body']['contents'][0]['contents'][4]['contents'][1]['text'] = emotion_fear
    flex_message_json_dict['body']['contents'][0]['contents'][5]['contents'][1]['text'] = emotion_confused
    flex_message_json_dict['body']['contents'][0]['contents'][6]['contents'][1]['text'] = emotion_disgusted
    flex_message_json_dict['body']['contents'][0]['contents'][7]['contents'][1]['text'] = emotion_angry
    flex_message_json_dict['body']['contents'][0]['contents'][8]['contents'][1]['text'] = emotion_sad

    flex_message_json_dict['body']['contents'][0]['contents'][1]['contents'][2]['text'] = happy_score
    flex_message_json_dict['body']['contents'][0]['contents'][2]['contents'][2]['text'] = calm_score
    flex_message_json_dict['body']['contents'][0]['contents'][3]['contents'][2]['text'] = surprised_score
    flex_message_json_dict['body']['contents'][0]['contents'][4]['contents'][2]['text'] = fear_score
    flex_message_json_dict['body']['contents'][0]['contents'][5]['contents'][2]['text'] = confused_score
    flex_message_json_dict['body']['contents'][0]['contents'][6]['contents'][2]['text'] = disgusted_score
    flex_message_json_dict['body']['contents'][0]['contents'][7]['contents'][2]['text'] = angry_score
    flex_message_json_dict['body']['contents'][0]['contents'][8]['contents'][2]['text'] = sad_score
    flex_message_json_dict['body']['contents'][0]['contents'][9]['contents'][2]['text'] = combat_power

    return flex_message_json_dict


def get_dynamo_table(table_name):
    session = Session(
        region_name='ap-northeast-1'
    )

    dynamodb = session.resource('dynamodb')
    dynamo_table = dynamodb.Table(table_name)
    return dynamo_table

# DyanmoDBはfloat 型に対応していない
# decimal に変換する必要があるが、データはそのまま残しておきたい


def emotions_conv(emotions):
    len_emotions = len(emotions)
    for cnt_i in range(len_emotions):
        emotions[cnt_i]['Confidence'] = Decimal(
            str(round(emotions[cnt_i]['Confidence'], 3)))
    return emotions


def emo_json(emotions):
    emotion_items = {}

    for emotion in emotions:
        emotion_value = round(emotion['Confidence'], 3)
        emotion_score = str(emotion_value*level)
        emotion_items[emotion['Type']] = emotion_score

    return emotion_items
