# make_srt.py — 把 Groq 的 verbose_json 組成 .srt
# 用法：uv run python make_srt.py 輸出.srt 第1段.json 第2段.json ...
# 只有一段就只傳一個 json；多段會自動接上時間碼偏移（見步驟四）
import json, os, subprocess, sys

def fmt(t):
    """秒數 → SRT 的 00:00:00,000 格式"""
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def real_seconds(path):
    """用 ffprobe 量音訊檔的實際長度（秒）。量不到就回 None"""
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", path],
            capture_output=True, text=True, check=True).stdout.strip()
        return float(out)
    except Exception:
        return None

out_path, json_files = sys.argv[1], sys.argv[2:]
if not json_files:
    sys.exit("SRT_FAIL 沒有指定任何 json 檔")

offset, idx, blocks = 0.0, 1, []
for jf in json_files:
    with open(jf, encoding="utf-8") as f:
        data = json.load(f)
    for seg in data.get("segments", []):
        text = (seg.get("text") or "").strip()
        if not text:
            continue
        blocks.append(
            f"{idx}\n{fmt(seg['start'] + offset)} --> {fmt(seg['end'] + offset)}\n{text}\n")
        idx += 1
    # 🚨 陷阱 ④：偏移量用「這一段的實際長度」累加，不要用名目的 600 秒
    audio = os.path.splitext(jf)[0] + ".flac"
    dur = real_seconds(audio) if os.path.exists(audio) else None
    if dur is None:                       # ffprobe 不在？改用 API 回傳的長度
        dur = float(data.get("duration") or 0.0)
    offset += dur

with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(blocks))
print(f"SRT_OK segments={idx - 1} files={len(json_files)} out={out_path}")
