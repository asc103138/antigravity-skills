---
name: task-observer
description: 監視任務執行過程中的改進機會。在任何多步驟任務、備課、班級行政或教學工作流程中調用。能自動記錄使用者修正、工作流模式，並提煉為新技能或改進現有技能。
---

# Task Observer — 自動學習與技能演化系統 (OpenCode 版)

本技能基於 [rebelytics/one-skill-to-rule-them-all](https://github.com/rebelytics/one-skill-to-rule-them-all) 設計，適用於 OpenCode 環境。

## 核心理念
技能的最佳改進時機，來自於真實工作過程中的修正與摩擦。本技能在背景運行，靜默記錄每一次的反饋與調整，將重複工作轉化為結構化的可重複技能。

---

## 工作目錄與檔案結構

在專案目錄下建立並維護以下檔案結構：
```text
.opencode/
  ├── skills/                          # 存放各項已建立的專屬技能 (.md)
  └── skill-observations/
      ├── log.md                       # 當前進行中的觀察日誌 (主要記錄檔)
      ├── cross-cutting-principles.md  # 跨領域通用原則 (如隱私保護、教學語氣)
      ├── last-review-date.txt         # 記錄上次回顧日期 (初始值為: never)
      └── archive/                     # 存放已處理完成的歷史日誌
```
