<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>《快樂的家庭活動》作文句型學習單 — 從鷹架到精彩作文</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reset.css" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/night.css" />
  <!-- WordCloud2.js for interactive word cloud -->
  <script src="https://cdn.jsdelivr.net/npm/wordcloud@1.2.2/src/wordcloud2.min.js"></script>
  <style>
    /* === 全域變數 === */
    :root {
      --accent:  #e8643a;  /* 活力橘紅 */
      --accent2: #4fc3f7;  /* 科技青藍 */
      --success: #81c784;  /* 清新亮綠 */
      --warn:    #ffb74d;  /* 溫暖金黃 */
      --card-bg: rgba(255, 255, 255, 0.06);
      --card-border: rgba(255, 255, 255, 0.12);
    }

    .reveal {
      font-family: 'Segoe UI', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif;
      color: #f1f5f9;
      background: #0d1117;
    }
    .reveal h1, .reveal h2, .reveal h3 {
      font-family: 'Segoe UI', 'Noto Sans TC', sans-serif;
      font-weight: 700;
      letter-spacing: -0.01em;
    }
    .reveal h1 { font-size: 2.1em; line-height: 1.2; }
    .reveal h2 { font-size: 1.45em; color: var(--accent2); margin-bottom: 0.5em; }
    .reveal h3 { font-size: 1.1em; color: var(--warn); }
    .reveal .progress { color: var(--accent); }
    .reveal .fragment { opacity: 0.15; transition: all 0.3s ease; }
    .reveal .fragment.visible { opacity: 1; }

    /* === 封面 === */
    .title-slide { text-align: center; }
    .title-slide .tag {
      display: inline-block;
      background: linear-gradient(135deg, var(--accent), #ff7043);
      color: #fff;
      padding: 5px 16px;
      border-radius: 20px;
      font-size: 0.45em;
      letter-spacing: 0.08em;
      margin-bottom: 0.8em;
      font-weight: 600;
      box-shadow: 0 4px 12px rgba(232,100,58,0.4);
    }
    .title-slide .subtitle { font-size: 0.65em; color: #cbd5e1; margin-top: 0.5em; line-height: 1.5; }
    .title-slide .author { margin-top: 2em; font-size: 0.45em; color: #94a3b8; }

    /* === 卡片與網格 === */
    .card-grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-top: 0.8em;
    }
    .card-grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      margin-top: 0.8em;
    }
    .adv-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-top: 4px solid var(--accent2);
      border-radius: 12px;
      padding: 18px 14px;
      text-align: center;
      transition: transform 0.2s ease;
    }
    .adv-card:hover { transform: translateY(-4px); }
    .adv-card .adv-icon { margin-bottom: 10px; }
    .adv-card .adv-icon img {
      width: 60px; height: 60px; object-fit: contain;
      display: block; margin: 0 auto;
      filter: drop-shadow(0 0 12px rgba(79,195,247,0.7));
    }
    .adv-card .adv-title { font-size: 0.55em; font-weight: 700; color: var(--accent2); margin-bottom: 6px; }
    .adv-card .adv-desc { font-size: 0.4em; color: #cbd5e1; line-height: 1.6; }

    /* === 段落結構地圖卡片 === */
    .step-card {
      background: var(--card-bg);
      border-radius: 12px;
      padding: 16px 12px;
      text-align: left;
      border: 1px solid var(--card-border);
    }
    .step-card.qi   { border-top: 4px solid #81c784; }
    .step-card.cheng{ border-top: 4px solid #4fc3f7; }
    .step-card.zhuan{ border-top: 4px solid #ffb74d; }
    .step-card.he   { border-top: 4px solid #e8643a; }
    .step-badge {
      display: inline-block; padding: 2px 8px; border-radius: 6px;
      font-size: 0.35em; font-weight: 700; margin-bottom: 6px;
    }
    .step-card.qi    .step-badge { background: rgba(129,199,132,0.2); color: #81c784; }
    .step-card.cheng .step-badge { background: rgba(79,195,247,0.2);  color: #4fc3f7; }
    .step-card.zhuan .step-badge { background: rgba(255,183,77,0.2);  color: #ffb74d; }
    .step-card.he    .step-badge { background: rgba(232,100,58,0.2);  color: #e8643a; }
    .step-title { font-size: 0.52em; font-weight: 700; margin-bottom: 6px; color: #fff; }
    .step-desc  { font-size: 0.38em; color: #cbd5e1; line-height: 1.5; }

    /* === 好詞百寶箱標籤 === */
    .tag-container {
      display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin: 12px 0;
    }
    .vocab-tag {
      background: rgba(79,195,247,0.12);
      border: 1px solid rgba(79,195,247,0.35);
      color: #e0f2fe;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.42em;
      font-weight: 600;
    }
    .vocab-tag.highlight {
      background: rgba(232,100,58,0.2);
      border-color: var(--accent);
      color: #ffccbc;
    }

    /* === 鷹架填空句型卡 === */
    .sentence-scaffold {
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(255,255,255,0.15);
      border-left: 5px solid var(--accent2);
      border-radius: 10px;
      padding: 16px 20px;
      font-size: 0.5em;
      line-height: 1.8;
      text-align: left;
      margin: 12px 0;
      box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }
    .fill-blank {
      color: var(--warn);
      background: rgba(255,183,77,0.15);
      padding: 2px 8px;
      border-radius: 4px;
      border-bottom: 2px dashed var(--warn);
      font-weight: 700;
    }

    /* === 雙欄排版 === */
    .two-col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      align-items: stretch;
      margin-top: 0.6em;
    }
    .col-box {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 18px;
      text-align: left;
    }

    /* === 滑桿對比組件 === */
    .slider-box {
      position: relative;
      height: 380px;
      border-radius: 14px;
      overflow: hidden;
      border: 1px solid rgba(255,255,255,0.18);
      background: #111827;
      margin-top: 10px;
    }
    .slider-layer {
      position: absolute;
      inset: 0;
      padding: 24px;
      box-sizing: border-box;
      text-align: left;
      font-size: 0.44em;
      line-height: 1.8;
      overflow-y: auto;
    }
    .slider-layer.before {
      background: #1e1b4b;
      color: #e0e7ff;
    }
    .slider-layer.after {
      background: #064e3b;
      color: #ecfdf5;
      clip-path: inset(0 100% 0 0);
    }
    .slider-divider {
      position: absolute;
      top: 0; left: 0;
      width: 3px; height: 100%;
      background: linear-gradient(to bottom, transparent, #4fc3f7, #81c784, transparent);
      box-shadow: 0 0 14px #4fc3f7;
      pointer-events: none;
    }
    .slider-ctrl {
      width: 80%;
      margin: 14px auto 0;
      display: block;
      accent-color: var(--accent2);
    }

    /* === 完整作文展示羊皮紙樣式 === */
    .essay-scroll {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 12px;
      padding: 20px 26px;
      font-size: 0.42em;
      line-height: 1.9;
      text-align: justify;
      color: #f8fafc;
      max-height: 440px;
      overflow-y: auto;
      box-shadow: inset 0 2px 10px rgba(0,0,0,0.5);
    }
    .essay-scroll p { margin-bottom: 1em; text-indent: 2em; }

    /* === 動畫與按鈕 === */
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.6; } }
    .btn-action {
      background: var(--accent2);
      color: #0d1117;
      border: none;
      padding: 9px 18px;
      border-radius: 8px;
      font-weight: 700;
      cursor: pointer;
      font-family: inherit;
    }
  </style>
</head>
<body>
<div class="reveal">
  <div class="slides">

    <!-- Slide 1: 封面 [BG] -->
    <section data-background-image="images/cover.png"
             data-background-opacity="0.32"
             data-background-size="cover">
      <div class="title-slide">
        <div class="tag">國小國語四年級寫作力大躍進 · 翰林版對齊</div>
        <h1 style="color:#ffffff;">《快樂的家庭活動》</h1>
        <h2 style="color:var(--accent); font-size:1.15em; margin-top:0.2em;">從句型鷹架到精彩作文的大冒險</h2>
        <p class="subtitle">
          打破「寫作腦袋空空」的魔咒！掌握起承轉合與課文好詞百寶箱，<br>
          只要填空完成，就是一篇 400~500 字的生動記敘文。
        </p>
        <p class="author">臺中市梧棲區中正國小 四年級國語教學團隊</p>
      </div>
    </section>

    <!-- Slide 2: 互動文字雲 [INTERACT:wordcloud] -->
    <section id="slide-wordcloud">
      <h2>即時破冰：提到家庭活動，你第一個想到什麼？</h2>
      <div style="display:grid; grid-template-columns:260px 1fr; gap:16px; height:450px;">
        <!-- 左欄：輸入與即時統計 -->
        <div style="display:flex; flex-direction:column; gap:10px;">
          <div style="background:var(--card-bg); border:1px solid var(--card-border); border-radius:10px; padding:14px;">
            <div style="font-size:0.38em; color:var(--accent2); font-weight:700; margin-bottom:8px;">輸入你的關鍵詞</div>
            <input id="wc-input" type="text" placeholder="例：烤肉、露營、散步…" maxlength="15"
              style="width:100%; padding:8px 12px; border-radius:8px; border:1px solid rgba(79,195,247,0.3);
                     background:rgba(255,255,255,0.08); color:#fff; font-size:13px;
                     box-sizing:border-box; font-family:inherit; outline:none;" />
            <button id="wc-btn" class="btn-action" style="width:100%; margin-top:8px;">送出靈感 ↵</button>
          </div>
          <div style="background:var(--card-bg); border:1px solid var(--card-border); border-radius:10px; padding:12px; flex:1; display:flex; flex-direction:column; overflow:hidden;">
            <div style="font-size:0.36em; color:var(--accent2); font-weight:700; margin-bottom:6px;">
              全班即時靈感
              <span style="display:inline-block; background:#ff4757; color:#fff; padding:1px 6px; border-radius:10px; font-size:0.85em; animation:pulse 1.5s infinite;">LIVE</span>
            </div>
            <div id="wc-list" style="font-size:0.33em; overflow-y:auto; flex:1; color:#cbd5e1;"></div>
            <div style="margin-top:6px; font-size:0.3em; color:#94a3b8; border-top:1px solid rgba(255,255,255,0.08); padding-top:4px; display:flex; justify-content:space-between; align-items:center;">
              <div>總提交：<span id="wc-total" style="color:var(--accent); font-weight:700;">0</span> 則　多樣：<span id="wc-unique" style="color:var(--accent2); font-weight:700;">0</span> 種</div>
              <button id="wc-reset-btn" title="新班級重置文字雲" style="background:transparent; border:1px solid rgba(255,255,255,0.2); color:#94a3b8; border-radius:4px; font-size:11px; padding:2px 6px; cursor:pointer;">重置 ↺</button>
            </div>
          </div>
        </div>

        <!-- 右欄：文字雲視覺化 -->
        <div style="background:rgba(255,255,255,0.03); border-radius:12px; overflow:hidden; position:relative; border:1px solid rgba(255,255,255,0.08);">
          <canvas id="wc-canvas" style="width:100%; height:100%; display:block;"></canvas>
          <div id="wc-empty" style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); color:#64748b; font-size:0.42em; text-align:center; pointer-events:none; line-height:1.8;">
            在左側輸入你的點子<br>全班靈感文字雲立刻浮現 ✨
          </div>
        </div>
      </div>
    </section>

    <!-- Slide 3: 寫作三大通關密碼 [ICON] -->
    <section>
      <h2>寫作大解密：掌握三大通關密碼</h2>
      <p style="font-size:0.45em; color:#94a3b8; margin-top:-0.4em;">寫作不是默背，而是把腦海中溫暖的記憶，用積木拼圖組合起來！</p>
      
      <div class="card-grid-3">
        <div class="adv-card fragment">
          <div class="adv-icon"><img src="images/icon_puzzle.png" alt="句型鷹架"></div>
          <div class="adv-title">① 句型搭鷹架</div>
          <div class="adv-desc">不用自己從零擠出字句。透過給定句型引導，填入自己經歷的細節，像蓋城堡一樣穩定安心。</div>
        </div>
        <div class="adv-card fragment">
          <div class="adv-icon"><img src="images/icon_chest.png" alt="好詞寶箱"></div>
          <div class="adv-title">② 課文好詞寶箱</div>
          <div class="adv-desc">「大顯身手」、「煙霧瀰漫」、「美妙動人」...不用生硬死背，直接活用國語課本真實生詞！</div>
        </div>
        <div class="adv-card fragment">
          <div class="adv-icon"><img src="images/icon_steps.png" alt="四步成篇"></div>
          <div class="adv-title">③ 四步自然成篇</div>
          <div class="adv-desc">依照起、承、轉、合四大段落循序思考，寫完直接連成 400~500 字佳作，告別塗改卡關。</div>
        </div>
      </div>
    </section>

    <!-- Slide 4: 全篇架構：起承轉合四部曲 -->
    <section>
      <h2>全篇架構地圖：起承轉合四部曲</h2>
      <p style="font-size:0.45em; color:#94a3b8; margin-top:-0.4em;">就像一部精彩的電影，文章要有好的開始、精彩過程、意外插曲與回味無窮的收尾：</p>
      
      <div class="card-grid-4">
        <div class="step-card qi fragment">
          <span class="step-badge">第一段</span>
          <div class="step-title">🟩 起：活動開場</div>
          <div class="step-desc">
            • 交代時間、地點<br>
            • 出現的主要家人<br>
            • 出發前的期待心情
          </div>
        </div>
        <div class="step-card cheng fragment">
          <span class="step-badge">第二段</span>
          <div class="step-title">🟦 承：分工與體驗</div>
          <div class="step-desc">
            • 家人分工合作默契<br>
            • 五感描寫（色香味）<br>
            • 融入惜食生活素養
          </div>
        </div>
        <div class="step-card zhuan fragment">
          <span class="step-badge">第三段</span>
          <div class="step-title">🟧 轉：難忘插曲</div>
          <div class="step-desc">
            • 趣味意外（棉花糖著火）<br>
            • 從緊張到破涕為笑<br>
            • 結合生活科學觀察
          </div>
        </div>
        <div class="step-card he fragment">
          <span class="step-badge">第四段</span>
          <div class="step-title">🟨 合：心得與金句</div>
          <div class="step-desc">
            • 活動收尾的深刻感受<br>
            • 體會家人相聚真諦<br>
            • 運用名言金句昇華
          </div>
        </div>
      </div>
    </section>

    <!-- Slide 5: 第一段（起）：熱鬧開場 -->
    <section>
      <h2>第一段（起）：活動熱鬧開場</h2>
      <p style="font-size:0.45em; color:#94a3b8; margin-top:-0.4em;">好的開始是成功的一半！先把「什麼時間、和誰、帶著什麼心情」清楚點出。</p>
      
      <div class="sentence-scaffold">
        <p><strong>每到</strong><span class="fill-blank">【中秋節】</span>，<strong>窗外的月亮像一面明亮的圓鏡，我們全家都會聚在一起。</strong></p>
        <p><strong>這一天，我和</strong><span class="fill-blank">【爸爸、媽媽、哥哥】</span>，<strong>帶著期待的心情準備烤肉。</strong></p>
        <p><strong>想到可以和親愛的家人聚在一起，我的心情就像</strong><span class="fill-blank">【高聲歡呼一樣快樂】</span>！</p>
      </div>

      <div style="background:var(--card-bg); border-radius:10px; padding:12px 18px; margin-top:10px;">
        <span style="font-size:0.38em; color:var(--warn); font-weight:700;">💡 課本好詞推薦（翰林真實生詞）：</span>
        <div class="tag-container" style="margin-top:6px;">
          <span class="vocab-tag highlight">高聲歡呼</span>
          <span class="vocab-tag">快樂</span>
          <span class="vocab-tag">溫暖</span>
          <span class="vocab-tag">健康平安</span>
          <span class="vocab-tag">美好時光</span>
        </div>
      </div>
    </section>

    <!-- Slide 6: 避坑指南① 滑桿對比 [VIZ] -->
    <section>
      <h2>寫作避坑指南①：告別流水帳！</h2>
      <p style="font-size:0.42em; color:#94a3b8; margin-top:-0.4em;">
        拖動下方滑桿，看看「流水帳開頭」與「優質鷹架開頭」的巨大差異：
      </p>

      <div class="slider-box">
        <div class="slider-layer before">
          <div style="color:#f87171; font-weight:700; font-size:1.1em; margin-bottom:8px;">❌ 常見流水帳寫法（代碼 C4-TEXT-01）</div>
          <p>
            今天是中秋節。我們全家一起去烤肉。我們帶了肉跟菜。我們先烤肉，然後又吃肉，接著又吃香腸。吃完香腸之後，哥哥去洗手，媽媽在旁邊坐著。我們吃很多東西，我覺得烤肉很好吃，大家都很飽。
          </p>
          <div style="color:#fca5a5; margin-top:12px; font-size:0.9em;">
            ⚠️ 缺點：缺少環境氛圍、缺乏修辭譬喻、全是一連串動作堆疊，索然無味。
          </div>
        </div>

        <div class="slider-layer after" id="viz1-after">
          <div style="color:#34d399; font-weight:700; font-size:1.1em; margin-bottom:8px;">✅ 鷹架引導優質寫法</div>
          <p>
            每到中秋節，窗外的月亮像一面明亮的圓鏡，我們全家都會聚在一起。這一天，我和爸爸、媽媽、哥哥，帶著期待的心情準備烤肉。想到可以和親愛的家人聚在一起，我的心情就像高聲歡呼一樣快樂！
          </p>
          <div style="color:#a7f3d0; margin-top:12px; font-size:0.9em;">
            ✨ 優點：景物譬喻（圓鏡）、主角同行交代分明、心情生動躍然紙上！
          </div>
        </div>

        <div class="slider-divider" id="viz1-divider"></div>
      </div>

      <input type="range" min="0" max="100" value="0" class="slider-ctrl" id="viz1-slider" />
      <div style="display:flex; justify-content:space-between; width:80%; margin:4px auto 0; font-size:0.35em; color:#94a3b8;">
        <span>👈 拖曳查看【流水帳】</span>
        <span>拖曳查看【鷹架美文】 👉</span>
      </div>
    </section>

    <!-- Slide 7: 第二段（承）：五感體驗與分工 [ICON] -->
    <section>
      <h2>第二段（承）：分工合作與五感體驗</h2>
      <p style="font-size:0.45em; color:#94a3b8; margin-top:-0.4em;">讓文章「香氣四溢」的秘密：打開你的眼睛、鼻子、嘴巴與皮膚感受！</p>

      <div class="two-col">
        <div class="col-box">
          <h3 style="color:var(--accent2); font-size:0.6em; margin-bottom:8px;">🍴 課本好詞融入句型</h3>
          <div style="font-size:0.38em; line-height:1.8; color:#cbd5e1;">
            • 爸爸烤肉時：<span style="color:var(--accent2); font-weight:700;">大顯身手</span><br>
            • 媽媽細心調味：讓我<span style="color:var(--accent2); font-weight:700;">大飽口福</span><br>
            • 炭火跳躍：空氣中<span style="color:var(--accent2); font-weight:700;">煙霧瀰漫</span><br>
            • 嘴裡吃著：<span style="color:var(--accent2); font-weight:700;">熱呼呼</span> 的美食無比舒服
          </div>
        </div>

        <div class="col-box" style="border-top:4px solid var(--accent);">
          <div class="adv-icon" style="text-align:center;"><img src="images/icon_bbq.png" alt="家庭燒烤" style="width:65px; height:65px; filter:drop-shadow(0 0 10px rgba(232,100,58,0.7));"></div>
          <div style="font-size:0.42em; font-weight:700; color:var(--accent); text-align:center; margin-bottom:4px;">五感立體描寫法</div>
          <div style="font-size:0.35em; color:#cbd5e1; line-height:1.6;">
            👁️ 視覺：金黃火光跳躍<br>
            👃 嗅覺：一陣陣烤肉香氣撲鼻<br>
            👅 味覺：熱呼呼、鮮甜多汁<br>
            👂 聽覺：家人成群結隊有說有笑
          </div>
        </div>
      </div>
    </section>

    <!-- Slide 8: 素養微加分：愛惜食物愛地球 -->
    <section>
      <h2>🌱 生活素養微加分：責任消費愛地球</h2>
      <p style="font-size:0.45em; color:#94a3b8; margin-top:-0.4em;">記敘文不只寫「吃吃喝喝」，更能寫出對生活的反思與好習慣！</p>

      <div class="two-col" style="margin-top:1em;">
        <div class="col-box" style="border-top:4px solid var(--success);">
          <div style="color:var(--success); font-weight:700; font-size:0.55em; margin-bottom:8px;">🌍 SDG 12：負責任的生活實踐</div>
          <div style="font-size:0.4em; color:#cbd5e1; line-height:1.7;">
            • <strong>吃多少、烤多少</strong>：珍惜食材不浪費，對大自然的餽贈心存感激。<br>
            • <strong>自備環保餐具</strong>：少用免洗筷與塑膠杯，落實減塑愛地球。<br>
            • <strong>收拾整理好榜樣</strong>：活動結束後隨手做分類，環境更整潔。
          </div>
        </div>

        <div class="sentence-scaffold" style="margin:0; border-left-color:var(--success);">
          <div style="color:var(--success); font-weight:700; margin-bottom:6px;">📝 放入文章中的金句鷹架：</div>
          「大家吃多少烤多少、愛惜食物不浪費，現場成群結隊的家人有說有笑，真是美好！」
        </div>
      </div>
    </section>

    <!-- Slide 9: 第三段（轉）：棉花糖著火記 [BG] -->
    <section data-background-image="images/marshmallow.png"
             data-background-opacity="0.32"
             data-background-size="cover">
      <h2>第三段（轉）：最難忘的驚喜插曲！</h2>
      <p style="font-size:0.45em; color:#cbd5e1; margin-top:-0.4em;">
        平鋪直敘會讓人想打哈欠！加入一點意外或插曲，文章立刻活潑生動起來。
      </p>

      <div class="sentence-scaffold" style="background:rgba(13,17,23,0.85);">
        <p><strong>最讓我難忘的是大家一起烤棉花糖時</strong><span class="fill-blank">【新奇】</span><strong>的體驗。</strong></p>
        <p><strong>正當我們帶著</strong><span class="fill-blank">【好奇】</span><strong>的心情轉動竹籤時，突然一陣風吹過來，棉花糖靠得太近，</strong><span class="fill-blank">【竟然】</span><strong>著火了！</strong></p>
        <p><strong>哥哥看見後非常</strong><span class="fill-blank">【驚訝】</span>，<strong>大家</strong><span class="fill-blank">【克服】</span><strong>了手忙腳亂的緊張，趕緊把火吹熄，棉花糖</strong><span class="fill-blank">【彷彿】</span><strong>變成了一顆黑色小煤炭。</strong></p>
      </div>

      <div style="font-size:0.38em; color:var(--warn); margin-top:8px;">
        💡 轉折三部曲：期待（新奇、好奇）➔ 意外（竟然著火）➔ 解決（克服手忙腳亂、彷彿小煤炭）
      </div>
    </section>

    <!-- Slide 10: STEAM 小偵探：棉花糖著火記 -->
    <section>
      <h2>🔬 STEAM 小偵探：生活處處是科學</h2>
      <p style="font-size:0.45em; color:#94a3b8; margin-top:-0.4em;">把生活中的科學好奇寫進作文，文章層次立刻超越一般同學！</p>

      <div class="card-grid-3">
        <div class="step-card cheng fragment">
          <div class="step-title">1. 熱對流與風向</div>
          <div class="step-desc">突來的一陣風改變了熱氣流動方向，讓高溫火焰突然偏向竹籤。</div>
        </div>
        <div class="step-card zhuan fragment">
          <div class="step-title">2. 糖的焦糖化與燃點</div>
          <div class="step-desc">棉花糖主要成分是糖，受熱時水分蒸發，一旦太靠近炭火便達到著火點。</div>
        </div>
        <div class="step-card he fragment">
          <div class="step-title">3. 爸爸的科學講解</div>
          <div class="step-desc">「爸爸笑著說明火候與受熱的原理」，把笑料昇華為溫馨的親子學習時刻！</div>
        </div>
      </div>
    </section>

    <!-- Slide 11: 第四段（合）：收尾心得與名言金句 -->
    <section>
      <h2>第四段（合）：收尾心得與名言金句</h2>
      <p style="font-size:0.45em; color:#94a3b8; margin-top:-0.4em;">好的結尾就像一首好歌的最後一個音符，餘音繞樑、溫暖人心。</p>

      <div class="sentence-scaffold">
        <p><strong>這次的家庭活動，讓我深深覺得</strong><span class="fill-blank">【美妙動人】</span>。</p>
        <p><strong>這次活動不但讓我</strong><span class="fill-blank">【大開眼界】</span>，<strong>也讓我更加體會到家人的愛與陪伴是世界上最珍貴的寶物。</strong></p>
        <p><strong>常言道：</strong><span style="color:var(--accent2); font-weight:700;">「快樂不一定要去很遠的地方，只要一家人在一起，就是最美好的時光！」</span></p>
      </div>

      <div style="background:var(--card-bg); border-radius:10px; padding:12px; margin-top:12px; font-size:0.38em; color:#cbd5e1;">
        ✨ <strong>結尾兩大錦囊：</strong>
        ① <strong>昇華主題</strong>：從「吃烤肉的快樂」延伸到「體會家人相聚的幸福」<br>
        ② <strong>引用金句</strong>：運用恰當的俗語或金句，讓結論力道十足！
      </div>
    </section>

    <!-- Slide 12: 避坑指南② 標點符號防呆 [INTERACT:poll] -->
    <section id="slide-poll">
      <h2>避坑指南②：標點符號神探（隨堂快問快答）</h2>
      <p style="font-size:0.42em; color:#94a3b8; margin-top:-0.4em;">
        抓出「一逗到底（C4-PUNCT-01）」與標點誤用！請選出標點符號使用<strong>最正確</strong>的句子：
      </p>

      <div id="poll-options" style="display:flex; flex-direction:column; gap:10px; margin-top:0.6em;">
        <!-- 動態生成選項 -->
      </div>
      <div style="font-size:0.36em; color:#94a3b8; text-align:center; margin-top:0.8em; display:flex; justify-content:center; align-items:center; gap:16px;">
        <span>全班即時投票：<span id="poll-total" style="color:var(--accent2); font-weight:700;">0</span> 人已作答</span>
        <button id="poll-reset-btn" title="新班級重置投票" style="background:transparent; border:1px solid rgba(255,255,255,0.2); color:#94a3b8; border-radius:4px; font-size:11px; padding:2px 8px; cursor:pointer;">重置投票 ↺</button>
      </div>
    </section>

    <!-- Slide 13: 揭露魔法：學習單轉作文簿 [VIZ] -->
    <section>
      <h2>神奇魔法：從學習單到作文簿</h2>
      <p style="font-size:0.42em; color:#94a3b8; margin-top:-0.4em;">
        拖動滑桿！見證填空完成的學習單，如何順暢轉化為作文簿上的連貫篇章：
      </p>

      <div class="slider-box">
        <div class="slider-layer before">
          <div style="color:var(--warn); font-weight:700; font-size:1.1em; margin-bottom:8px;">📄 填寫完成的學習單卡片</div>
          <p>
            【第一段】每到（中秋節），窗外的月亮像一面明亮的圓鏡，我們全家都會聚在一起。這一天，我和（爸爸、媽媽、哥哥），帶著期待的心情準備烤肉。想到可以和親愛的家人聚在一起，我的心情就像（高聲歡呼一樣快樂）！<br><br>
            【第二段】活動一開始，我們先清洗新鮮的（蔬菜、水果）...爸爸烤肉時（大顯身手），媽媽細心調味讓我（大飽口福）...
          </p>
        </div>

        <div class="slider-layer after" id="viz2-after">
          <div style="color:var(--accent2); font-weight:700; font-size:1.1em; margin-bottom:8px;">📝 作文簿上的正式篇章（每段開頭空兩格）</div>
          <p>
            　　每到中秋節，窗外的月亮像一面明亮的圓鏡，我們全家都會聚在一起。這一天，我和爸爸、媽媽、哥哥，帶著期待的心情準備烤肉。想到可以和親愛的家人聚在一起，我的心情就像高聲歡呼一樣快樂！<br><br>
            　　活動一開始，我們先清洗新鮮的蔬菜、水果，接著整齊擺放在桌上。大家分工合作，爸爸在烤肉時大顯身手，媽媽則細心調味，讓我大飽口福...
          </p>
        </div>

        <div class="slider-divider" id="viz2-divider"></div>
      </div>

      <input type="range" min="0" max="100" value="0" class="slider-ctrl" id="viz2-slider" />
      <div style="display:flex; justify-content:space-between; width:80%; margin:4px auto 0; font-size:0.35em; color:#94a3b8;">
        <span>👈 填空學習單</span>
        <span>完整作文簿成文 👉</span>
      </div>
    </section>

    <!-- Slide 14: 完整範文欣賞 -->
    <section>
      <h2>完整範文配對欣賞（400~500 字）</h2>
      <p style="font-size:0.42em; color:#94a3b8; margin-top:-0.4em;">
        只要把四個段落依照順序連起來，一篇結構完整、感情真摯的佳作就誕生了！
      </p>

      <div class="essay-scroll">
        <p>
          每到中秋節，窗外的月亮像一面明亮的圓鏡，我們全家都會聚在一起。這一天，我和爸爸、媽媽、哥哥，帶著期待的心情準備烤肉。想到可以和親愛的家人聚在一起，我的心情就像高聲歡呼一樣快樂！
        </p>
        <p>
          活動一開始，我們先清洗新鮮的蔬菜、水果，接著整齊擺放在桌上。大家分工合作，爸爸在烤肉時大顯身手，媽媽則細心調味，讓我大飽口福。這時，我看見金黃的火光在木炭間跳躍，空氣中煙霧瀰漫。一陣陣烤肉的香氣飄過來，吃著熱呼呼的食物，讓人覺得無比舒服。大家吃多少烤多少、愛惜食物不浪費，現場成群結隊的家人有說有笑，真是美好！
        </p>
        <p>
          這次的活動中，最讓我難忘的是大家一起烤棉花糖時新奇的體驗。正當我們帶著好奇的心情轉動竹籤時，突然一陣風吹過來，棉花糖靠得太近，竟然著火了！哥哥看見後非常驚訝，大家克服了手忙腳亂的緊張，趕緊把火吹熄，棉花糖彷彿變成了一顆黑色小煤炭。爸爸笑著說明火候與受熱的原理，這場趣味插曲逗得大家合不攏嘴，過程實在太好玩了！
        </p>
        <p>
          這次的家庭活動，讓我深深覺得美妙動人。這次活動不但讓我大開眼界，也讓我更加體會到家人的愛與陪伴是世界上最珍貴的寶物。我發現，一家人能夠健康平安的圍坐在一起，就是最平淡卻深刻的幸福。常言道：「快樂不一定要去很遠的地方，只要一家人在一起，就是最美好的時光！」我真希望下次還能和家人一起舉辦更多溫馨有趣的家庭活動！
        </p>
      </div>
    </section>

    <!-- Slide 15: 封底行動鼓勵 [BG] -->
    <section data-background-image="images/ending.png"
             data-background-opacity="0.38"
             data-background-size="cover">
      <div class="title-slide">
        <h1 style="color:var(--accent2); margin-bottom:0.2em;">提起你的筆，你也是寫作小達人！</h1>
        <h2 style="color:var(--warn); font-size:1.05em;">寫作四字訣：起 · 承 · 轉 · 合</h2>
        <div style="max-width:620px; margin:1.2em auto; background:rgba(13,17,23,0.7); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:16px 20px; font-size:0.42em; line-height:1.8; text-align:left;">
          ✍️ <strong>抄寫小叮嚀：</strong><br>
          1. 作文簿每一段開始，第一行<strong>空兩格</strong>。<br>
          2. 一個完整句子說完，記得加上<strong>句號（。）</strong>，不要一逗到底。<br>
          3. 引用名言時，正確使用<strong>冒號（：）</strong>與<strong>引號（「」）</strong>。<br>
          4. 相信自己，家庭的溫暖與回憶，就是最棒的寫作素材！
        </div>
        <p class="subtitle" style="color:#94a3b8; font-size:0.45em;">
          祝福每位小朋友都能寫出屬於自己最幸福動人的篇章 ✨
        </p>
      </div>
    </section>

  </div>
</div>

<!-- Reveal.js JS -->
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
<script>
  Reveal.initialize({
    hash: true,
    transition: 'slide',
    transitionSpeed: 'default',
    backgroundTransition: 'fade',
    center: true,
    progress: true,
    controls: true,
    slideNumber: 'c/t',
    keyboardCondition: function() {
      // 若當前焦點在任何輸入框、textarea 或按鈕上，暫停 Reveal.js 快捷鍵響應
      const tag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
      return tag !== 'input' && tag !== 'textarea' && tag !== 'select';
    },
    plugins: []
  });

  // === VIZ 1: 流水帳 vs 鷹架滑桿 ===
  const s1 = document.getElementById('viz1-slider');
  if (s1) {
    s1.addEventListener('input', function() {
      const v = +this.value;
      document.getElementById('viz1-after').style.clipPath = `inset(0 ${100 - v}% 0 0)`;
      document.getElementById('viz1-divider').style.left = v + '%';
    });
  }

  // === VIZ 2: 學習單 vs 作文簿滑桿 ===
  const s2 = document.getElementById('viz2-slider');
  if (s2) {
    s2.addEventListener('input', function() {
      const v = +this.value;
      document.getElementById('viz2-after').style.clipPath = `inset(0 ${100 - v}% 0 0)`;
      document.getElementById('viz2-divider').style.left = v + '%';
    });
  }
</script>

<!-- Firebase 互動元件 (文字雲 & 投票) -->
<script type="module">
  import { initializeApp } from 'https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js';
  import {
    getFirestore, collection, addDoc, doc, setDoc, onSnapshot,
    serverTimestamp, query, orderBy
  } from 'https://www.gstatic.com/firebasejs/11.0.2/firebase-firestore.js';

  const firebaseConfig = {
    apiKey: "AIzaSyAYQhNavPSce17XtvDC5xnXyl9iUhW9KjA",
    authDomain: "teacherstudy-109ef.firebaseapp.com",
    projectId: "teacherstudy-109ef",
    storageBucket: "teacherstudy-109ef.firebasestorage.app",
    messagingSenderId: "196599230156",
    appId: "1:196599230156:web:cfe55d364df3ae1b9d5c69"
  };

  const app = initializeApp(firebaseConfig);
  const fdb = getFirestore(app);

  // === 元件一：即時文字雲 ===
  const wordsRef = collection(fdb, 'family_activity_writing_wordcloud');
  const COLORS = ['#4fc3f7','#e8643a','#ffb74d','#81c784','#ce93d8','#80deea','#f48fb1'];
  let wcData = [];

  // 防止 Reveal.js 快捷鍵（如空白鍵切頁、方向鍵等）干擾文字框輸入
  const inputEl = document.getElementById('wc-input');
  if (inputEl) {
    ['keydown', 'keyup', 'keypress'].forEach(evt => {
      inputEl.addEventListener(evt, e => {
        e.stopPropagation();
        if (e.stopImmediatePropagation) e.stopImmediatePropagation();
      });
    });
  }

  function renderWordCloudData(words) {
    const counts = {};
    words.forEach(w => {
      if (w && typeof w === 'string') {
        const trimmed = w.trim();
        if (trimmed) counts[trimmed] = (counts[trimmed] || 0) + 1;
      }
    });
    wcData = Object.entries(counts).sort((a, b) => b[1] - a[1]);

    const totalEl = document.getElementById('wc-total');
    const uniqueEl = document.getElementById('wc-unique');
    if (totalEl) totalEl.textContent = words.length;
    if (uniqueEl) uniqueEl.textContent = wcData.length;

    const listEl = document.getElementById('wc-list');
    if (listEl) {
      listEl.innerHTML = wcData.slice(0, 10).map(([w, c]) =>
        `<div style="display:flex;justify-content:space-between;padding:3px 0;border-bottom:1px solid rgba(255,255,255,0.06);">
          <span>${w}</span><span style="color:var(--accent);font-weight:700;">${c}</span>
        </div>`
      ).join('') || '<div style="color:#64748b;padding:6px 0;">尚無資料，快當第一個！</div>';
    }

    const empty = document.getElementById('wc-empty');
    if (empty) empty.style.display = wcData.length > 0 ? 'none' : '';
    drawWordCloud();
  }

  // 本地快取與容錯
  function getLocalWords() {
    try {
      return JSON.parse(localStorage.getItem('family_wc_words') || '[]');
    } catch(e) { return []; }
  }
  function saveLocalWord(word) {
    try {
      const arr = getLocalWords();
      arr.push(word);
      localStorage.setItem('family_wc_words', JSON.stringify(arr));
      return arr;
    } catch(e) { return []; }
  }

  // 初始載入本地預設（若雲端連線失敗或尚無資料時有預設靈感）
  let localWords = getLocalWords();
  if (localWords.length === 0) {
    localWords = ['烤肉', '中秋節', '棉花糖', '大顯身手', '歡聚', '笑聲', '愛惜食物'];
    localStorage.setItem('family_wc_words', JSON.stringify(localWords));
  }
  renderWordCloudData(localWords);

  window.wcSubmit = async function() {
    const input = document.getElementById('wc-input');
    const word = input.value.trim();
    if (!word) return;
    const btn = document.getElementById('wc-btn');
    btn.disabled = true;

    // 先存入本地，確保即便 Firestore 延遲或權限異常也能即時看到互動效果
    const updated = saveLocalWord(word);
    renderWordCloudData(updated);

    try {
      await addDoc(wordsRef, { word, created_at: serverTimestamp() });
    } catch(e) {
      console.warn("Firestore 雲端同步失敗（已保存在本機/離線模式）:", e);
    } finally {
      input.value = '';
      btn.disabled = false;
      input.focus();
    }
  };

  document.getElementById('wc-input')?.addEventListener('keydown', e => {
    if (e.key === 'Enter') {
      e.preventDefault();
      e.stopPropagation();
      window.wcSubmit();
    }
  });
  document.getElementById('wc-btn')?.addEventListener('click', window.wcSubmit);

  // 嘗試監聽 Firestore 雲端同步
  try {
    onSnapshot(query(wordsRef, orderBy('created_at', 'asc')), snap => {
      const cloudWords = [];
      snap.forEach(doc => {
        const data = doc.data();
        if (data && data.word) cloudWords.push(data.word);
      });
      if (cloudWords.length > 0) {
        // 合併雲端與本地
        const merged = Array.from(new Set([...cloudWords, ...getLocalWords()]));
        renderWordCloudData(merged);
      }
    }, err => {
      console.warn("Firestore onSnapshot 離線備援啟用:", err.message);
    });
  } catch(err) {
    console.warn("無法啟動 Firestore 監聽:", err);
  }

  // 重置文字雲（支援一鍵清空/新班級開局）
  document.getElementById('wc-reset-btn')?.addEventListener('click', () => {
    if (confirm('確定要清空文字雲，讓下一班學生重新輸入嗎？')) {
      localStorage.removeItem('family_wc_words');
      renderWordCloudData([]);
    }
  });

  function drawWordCloud() {
    const canvas = document.getElementById('wc-canvas');
    if (!canvas || typeof WordCloud === 'undefined') return;
    const rect = canvas.getBoundingClientRect();
    if (rect.width < 10 || rect.height < 10) return;
    canvas.width = rect.width;
    canvas.height = rect.height;
    if (wcData.length === 0) return;
    const maxCount = wcData[0][1];
    WordCloud(canvas, {
      list: wcData.map(([w, c]) => [w, Math.max(16, Math.round((c / maxCount) * 60))]),
      gridSize: 6,
      weightFactor: 1,
      fontFamily: '"Segoe UI", "Noto Sans TC", sans-serif',
      color: () => COLORS[Math.floor(Math.random() * COLORS.length)],
      backgroundColor: 'transparent',
      rotateRatio: 0.25,
      shuffle: true,
    });
  }

  Reveal.on('slidechanged', e => {
    if (e.currentSlide?.id === 'slide-wordcloud') {
      setTimeout(drawWordCloud, 150);
    }
  });

  // === 元件二：單選投票 (標點符號診斷) ===
  const OPTIONS = [
    { id: 'a', label: 'A. 今天是中秋節，我們去烤肉，吃很多肉，哥哥喝果汁，我很開心。' },
    { id: 'b', label: 'B. 常言道：「只要一家人在一起，就是最美好的時光！」這句話說得真好。' },
    { id: 'c', label: 'C. 爸爸在烤肉時大顯身手，媽媽細心調味。讓我大飽口福。' }
  ];
  const pollRef = doc(fdb, 'family_activity_writing_poll', 'slide12');
  const userId = 'user_' + Math.random().toString(36).slice(2, 9);
  let myVote = localStorage.getItem('family_poll_myvote');

  function renderPollResults(votes) {
    const counts = {};
    OPTIONS.forEach(o => counts[o.id] = 0);
    Object.values(votes).forEach(v => { if (counts[v] !== undefined) counts[v]++; });
    const total = Object.values(counts).reduce((a, b) => a + b, 0);

    const totalEl = document.getElementById('poll-total');
    if (totalEl) totalEl.textContent = total;

    OPTIONS.forEach(opt => {
      const pct = total > 0 ? Math.round((counts[opt.id] / total) * 100) : 0;
      const bar = document.getElementById(`poll-bar-${opt.id}`);
      const pctEl = document.getElementById(`poll-pct-${opt.id}`);
      const check = document.getElementById(`poll-check-${opt.id}`);
      if (bar) bar.style.width = pct + '%';
      if (pctEl) pctEl.textContent = pct + '%';
      if (check) {
        if (myVote === opt.id) {
          check.textContent = '✓';
          check.style.background = 'var(--accent2)';
          check.style.borderColor = 'var(--accent2)';
          check.style.color = '#0d1117';
          check.style.fontWeight = 'bold';
        } else {
          check.textContent = '';
          check.style.background = 'transparent';
          check.style.borderColor = 'rgba(255,255,255,0.3)';
        }
      }
    });
  }

  // 本地票數快取
  function getLocalPollVotes() {
    try {
      return JSON.parse(localStorage.getItem('family_poll_votes') || '{"u1":"b","u2":"b","u3":"a"}');
    } catch(e) { return {"u1":"b"}; }
  }

  const container = document.getElementById('poll-options');
  if (container) {
    OPTIONS.forEach(opt => {
      const btn = document.createElement('button');
      btn.id = `poll-btn-${opt.id}`;
      btn.innerHTML = `
        <div style="display:flex;align-items:center;gap:10px;">
          <span style="flex:0 0 22px;height:22px;border-radius:50%;border:2px solid rgba(255,255,255,0.3);
                       display:flex;align-items:center;justify-content:center;font-size:11px;"
                id="poll-check-${opt.id}"></span>
          <span style="flex:1;text-align:left;font-size:0.42em;line-height:1.4;">${opt.label}</span>
          <span id="poll-bar-wrap-${opt.id}"
                style="flex:0 0 100px;height:8px;background:rgba(255,255,255,0.1);border-radius:4px;overflow:hidden;">
            <div id="poll-bar-${opt.id}" style="height:100%;width:0;background:var(--accent2);border-radius:4px;transition:width 0.4s;"></div>
          </span>
          <span id="poll-pct-${opt.id}" style="flex:0 0 35px;text-align:right;font-size:0.4em;color:#94a3b8;">0%</span>
        </div>
      `;
      btn.style.cssText = `width:100%;padding:10px 14px;background:var(--card-bg);
        border:1px solid var(--card-border);border-radius:10px;color:#fff;
        cursor:pointer;font-family:inherit;text-align:left;transition:background 0.2s;`;
      btn.onclick = () => vote(opt.id);
      container.appendChild(btn);
    });
  }

  renderPollResults(getLocalPollVotes());

  async function vote(optId) {
    myVote = optId;
    localStorage.setItem('family_poll_myvote', optId);
    const local = getLocalPollVotes();
    local[userId] = optId;
    localStorage.setItem('family_poll_votes', JSON.stringify(local));
    renderPollResults(local);

    const data = {};
    data[`votes.${userId}`] = optId;
    data.updated_at = serverTimestamp();
    try {
      await setDoc(pollRef, data, { merge: true });
    } catch(e) {
      console.warn("Firestore 投票雲端同步失敗（已保存在本機）:", e);
    }
  }

  try {
    onSnapshot(pollRef, snap => {
      const data = snap.data() || {};
      const votes = data.votes || {};
      if (Object.keys(votes).length > 0) {
        renderPollResults(votes);
      }
    }, err => {
      console.warn("Firestore poll 離線備援啟用");
    });
  } catch(err) {
    console.warn("無法啟動 Firestore poll 監聽:", err);
  }

  // 重置投票結果（支援一鍵清空/新班級開局）
  document.getElementById('poll-reset-btn')?.addEventListener('click', () => {
    if (confirm('確定要清空全班投票紀錄，讓新班級重新作答嗎？')) {
      localStorage.removeItem('family_poll_votes');
      localStorage.removeItem('family_poll_myvote');
      myVote = null;
      renderPollResults({});
    }
  });
</script>

</body>
</html>
