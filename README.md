# LINE 自動訊息發送機器人

## 簡介
這是一個使用 Python 開發的自動化工具，能透過 **LINE 桌面版** 自動發送訊息。  
支援功能：
- 多人同時發送（從聊天清單最上方開始）
- 使用 JSON 設定訊息與時間
- 定時自動發送（排程）

## 安裝
1. 下載專案
   ```bash
   git clone https://github.com/mio1017/line-auto-sender.git
   cd line-message-bot
2. 安裝套件
   ```bash
   pip install -r requirements.txt
## 使用方式

1. 確認你的電腦已安裝 LINE 桌面版

2. 編輯 messages.json 設定要發送的訊息，例如：
   ```json
   [
     {"datetime": "2025-09-05 18:30", "message": "這是 9/5 自動訊息"},
     {"datetime": "2025-09-08 09:00", "message": "早安，這是 9/8 訊息"}
   ]
3. 執行程式
   ```bash
   python main.py
## 注意事項

* 需要 Windows 環境（因為使用 pywinauto 操作桌面應用程式）

* LINE 必須保持登入狀態

* 程式需要持續執行，才能在指定時間發送訊息

