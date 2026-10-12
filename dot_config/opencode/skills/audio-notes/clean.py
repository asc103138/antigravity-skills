# clean.py — 把逐字稿清洗成可讀講義（Groq Chat Completions）
# 用法：uv run python clean.py 逐字稿.txt 講義.md
import json, os, sys, time, urllib.error, urllib.request

API   = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.3-70b-versatile"   # 會改名！先跑 /v1/models 確認
LIMIT = 1200                        # 每段送幾個字。免費方案 TPM 很小，不要調大

KEY = os.environ.get("GROQ_API_KEY")
if not KEY:
    sys.exit("CLEAN_FAIL 環境變數 GROQ_API_KEY 沒設，回步驟二")

SYSTEM = (
    "你是台灣國中小老師的文字編輯助理。把語音辨識出來的逐字稿，"
    "整理成可以直接發給學生看的講義段落。規則："
    "① 一律輸出繁體中文，用台灣的慣用詞；"
    "② 刪掉贅詞、口頭禪、結巴、重複、以及講者自己更正掉的前半句；"
    "③ 補上標點符號，依語意分段；"
    "④ 不要新增原文沒有的內容，不要加自己的解釋；"
    "⑤ 聽不出來的地方原樣保留，並在後面加上 [?]；"
    "⑥ 不要寫開場白或結語，直接輸出整理後的內文。"
)

def split_text(raw, limit):
    """依行切段，盡量不切在句子中間"""
    parts, buf = [], ""
    def flush():
        nonlocal buf
        if buf.strip():
            parts.append(buf)
        buf = ""
    for line in raw.splitlines(keepends=True):
        while len(line) > limit:          # 整篇沒換行的長文，只好硬切
            flush()
            parts.append(line[:limit])
            line = line[limit:]
        if len(buf) + len(line) > limit:
            flush()
        buf += line
    flush()
    return parts

def call(text):
    body = json.dumps({
        "model": MODEL,
        "temperature": 0.2,
        "messages": [{"role": "system", "content": SYSTEM},
                     {"role": "user",   "content": text}],
    }).encode("utf-8")
    req = urllib.request.Request(API, data=body, headers={
        "Authorization": "Bearer " + KEY,
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)["choices"][0]["message"]["content"].strip()

raw   = open(sys.argv[1], encoding="utf-8").read()
parts = split_text(raw, LIMIT)
out   = []

for n, p in enumerate(parts, 1):
    print(f"清洗第 {n}/{len(parts)} 段…")
    for attempt in range(3):
        try:
            out.append(call(p))
            break
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "ignore")[:300]
            if e.code == 429 and attempt < 2:      # 額度滿了，等一下再試
                print("   額度滿了，等 35 秒再試")
                time.sleep(35)
                continue
            sys.exit(f"CLEAN_FAIL http={e.code} {detail}")
    time.sleep(2)                                   # 段與段之間刻意留間隔

open(sys.argv[2], "w", encoding="utf-8").write("\n\n".join(out))
print(f"CLEAN_OK pieces={len(parts)} out={sys.argv[2]}")
