# Visual Bible 規範

每個專案正式生圖前，先建立以下內容，後續所有頁面都視為硬性一致性參考。

```yaml
canvas:
  ratio: "16:9"
  orientation: "landscape"
  resolution: "high"

style:
  illustration: "依使用者需求決定"
  texture: "保持全套一致"
  lighting: "保持全套一致"
  atmosphere: "依班級定位設定"

color:
  primary: ""
  secondary: ""
  accent: ""
  background: ""

characters:
  teacher:
    face: ""
    hair: ""
    outfit: ""
    body_ratio: ""
  students:
    style: ""
    diversity: "自然多元，不對應真實個別學生"
  parents:
    style: ""

layout:
  safe_margin: "至少畫面寬高的 5%"
  title_zone: "固定或準固定"
  content_zone: "保留足夠留白"

recurring_elements:
  - ""

negative_constraints:
  - "不要假英文"
  - "不要亂碼"
  - "不要多餘文字"
  - "不要水印"
  - "不要裁切標題"
  - "不要每頁改變畫風"
```

## 一致性檢查

每生成一頁都要比對：

1. 老師角色是否仍是同一人
2. 髮型與服裝是否一致
3. 主色與背景色是否一致
4. 插畫筆觸是否一致
5. 圓角、卡片、裝飾元素是否一致
6. 標題與重要資訊是否落在安全區
7. 16:9 是否正確
