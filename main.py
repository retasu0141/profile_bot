from flask import Flask, request, abort,render_template
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, JoinEvent, TextMessage, TextSendMessage, FlexSendMessage,  PostbackEvent, TemplateSendMessage,ButtonsTemplate,URIAction,QuickReplyButton,QuickReply
)

import time
import math
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

import psycopg2
import random

from datetime import datetime as dt

import urllib.request, urllib.error

from apiclient.discovery import build
import urllib.parse
import re, requests
app = Flask(__name__)


def syoukai():
    data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://pbs.twimg.com/profile_images/1130431449927000064/7p5cs0qh_400x400.jpg",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "自己紹介",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "名前",
                    "wrap": True,
                    "color": "#aaaaaa",
                    "size": "sm",
                    "flex": 1
                  },
                  {
                    "type": "text",
                    "text": "レタス",
                    "wrap": True,
                    "color": "#666666",
                    "size": "sm",
                    "flex": 2
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
                    "text": "年齢",
                    "wrap": True,
                    "color": "#aaaaaa",
                    "size": "sm",
                    "flex": 1
                  },
                  {
                    "type": "text",
                    "text": "17",
                    "wrap": True,
                    "color": "#666666",
                    "size": "sm",
                    "flex": 2
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
                    "text": "性別",
                    "wrap": True,
                    "color": "#aaaaaa",
                    "size": "sm",
                    "flex": 1
                  },
                  {
                    "type": "text",
                    "text": "男",
                    "wrap": True,
                    "color": "#666666",
                    "size": "sm",
                    "flex": 2
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
                    "text": "住み",
                    "wrap": True,
                    "color": "#aaaaaa",
                    "size": "sm",
                    "flex": 1
                  },
                  {
                    "type": "text",
                    "text": "東京",
                    "wrap": True,
                    "color": "#666666",
                    "size": "sm",
                    "flex": 2
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://illustrain.com/img/work/2016/illustrain02-hobby01.png",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "僕の趣味",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "下のボタンを押して続ける",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "postback",
                      "label": "僕の趣味",
                      "data": "趣味",
                      "displayText": "僕の趣味を説明するよ！"
                    }
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
}
    return data

def syumi():
    data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://www.atoone.co.jp/wp-content/uploads/2019/05/Men-doing-videoediting.jpeg"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "動画編集",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "2020年7月",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "辺りから",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "詳しく見る",
              "data": "動画",
              "displayText": "動画編集について詳しく！"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://www.pakutaso.com/shared/img/thumb/cameraIMGL9940_TP_V.jpg"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "写真撮影",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "flex": 1,
            "contents": [
              {
                "type": "text",
                "text": "2016年6月",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "辺りから",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "詳しく見る",
              "data": "写真",
              "displayText": "写真撮影について詳しく！"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://i1.wp.com/threem-design.com/wp-content/uploads/youtube-bgm-eye.jpg?fit=1580%2C960&ssl=1"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "音楽制作",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "flex": 1,
            "contents": [
              {
                "type": "text",
                "text": "2016年4月",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "辺りから",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "詳しく見る",
              "data": "音楽",
              "displayText": "音楽制作について詳しく！"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "url": "https://pictkan.com/uploads/converted/15/06/06/2927926911-work-731198_1920-3Y4-1920x1280-MM-100.jpg"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "プログラミング",
            "wrap": True,
            "weight": "bold",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "baseline",
            "flex": 1,
            "contents": [
              {
                "type": "text",
                "text": "2017年6月",
                "wrap": True,
                "weight": "bold",
                "size": "xl",
                "flex": 0
              },
              {
                "type": "text",
                "text": "辺りから",
                "wrap": True,
                "weight": "bold",
                "size": "sm",
                "flex": 0
              }
            ]
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "flex": 2,
            "style": "primary",
            "action": {
              "type": "postback",
              "label": "詳しく見る",
              "data": "プログラミング",
              "displayText": "プログラミングについて詳しく！"
            }
          }
        ]
      }
    }
  ]
}
    return data

def douga():
    data = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.atoone.co.jp/wp-content/uploads/2019/05/Men-doing-videoediting.jpeg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "動画編集",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "きっかけ",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "時間や人間関係に縛られるのが辛くなり、自分で稼げて力もつく動画編集に憧れる",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "スタート",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "その時持っていたWindowsのデスクトップパソコンで自分の動画を編集し始める",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "それから",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "色々な人と接しながら案件を獲得。しかし相手の対応が酷く(振込日を過ぎても連絡なし)案件を受けなくなった。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "今の状況",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "色々ありデスクトップ売りM1のMacBookを購入。動画編集を地道に続けている。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "これから",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "これからは再度案件を獲得するため自分の情報発信を続け信頼を獲得したい。すでに話の進んできている案件もある。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "趣味一覧に戻る",
          "data": "趣味",
          "displayText": "趣味一覧に戻って！"
        }
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
}
    return data

def syasin():
    data = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://www.pakutaso.com/shared/img/thumb/cameraIMGL9940_TP_V.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "写真撮影",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "きっかけ",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "親の古くなったミラーレス一眼レフを貰う。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "スタート",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "6月に行ったキャンプで写真を撮ることにハマる。その後自分用の一眼レフを買う。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "それから",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "親がよく行くキャンプで写真を撮り続け風景写真を沢山撮影する。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "今の状況",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "某ウイルスのせいもありキャンプになかなか行けず最近は一眼レフを触れてない。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "これから",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "外に出れる状況になったらまた沢山風景写真を撮りたい。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "インスタ",
          "uri": "https://www.instagram.com/retasu_0141/"
        },
        "style": "secondary"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "趣味一覧に戻る",
          "data": "趣味",
          "displayText": "趣味一覧に戻って！"
        }
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
}
    return data

def music():
    data = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i1.wp.com/threem-design.com/wp-content/uploads/youtube-bgm-eye.jpg?fit=1580%2C960&ssl=1",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "音楽制作",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "きっかけ",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "小学校の頃PCの授業で音楽を作るというものがあり、そこで楽曲制作にハマる。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "スタート",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "中一でスマホを買ってもらったと同時にガレージバンドというアプリで作曲を開始。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "それから",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "曲をYouTubeに載せながらボチボチと作曲を継続。元から得意でなくとも続けることである程度の所まで行けることを実感。少し勇気が出た。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "今の状況",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "ボーカロイドを使いながらボカロ曲を制作。音楽の知識も勉強中。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "これから",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "ギターやピアノなどの楽器を使えるようになりたい。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "趣味一覧に戻る",
          "data": "趣味",
          "displayText": "趣味一覧に戻って！"
        }
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
}
    return data

def program():
    data = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://pictkan.com/uploads/converted/15/06/06/2927926911-work-731198_1920-3Y4-1920x1280-MM-100.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "音楽制作",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "きっかけ",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "プログラマーになりたいなどではなく、その時流行っていたLINEの非公式のBotを作りたい為に中古のPCを購入。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "スタート",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "親に内緒で買った中古PCを使い見よう見まねでBotを作成。プログラム自体にハマる。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "それから",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "非公式だと限界を感じ公式のLINEボットを作成。その後ディスコードやSlackのbotも作成。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "今の状況",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "新しいBotの案をねりながら色んなBotを作成。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
                "text": "これから",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "夢は誰かが必要としているBotを作ること。Bot作成依頼などもいつか受けたい。ボトルメールBotという自作のBotの使用者を増やしたい。",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 3
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
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "趣味一覧に戻る",
          "data": "趣味",
          "displayText": "趣味一覧に戻って！"
        }
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
}
    return data

def portfolio():
    data = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://img.icons8.com/ios/452/bot.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "fit",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "weight": "bold",
        "size": "md",
        "text": "Botの作例&動画のポートフォリオ",
        "align": "center"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://img.icons8.com/ios/452/bot.png"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "トレンドBOT",
          "uri": "https://lin.ee/Q0ZmYbQ"
        }
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "ボトルメールBOT",
          "uri": "https://lin.ee/qAOdMpA"
        }
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "ポートフォリオ",
          "uri": "https://youtu.be/s7fimIAjTu4"
        }
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
}
    return data

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/")
def hello_world():
    return "hello world!"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
@handler.add(JoinEvent)
def join(event):
    reply_token = event.reply_token
    data = syoukai()
    flex = {"type": "flex","altText": "自己紹介","contents":data}
    container_obj = FlexSendMessage.new_from_json_dict(flex)
    line_bot_api.reply_message(reply_token,messages=container_obj)


@handler.add(PostbackEvent)
def on_postback(event):
    reply_token = event.reply_token
    user_id = event.source.user_id
    postback_msg = event.postback.data

    if "趣味" in postback_msg:
        data = syumi()
        flex = {"type": "flex","altText": "趣味一覧","contents":data}
        container_obj = FlexSendMessage.new_from_json_dict(flex)
        line_bot_api.reply_message(reply_token,messages=container_obj)

    if "動画" in postback_msg:
        data = douga()
        flex = {"type": "flex","altText": "動画編集について","contents":data}
        container_obj = FlexSendMessage.new_from_json_dict(flex)
        line_bot_api.reply_message(reply_token,messages=container_obj)

    if "写真" in postback_msg:
        data = syasin()
        flex = {"type": "flex","altText": "写真撮影について","contents":data}
        container_obj = FlexSendMessage.new_from_json_dict(flex)
        line_bot_api.reply_message(reply_token,messages=container_obj)

    if "音楽" in postback_msg:
        data = music()
        flex = {"type": "flex","altText": "音楽制作について","contents":data}
        container_obj = FlexSendMessage.new_from_json_dict(flex)
        line_bot_api.reply_message(reply_token,messages=container_obj)

    if "プログラミング" in postback_msg:
        data = program()
        flex = {"type": "flex","altText": "プログラミングについて","contents":data}
        container_obj = FlexSendMessage.new_from_json_dict(flex)
        line_bot_api.reply_message(reply_token,messages=container_obj)

    if "写真" in postback_msg:
        data = syasin()
        flex = {"type": "flex","altText": "写真撮影について","contents":data}
        container_obj = FlexSendMessage.new_from_json_dict(flex)
        line_bot_api.reply_message(reply_token,messages=container_obj)



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global set_
    global stoptime
    global stoppoint
    msg_from = event.reply_token
    msg_text = event.message.text
    msg_id = event.message.id
    user_id = event.source.user_id

    if msg_text == '自己紹介':
        data = syoukai()
        flex = {"type": "flex","altText": "スタート","contents":data}
        container_obj = FlexSendMessage.new_from_json_dict(flex)
        line_bot_api.reply_message(msg_from,messages=container_obj)
        return

    if msg_text == 'Bot作例':
        data = portfolio()
        flex = {"type": "flex","altText": "スタート","contents":data}
        container_obj = FlexSendMessage.new_from_json_dict(flex)
        line_bot_api.reply_message(msg_from,messages=container_obj)
        return




if __name__ == "__main__":
#    app.run()
    port =  int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
