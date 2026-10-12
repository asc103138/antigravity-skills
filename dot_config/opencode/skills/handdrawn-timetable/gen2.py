# -*- coding: utf-8 -*-
"""那隻水母風：手繪奶油色課表（一年庚班 115上）"""
import re, pymupdf

PDF = r"C:\Users\ccps\Desktop\一年庚班課表_115上.pdf"
OUT = r"C:\Users\ccps\AppData\Local\Temp\opencode\schedule\schedule2.html"

SUBJECTS = {"體育","國語","數學","生活","生活美勞","國際新視野","本土語","健康","閱讀","梧風啟航"}
TEACHERS = {"鄭穎佳","王怡婷","洪鈺棋","楊于萱","林淑慧"}

doc = pymupdf.open(PDF)
lines = [l.strip() for l in doc[0].get_text().splitlines() if l.strip()]

periods = []
cur = None
for line in lines:
    if re.fullmatch(r"\d", line) or line == "午休":
        cur = {"no": int(line) if line.isdigit() else "B", "time": None, "cells": []}
        periods.append(cur)
        continue
    if cur is None:
        continue
    if line.startswith("節次") or line == "時間" or "星期" in line or "臺中市" in line or line.startswith("國語6"):
        continue
    if cur["time"] is None and ":" in line and "-" in line:
        cur["time"] = line
        continue
    cur["cells"].append(line)

matrix = []          # 課表：每節 = (time, [5 x (subject, teacher)])，以 xlsx 格位為準
import openpyxl
_wb = openpyxl.load_workbook(r"C:\Users\ccps\Desktop\一年庚班課表_115上_v3.xlsx", data_only=True)
_xcells = {}
for r in _wb.active.iter_rows(min_row=3, values_only=True):
    key = str(r[0]).strip() if r[0] else ""
    if key == "":
        continue
    if key == "午休":
        _xcells["B"] = [None] * 5
        continue
    _cells = []
    for i in range(5):
        v = r[2 + i]
        _cells.append(str(v).strip() if v is not None and str(v).strip() else None)
    _xcells[key] = _cells
for p in periods:
    if p["no"] == "B":
        matrix.append((p["time"], None))
        continue
    pdfseq = []
    for c in p["cells"]:
        toks = c.split()
        tch = next((t for t in toks[1:] if t in TEACHERS), None)
        pdfseq.append((toks[0], tch))
    slots = _xcells.get(str(p["no"]), [None] * 5)
    k = 0
    row = []
    for s in slots:
        if s is None:
            row.append((None, None))
        else:
            row.append(pdfseq[k]); k += 1
    matrix.append((p["time"], row))

INK = "#6C5F52"
BG = "#F6EEDA"
TINT = "#EBDCC4"
WHITE = "#FDFCF8"
SOFT = "#BED3E1"

def sparkle(x=16, s=1.0):
    return f'<svg viewBox="0 0 32 32" width="{32*s}" height="{32*s}" style="opacity:.9"><path d="M16 0 L19.5 12.5 L32 16 L19.5 19.5 L16 32 L12.5 19.5 L0 16 L12.5 12.5 Z" fill="#fff" opacity=".9" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/></svg>'

def star(s=42):
    return f'<svg viewBox="0 0 40 40" width="{s}" height="{s}"><path d="M20 2 L25.2 13.4 L37.5 14.6 L28.4 22.6 L31.1 34.8 L20 28.4 L8.9 34.8 L11.6 22.6 L2.5 14.6 L14.8 13.4 Z" fill="#fff" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/><circle cx="16.5" cy="18" r="1.7" fill="{INK}"/><circle cx="23.5" cy="18" r="1.7" fill="{INK}"/><path d="M17 23 Q20 26 23 23" stroke="{INK}" stroke-width="2" fill="none" stroke-linecap="round"/></svg>'

def jelly(s=110):
    return f'''<svg viewBox="0 0 76 100" width="{s}" height="{int(s*1.32)}">
<path d="M13 42 C13 16 63 16 63 42 L63 45 C58 41 54 48 49 44 C44 40 40 47 35 43 C30 39 26 46 21 42 C16 38 13 46 13 49 Z" fill="{SOFT}" stroke="{INK}" stroke-width="3.2" stroke-linejoin="round"/>
<circle cx="28" cy="30" r="2.8" fill="{INK}"/><circle cx="48" cy="30" r="2.8" fill="{INK}"/>
<path d="M33 38 Q38 43 43 38" stroke="{INK}" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<path d="M22 50 Q18 62 21 70 M38 52 Q39 64 36 72 M54 50 Q58 61 55 70" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>
</svg>'''

def heart(s=30):
    return f'<svg viewBox="0 0 36 34" width="{s}" height="{int(s*0.95)}"><path d="M18 30 C8 23 3 15 8 8 C12 3 18 8 18 12 C18 8 24 3 28 8 C33 15 28 23 18 30 Z" fill="#fff" opacity=".92" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/></svg>'

def smiley(s=34):
    return f'<svg viewBox="0 0 36 36" width="{s}" height="{s}"><circle cx="18" cy="18" r="15" fill="#F8E3AC" opacity=".95" stroke="{INK}" stroke-width="2.6"/><circle cx="12.5" cy="15.5" r="2" fill="{INK}"/><circle cx="23.5" cy="15.5" r="2" fill="{INK}"/><path d="M12 21 Q18 27 24 21" stroke="{INK}" stroke-width="2.4" fill="none" stroke-linecap="round"/></svg>'

def bubble_txt(txt):
    return f'<div class="bubble"><span>{txt}</span></div>'

DAY_EN = ["MON", "TUE", "WED", "THU", "FRI"]
DAY_CN = ["星期一", "星期二", "星期三", "星期四", "星期五"]

def cell_text(subj, tch):
    t = f'<div class="sname">{subj}</div>'
    if tch:
        t += f'<div class="steacher">{tch} 老師</div>'
    return t

# ---------- 組表格 ----------
head_btn = star(44)
TR = []
# 標題列
day_cells = "".join(
    f'<td class="dhead"><div class="den">{e}</div><div class="dcn">{c}</div></td>'
    for e, c in zip(DAY_EN, DAY_CN))
TR.append(f'<tr><td class="num">{head_btn}</td>{day_cells}</tr>')

for idx, (time, row) in enumerate(matrix):
    if row is None:
        t1, t2 = time.split("-")
        TR.append(f'''<tr class="bk"><td class="num"></td>
<td colspan="5"><div class="bkband"><div class="bkheart">{heart(26)}</div><div class="bken">- BREAK TIME -</div>
<div class="bkcn">午休 · {t1} – {t2}</div><span class="bkface">(◕‿◕)</span></div></td></tr>''')
        continue
    noon = idx < 4
    cls = "" if noon else " pm"
    pno = idx + 1 if idx < 4 else idx
    t1, t2 = time.split("-")
    num_html = f'<div class="pno">{pno}</div><div class="ptime">{t1}<br>{t2}</div>'
    cells = []
    for j, (subj, tch) in enumerate(row):
        if subj is None:
            extra = smiley(34) if (idx == 5 and j == 2) else ""
            cells.append(f'<td class="cell{cls}">{extra}</td>')
        else:
            hx = '<span class="cellheart">' + heart(26) + '</span>' if (idx == 1 and j == 1) else ""
            cells.append(f'<td class="cell{cls}">{hx}{cell_text(subj, tch)}</td>')
    TR.append(f'<tr class="row"><td class="num{cls}">{num_html}</td>{"".join(cells)}</tr>')

HTML = f'''<!DOCTYPE html><html lang="zh-Hant"><head><meta charset="utf-8">
<style>
@font-face {{ font-family:"Kuai"; src:url("fonts/ZCOOLKuaiLe-Regular.ttf"); }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:1150px; background:{BG}; font-family:"Kuai","Microsoft JhengHei",sans-serif; }}
.page {{ width:1150px; padding:38px 42px 26px; position:relative; }}
.svgdefs {{ position:absolute; width:0; height:0; }}
/* 標題 */
.schline {{ text-align:center; font-size:19px; letter-spacing:2px; color:#8A7B68; }}
.bubble {{ width:fit-content; margin:14px auto 4px; padding:12px 46px 16px; border:5px solid {INK};
 border-radius:70px; background:#FBEFDB; }}
.bubble span {{ font-size:40px; letter-spacing:10px; color:{INK}; padding-left:10px; }}
.bigtitle {{ text-align:center; margin-top:14px; font-size:52px; color:{INK}; letter-spacing:8px; }}
.bigtitle b {{ background:{INK}; color:{BG}; padding:0 18px; border-radius:14px; }}
/* 塗鴉定位 */
.doodle-1 {{ position:absolute; left:112px; top:156px; transform:rotate(-10deg); font-size:26px;
 font-family:"Kuai",sans-serif; color:#8A7B68; }}
.doodle-2 {{ position:absolute; right:90px; top:220px; }}
.jelly {{ position:absolute; right:92px; top:64px; transform:rotate(10deg); }}
.doodle-3 {{ position:absolute; right:70px; bottom:66px; }}
/* 表格 */
table {{ border-collapse:separate; border-spacing:10px; margin-top:8px; width:1090px;
 margin-left:auto; margin-right:auto; filter:url(#wobble); }}
td {{ vertical-align:middle; text-align:center; }}
.num {{ width:100px; }}
.pno {{ font-size:46px; color:{INK}; line-height:1; }}
.ptime {{ font-size:14px; color:#8A7B68; margin-top:6px; line-height:1.5; }}
.dhead {{ background:{WHITE}; border:3.5px solid {INK}; border-radius:10px; height:92px; }}
.den {{ font-size:30px; letter-spacing:5px; color:{INK}; }}
.dcn {{ font-size:14px; margin-top:3px; color:#8A7B68; letter-spacing:3px; }}
.cell {{ position:relative; background:{WHITE}; border:3.5px solid {INK}; border-radius:10px; height:128px; }}
.cellheart {{ position:absolute; left:4px; top:-12px; }}
.cell.fix1 {{ position:relative; }} 
.cell.pm {{ background:{TINT}; }}
.sname {{ font-size:31px; color:{INK}; letter-spacing:2px; }}
.steacher {{ font-size:17px; color:#8A7B68; margin-top:4px; }}
tr.bk td {{ border:none; }}
.bkband {{ position:relative; background:#FBEFDB; border:4px solid {INK}; border-radius:10px; height:104px;
 display:flex; flex-direction:column; justify-content:center; align-items:center; gap:2px; }}
.bken {{ font-size:30px; letter-spacing:8px; color:{INK}; }}
.bkcn {{ font-size:15px; color:#8A7B68; letter-spacing:2px; }}
.bkface {{ position:absolute; right:36px; font-size:18px; color:{INK}; opacity:.85; }}
.bkheart {{ position:absolute; left:22px; top:36px; }}
.tr-hold {{ position:relative; }}
.sig {{ text-align:center; margin-top:14px; font-size:21px; color:#9A8B75; letter-spacing:2px; }}
</style></head><body>
<svg class="svgdefs" xmlns="http://www.w3.org/2000/svg">
<filter id="wobble" x="-5%" y="-5%" width="110%" height="110%">
<feTurbulence type="fractalNoise" baseFrequency="0.019 0.021" numOctaves="2" seed="8" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="4.5"/>
</filter>
</svg>
<div class="page">
<div class="doodle-1">(◕‿◕)</div>
<div class="doodle-2">{sparkle(40, 0.9)}</div>
<div class="jelly">{jelly(112)}</div>
<div class="doodle-3">{star(40)}</div>
<div class="schline">臺中市梧棲區中正國民小學 · 115 學年度第 1 學期</div>
{bubble_txt("TIMETABLE")}
<div class="bigtitle">一年<b>庚</b>班的課表</div>
<table class="tr-hold">
{''.join(TR)}
</table>
<div class="sig">@ 中正國小 · 一年庚班</div>
</div>
</body></html>'''

HTML = HTML.replace("sparklesvgov", "")
with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("OK", OUT)
for i, (t, row) in enumerate(matrix):
    print(i, t, row)
