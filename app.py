# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__, static_folder="static", template_folder="templates")

QUOTES = [
    {"text": "天行健，君子以自强不息。", "source": "《周易》"},
    {"text": "穷且益坚，老而弥励。", "source": "《礼记》"},
    {"text": "路漫漫其修远兮，吾将上下而求索。", "source": "屈原"},
    {"text": "宝剑锋从磨砺出，梅花香自苦寒来。", "source": "佚名"},
    {"text": "天将降大任于斯人也，必先苦其心志。", "source": "《孟子》"},
    {"text": "积土成山，风雨兴焉；积水成渊，蛟龙生焉。", "source": "《荀子》"},
    {"text": "不积跬步，无以至千里；不积小流，无以成江海。", "source": "《荀子》"},
    {"text": "业精于勤，荒于嬉；行成于思，毁于随。", "source": "韩愈"},
    {"text": "读万卷书，行万里路。", "source": "刘彭年"},
    {"text": "会当凌绝顶，一览众山小。", "source": "杜甫"},
    {"text": "志不求易者成，事不避难者进。", "source": "《后汉书》"},
    {"text": "海阔凭鱼跃，天高任鸟飞。", "source": "佚名"},
]

KEYWORD_QUOTES = {
    "焦虑": {"text": "天将降大任于斯人也，必先苦其心志。", "source": "《孟子》"},
    "压力": {"text": "不积跬步，无以至千里；不积小流，无以成江海。", "source": "《荀子》"},
    "失败": {"text": "宝剑锋从磨砺出，梅花香自苦寒来。", "source": "佚名"},
    "累": {"text": "业精于勤，荒于嬉；行成于思，毁于随。", "source": "韩愈"},
    "迷茫": {"text": "路漫漫其修远兮，吾将上下而求索。", "source": "屈原"},
    "内耗": {"text": "天行健，君子以自强不息。", "source": "《周易》"},
    "摆烂": {"text": "志不求易者成，事不避难者进。", "source": "《后汉书》"},
}

EXTRA_ADVICE = [
    "今天给自己一个小目标，明天你会看到不一样的坚持。",
    "先接纳自己的疲惫，再把它变成前进的动力。",
    "一步一步走，所有压力都会变成你的底气。",
    "凡事从当下开始，日积月累就会形成力量。",
]


def choose_quote(user_input: str) -> dict:
    if not user_input:
        return random.choice(QUOTES)

    text = user_input.strip().lower()
    for key, quote in KEYWORD_QUOTES.items():
        if key in text:
            return quote
    return random.choice(QUOTES)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/encourage", methods=["POST"])
def encourage():
    data = request.get_json(silent=True) or {}
    user_text = data.get("message", "")
    quote = choose_quote(user_text)
    advice = random.choice(EXTRA_ADVICE)

    return jsonify({
        "request": user_text,
        "quote": quote["text"],
        "source": quote["source"],
        "advice": advice,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
