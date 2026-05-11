from __future__ import annotations

import random
from dataclasses import dataclass

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


@dataclass(frozen=True)
class Quote:
    text: str
    author: str
    source: str
    meaning: str
    tags: tuple[str, ...]


QUOTES: tuple[Quote, ...] = (
    Quote(
        text="天行健，君子以自强不息。",
        author="《周易》",
        source="乾卦",
        meaning="真正的力量不是从不疲惫，而是愿意一次次把自己扶起来。",
        tags=("奋斗", "坚持", "迷茫", "摆烂"),
    ),
    Quote(
        text="士不可以不弘毅，任重而道远。",
        author="曾子",
        source="《论语》",
        meaning="把人生看长一点，今天的压力就不必变成对自己的否定。",
        tags=("压力", "责任", "学习", "工作"),
    ),
    Quote(
        text="知不足而奋进，望远山而前行。",
        author="化用古训",
        source="劝学精神",
        meaning="承认不足不是羞耻，停在原地才会让焦虑反复生长。",
        tags=("内耗", "自卑", "成长", "迷茫"),
    ),
    Quote(
        text="路漫漫其修远兮，吾将上下而求索。",
        author="屈原",
        source="《离骚》",
        meaning="人生的答案通常不是想出来的，而是在行动中一点点走出来的。",
        tags=("迷茫", "选择", "坚持", "焦虑"),
    ),
    Quote(
        text="博学之，审问之，慎思之，明辨之，笃行之。",
        author="《礼记》",
        source="中庸",
        meaning="别让脑内反复推演替代行动，把问题拆小，然后笃定去做。",
        tags=("内耗", "学习", "行动", "拖延"),
    ),
    Quote(
        text="千里之行，始于足下。",
        author="老子",
        source="《道德经》",
        meaning="再大的改变，也从当下一个可完成的小动作开始。",
        tags=("拖延", "摆烂", "行动", "开始"),
    ),
    Quote(
        text="不积跬步，无以至千里；不积小流，无以成江海。",
        author="荀子",
        source="《劝学》",
        meaning="稳定的微小进步，最终会超过一阵热血后的停摆。",
        tags=("学习", "积累", "坚持", "奋斗"),
    ),
    Quote(
        text="锲而不舍，金石可镂。",
        author="荀子",
        source="《劝学》",
        meaning="不要用一天的状态审判一生的可能，持续本身就是天赋。",
        tags=("坚持", "考试", "工作", "奋斗"),
    ),
    Quote(
        text="生于忧患，而死于安乐。",
        author="孟子",
        source="《孟子》",
        meaning="痛苦不必浪费，它也可以成为你升级认知和能力的燃料。",
        tags=("压力", "挫折", "成长", "奋斗"),
    ),
    Quote(
        text="穷且益坚，不坠青云之志。",
        author="王勃",
        source="《滕王阁序》",
        meaning="环境越不容易，越要替未来的自己守住一点志气。",
        tags=("低谷", "挫折", "坚持", "自卑"),
    ),
    Quote(
        text="长风破浪会有时，直挂云帆济沧海。",
        author="李白",
        source="《行路难》",
        meaning="眼前不顺不是终局，先把帆挂起来，风才有机会帮你。",
        tags=("低谷", "希望", "工作", "考试"),
    ),
    Quote(
        text="会当凌绝顶，一览众山小。",
        author="杜甫",
        source="《望岳》",
        meaning="把目标抬高一点，很多眼前的比较和噪音就会变小。",
        tags=("目标", "奋斗", "内卷", "迷茫"),
    ),
    Quote(
        text="纸上得来终觉浅，绝知此事要躬行。",
        author="陆游",
        source="《冬夜读书示子聿》",
        meaning="想太多会耗尽心力，亲手做一点会带回掌控感。",
        tags=("行动", "拖延", "学习", "内耗"),
    ),
    Quote(
        text="宝剑锋从磨砺出，梅花香自苦寒来。",
        author="古代格言",
        source="《警世贤文》",
        meaning="吃苦不是目的，但经得住磨练的人会拥有更硬的底气。",
        tags=("奋斗", "坚持", "低谷", "考试"),
    ),
)


KEYWORD_TAGS: dict[str, str] = {
    "卷": "内卷",
    "内耗": "内耗",
    "焦虑": "焦虑",
    "迷茫": "迷茫",
    "摆烂": "摆烂",
    "躺平": "摆烂",
    "拖延": "拖延",
    "学习": "学习",
    "考试": "考试",
    "工作": "工作",
    "上班": "工作",
    "压力": "压力",
    "自卑": "自卑",
    "失败": "挫折",
    "低谷": "低谷",
}


ACTIONS: tuple[str, ...] = (
    "先做 10 分钟最小任务，不追求完美，只追求启动。",
    "写下一个今天能完成的小目标，并在完成后立刻打勾。",
    "把脑中最吵的一句话写出来，再写一句更公允的话回应它。",
    "关掉让你比较和焦虑的信息源 30 分钟，换回自己的节奏。",
    "给未来 7 天定一个固定动作，每天只推进一点点。",
    "找一件能带来掌控感的小事完成，比如整理桌面或复盘一页笔记。",
)


def pick_quote(message: str, mood: str) -> Quote:
    raw_text = f"{message} {mood}".lower()
    matched_tags = {tag for keyword, tag in KEYWORD_TAGS.items() if keyword in raw_text}

    if mood:
        matched_tags.add(mood)

    candidates = [
        quote
        for quote in QUOTES
        if matched_tags and any(tag in quote.tags for tag in matched_tags)
    ]

    return random.choice(candidates or list(QUOTES))


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/quotes")
def list_quotes():
    return jsonify(
        [
            {
                "text": quote.text,
                "author": quote.author,
                "source": quote.source,
                "meaning": quote.meaning,
                "tags": quote.tags,
            }
            for quote in QUOTES
        ]
    )


@app.post("/api/encourage")
def encourage():
    payload = request.get_json(silent=True) or {}
    message = str(payload.get("message", "")).strip()
    mood = str(payload.get("mood", "")).strip()

    if len(message) > 400:
        return jsonify({"error": "输入太长了，请控制在 400 字以内。"}), 400

    quote = pick_quote(message, mood)
    return jsonify(
        {
            "quote": quote.text,
            "author": quote.author,
            "source": quote.source,
            "meaning": quote.meaning,
            "action": random.choice(ACTIONS),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
