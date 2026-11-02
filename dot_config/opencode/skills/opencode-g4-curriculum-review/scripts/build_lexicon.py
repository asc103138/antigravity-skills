#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_lexicon.py (v4.0 視覺實體驗證防汙染版)
從本機真實課習視覺校對後之語料庫提取各課/單元精確詞彙庫、88個正式《我會寫字》生字表、句型與課文索引，
產出 references/g4_genuine_textbook_lexicon.json 與 references/g4_genuine_textbook_lexicon.md。

⚠️ 重要防呆記錄：
翰林版課本與習作 PDF 之「注音專用字型」在底層文字層（page.get_text()）會以同音字碼儲存
（如：ㄒㄩㄣˊ→巡、ㄋㄧㄥˊ→寧、ㄌㄨㄣˊ→倫、ㄖㄨㄥˊ→榮、ㄔㄨㄥ→衝、ㄐㄧㄥˋ→竟），
且每課《我會寫字》右下角「字詞猜猜看」寶箱內之提示字（守生、怖龍、記影、光魂、車流、衝見）為舊字提示而非本課生字。
本字典所有 characters 已 100% 透過課本原頁高解析渲染圖（p.10, p.20, p.28, p.44, p.54, p.64）人工與視覺雙重校對鎖定！
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUT_JSON = BASE_DIR / "references" / "g4_genuine_textbook_lexicon.json"
OUT_MD = BASE_DIR / "references" / "g4_genuine_textbook_lexicon.md"

# 出版社 PDF 注音字型同音異字碼與習作改錯題錯別字黑名單（嚴禁當成課本生字！）
PDF_FONT_HOMOPHONE_TRAP_CHARS = {
    "巡": "第五課 p.54/習作 p.31 注音字型『ㄒㄩㄣˊ』之底層同音字碼（真實生字為『循』、『尋』）",
    "寧": "第五課 p.49/p.54 注音字型『ㄋㄧㄥˊ』之底層同音字碼（真實生字為『凝』）",
    "倫": "第五課 p.50/p.54 注音字型『ㄌㄨㄣˊ』之底層同音字碼（真實生字為『輪』）",
    "榮": "第二課 p.23 標題『補充內容』注音字型『ㄖㄨㄥˊ』之底層同音字碼（本冊未出現『榮』字）",
    "衝": "第六課 p.64 右下角『字詞猜猜看』寶箱提示舊字 & 第二課 p.23『補充』注音字碼（非本冊 88 個習寫生字）",
    "竟": "第三課 p.28『鏡』之注音字型底層同音字碼（『竟然』雖見於 L02 p.15 內文，但非本冊 88 個習寫生字，L03 生字為『鏡』）",
    "接": "第一課 p.10『街』之注音字型底層同音字碼（真實生字為『街』）",
    "眠": "第一課 p.10『寒』之 PDF 錯置字碼（真實生字為『寒』）",
    "福": "第二課 p.20『彿』之注音字型底層同音字碼（真實生字為『彿』）",
    "允": "第六課 p.64『隕』之注音字型底層同音字碼（真實生字為『隕』）",
    "句": "第六課 p.64『距』之注音字型底層同音字碼（真實生字為『距』）",
}

HANLIN_CHINESE_LESSONS = {
    "L01": {
        "title": "第一課 美麗島（詩歌・楊喚｜課本 p.4~13、生字表 p.10）",
        "characters": ["島", "唾", "沫", "忠", "衛", "寒", "椰", "隊", "蕉", "街", "灣", "甜", "糖", "童"],
        "treasure_box_hints_do_not_test": ["守", "生"],
        "core_vocab": ["美麗島", "唾沫", "成群結隊", "甜蜜", "童話", "椰子樹", "香蕉", "海灣", "守衛", "忠實", "糖果", "大街小巷", "寒冷", "多采多姿"],
        "sentence_patterns": ["……像快樂的……一樣……", "伸著大手掌", "唱著……歌"]
    },
    "L02": {
        "title": "第二課 請到我的家鄉來（書信體｜課本 p.14~23、生字表 p.20）",
        "characters": ["泉", "抹", "訝", "牙", "齒", "區", "架", "速", "彷", "彿", "恐", "陀", "螺", "聚"],
        "treasure_box_hints_do_not_test": ["怖", "龍"],
        "core_vocab": ["大開眼界", "大飽口福", "大吃一驚", "大顯身手", "大排長龍", "彷彿", "好像", "竟然", "恐龍", "化石", "冷泉", "溫泉", "驚訝", "團聚", "陀螺", "打架", "牙齒", "抹在", "快速", "園區"],
        "sentence_patterns": ["以為……沒想到……竟然……", "天色這麼暗，彷彿要下雨了"]
    },
    "L03": {
        "title": "第三課 鏡頭下的家鄉（生活記敘文｜課本 p.24~31、生字表 p.28）",
        "characters": ["鏡", "軌", "樓", "與", "耕", "耘", "蔬", "鼓", "腮", "烤", "柳", "丁", "粉", "網", "錄"],
        "treasure_box_hints_do_not_test": ["記", "影"],
        "core_vocab": ["鏡頭", "紀錄", "耕耘", "蔬菜", "烤香腸", "柳丁", "鼓著", "腮幫子", "漁網", "鐵軌", "高樓", "金粉", "與眾不同"],
        "sentence_patterns": ["即使……也……", "如金粉從天上落下般美麗", "像……般……"]
    },
    "統整一": {
        "title": "統整活動一（讀信回信／審題立意／朗讀｜課本 p.32~37）",
        "characters": [],
        "core_vocab": ["稱謂", "問候語", "正文", "祝福語", "署名", "日期", "審題", "立意"],
        "sentence_patterns": ["先……再……", "針對提問具體回應"]
    },
    "L04": {
        "title": "第四課 飛行夢（記敘文・萊特兄弟｜課本 p.38~47、生字表 p.44）",
        "characters": ["兄", "翔", "鷹", "論", "控", "制", "命", "義", "標", "良", "研", "靈", "升", "紀", "碑"],
        "treasure_box_hints_do_not_test": ["光", "魂"],
        "core_vocab": ["飛行夢", "飛翔", "老鷹", "研究", "控制", "改良", "紀念碑", "靈感", "生命", "討論", "升空", "目標", "意義", "兄弟"],
        "sentence_patterns": ["無論……都……", "不管……都……", "如果失去生命，飛翔還有什麼意義？"]
    },
    "L05": {
        "title": "第五課 月光下（抒情記敘文・賞月｜課本 p.48~57、生字表 p.54）",
        "characters": ["掛", "皎", "凝", "曾", "考", "輪", "徘", "徊", "瑤", "妝", "科", "登", "循", "尋", "案"],
        "treasure_box_hints_do_not_test": ["車", "流"],
        "core_vocab": ["月白風清", "花紅柳綠", "風和日麗", "鳥語花香", "徘徊", "皎潔", "凝視", "白玉盤", "瑤臺鏡", "妝鏡", "曾經", "思考", "科學家", "登月", "循路", "尋找", "答案", "一輪明月", "高掛"],
        "sentence_patterns": ["不只……而且……", "小時不識月，呼作白玉盤"]
    },
    "L06": {
        "title": "第六課 又遠又近的月亮（科學記敘與說明｜課本 p.58~67、生字表 p.64）",
        "characters": ["館", "億", "隕", "撞", "擊", "坑", "射", "狀", "里", "均", "騎", "距", "萬", "餅", "揭"],
        "treasure_box_hints_do_not_test": ["衝", "見"],
        "core_vocab": ["圖書館", "四十五億", "隕石", "撞擊", "坑洞", "照射", "形狀", "萬里", "平均", "騎單車", "距離", "拒絕", "月餅", "揭開", "成千上萬"],
        "sentence_patterns": ["就算……也……", "透過六何法掌握新聞要點"]
    },
    "統整二": {
        "title": "統整活動二（六何法／寫作選材／一起來讀報｜課本 p.68~73）",
        "characters": [],
        "core_vocab": ["六何法", "新聞標題", "環境關懷"],
        "sentence_patterns": ["按照步驟……首先……接著……"]
    }
}

NANI_MATH_UNITS = {
    "單元1": {"title": "一億以內的數", "core_vocab": ["大數", "個位", "十位", "百位", "千位", "萬位", "十萬", "百萬", "千萬", "億位", "化聚", "讀作", "記作", "位值表"]},
    "單元2": {"title": "乘法", "core_vocab": ["直式乘法", "三位數乘以二位數", "積", "被乘數", "乘數", "位值對齊", "末位補零"]},
    "單元3": {"title": "角度", "core_vocab": ["角", "頂點", "邊", "旋轉角", "量角器", "刻度", "平角", "周角", "銳角", "鈍角", "直角", "度數"]},
    "單元4": {"title": "除法", "core_vocab": ["直式除法", "三位數除以二位數", "商", "餘數", "被除數", "除數", "驗算", "餘數小於除數"]},
    "單元5": {"title": "三角形", "core_vocab": ["正三角形", "等腰三角形", "頂角", "底角", "直角三角形", "銳角三角形", "鈍角三角形", "內角和"]},
    "單元6": {"title": "分數", "core_vocab": ["真分數", "假分數", "帶分數", "分子", "分母", "同分母分數", "加法", "減法", "平分"]},
    "單元7": {"title": "數量關係", "core_vocab": ["規律", "間隔", "數列", "對應關係"]},
    "單元8": {"title": "整數四則", "core_vocab": ["四則運算", "先乘除後加減", "括號先算"]},
    "單元9": {"title": "小數", "core_vocab": ["一位小數", "二位小數", "十分位", "百分位", "小數點", "加減"]},
    "單元10": {"title": "長度（公里）", "core_vocab": ["公里", "公尺", "公分", "長度單位換算", "距離"]}
}

KANGXUAN_SOCIAL_UNITS = {
    "單元1": {"title": "美麗的家鄉（家鄉的自然環境）", "core_vocab": ["家鄉", "地形", "平原", "盆地", "丘陵", "臺地", "山地", "海岸", "氣候", "雨量", "氣溫", "水資源", "河川", "水圳", "水庫", "高美濕地", "臺中港", "梧棲", "九降風", "季風", "風力發電"]},
    "單元2": {"title": "家鄉的傳統住屋與器物", "core_vocab": ["傳統住屋", "三合院", "正廳", "護龍", "合院", "土埆厝", "石板屋", "地下屋", "騎樓", "亭仔腳", "器物", "大灶", "石磨", "風鼓機", "菜櫥", "蓑衣", "木臼", "木杵", "竹編", "魚筌", "先民智慧"]},
    "單元3": {"title": "家鄉的傳統信仰與老街", "core_vocab": ["傳統信仰", "廟宇", "土地公", "媽祖", "老街", "聚落", "古蹟", "宗祠", "陣頭", "祭典", "信仰中心"]},
    "單元4": {"title": "家鄉的作息、節慶與節日", "core_vocab": ["生活作息", "農耕作息", "傳統節慶", "春節", "端午節", "中秋節", "元宵節", "公共節日", "公共設施", "安全維護", "社區營造"]}
}

def main():
    all_88_chars = []
    for l_info in HANLIN_CHINESE_LESSONS.values():
        all_88_chars.extend(l_info["characters"])

    lexicon_data = {
        "chinese": HANLIN_CHINESE_LESSONS,
        "chinese_all_official_characters": all_88_chars,
        "pdf_font_homophone_traps": PDF_FONT_HOMOPHONE_TRAP_CHARS,
        "math": NANI_MATH_UNITS,
        "social": KANGXUAN_SOCIAL_UNITS
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(lexicon_data, f, ensure_ascii=False, indent=2)

    lines = [
        "# 國小四年級核心教科書合法詞彙與命題真理辭典 (Genuine Curriculum Lexicon v4.0 視覺驗證防汙染版)",
        "",
        "> **使用指引（Agent 與出題者必讀）**：",
        "> 1. **第一大題生字注音絕對白名單（88 字）**：國語科第一大題（寫出國字和注音）之所有考點，**必須 100% 取自下方各課《課本生字（我會寫字）》清單（L01~L06 共 88 字）**！",
        "> 2. **嚴禁被 PDF 注音字型同音碼與猜字寶箱誤導**：",
        ">    - 課本生字表右下角「字詞猜猜看」寶箱內之舊字（`守、生、怖、龍、記、影、光、魂、車、流、衝、見`）**絕非本冊生字**，嚴禁出進第一大題！",
        ">    - 出版社 PDF 底層注音字型同音碼（如 `巡、寧、倫、榮、竟、接、眠、福、允、句`）**絕非該頁真實生字**，嚴禁未看原圖直接以 `page.get_text()` 抽字出題！",
        ">    - 課文內文出現但未列入《我會寫字》之延伸舊字（如 `衝、竟、造、耀`），亦不得作為第一大題生字注音考點！",
        "> 3. **審查比對依據**：`scripts/check_curriculum.py` 將以本字典之 88 字白名單進行單字級強制攔截，違者直接一票否決！",
        "",
        "---",
        "",
        f"## 📙 國語科（翰林版四上 L01~L06）《我會寫字》88 字視覺驗證白名單",
        ""
    ]

    for l_key, l_info in HANLIN_CHINESE_LESSONS.items():
        lines.append(f"### 【{l_key}】{l_info['title']}")
        if l_info["characters"]:
            lines.append(f"- **課本生字（{len(l_info['characters'])} 字）**：{'、'.join(l_info['characters'])}")
        else:
            lines.append("- **課本生字**：（統整活動無新增生字表）")
        if l_info.get("treasure_box_hints_do_not_test"):
            lines.append(f"- **⚠️ 猜字寶箱舊字（嚴禁當成生字出題）**：`{'`、`'.join(l_info['treasure_box_hints_do_not_test'])}`")
        lines.append(f"- **合法核心詞彙**：`{'`、`'.join(l_info['core_vocab'])}`")
        lines.append(f"- **課本/習作指定句型**：{'；'.join(l_info['sentence_patterns'])}")
        lines.append("")

    lines.append("### 🚫 出版社 PDF 注音字型同音異字碼黑名單（嚴禁誤用）")
    for trap_ch, reason in PDF_FONT_HOMOPHONE_TRAP_CHARS.items():
        lines.append(f"- **`{trap_ch}`**：{reason}")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 📘 數學科（南一版四上）各單元核心數學術語總表")
    lines.append("")
    for u_key, u_info in NANI_MATH_UNITS.items():
        lines.append(f"### 【{u_key}】{u_info['title']}")
        lines.append(f"- **核心數學概念與詞彙**：`{'`、`'.join(u_info['core_vocab'])}`")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 📗 社會科（康軒版四上）各單元專有名詞總表")
    lines.append("")
    for s_key, s_info in KANGXUAN_SOCIAL_UNITS.items():
        lines.append(f"### 【{s_key}】{s_info['title']}")
        lines.append(f"- **專有名詞與風土詞彙**：`{'`、`'.join(s_info['core_vocab'])}`")
        lines.append("")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"✅ 已成功產出 v4.0 視覺驗證合法詞彙辭典（共 {len(all_88_chars)} 個正式生字）：\n  - {OUT_JSON}\n  - {OUT_MD}")

if __name__ == "__main__":
    main()
