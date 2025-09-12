from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time, json, schedule, datetime

# === 可調整變數 ===
# LINE路徑
LINE_PATH = r"C:\Users\User\AppData\Local\LINE\bin\LineLauncher.exe"
# 預設發送對話數量 (從上往下數)
RECIPIENT_COUNT = 1
# 訊息檔案路徑
JSON_PATH = "messages.json"

# === 啟動或連線 LINE ===
def check_line_running(retry=3, delay=5):
    for attempt in range(retry):
        try:
            app = Application(backend="uia").connect(title_re="LINE")
            return app
        except Exception as e:
            if attempt == 0:
                try:
                    app = Application(backend="uia").start(LINE_PATH)
                    time.sleep(delay)
                except Exception as start_err:
                    print(f"啟動 LINE 失敗: {start_err}")
            time.sleep(delay)
    print("連線或啟動 LINE 失敗，請確認 LINE 是否安裝或路徑正確。")
    return None
app = check_line_running()
win = app.window(title_re="LINE")
win.set_focus()

# 找到聊天清單
lists = win.descendants(control_type="List")
chat_list = max(lists, key=lambda l: len(l.children()))
chat_items = chat_list.children()

if len(chat_items) < RECIPIENT_COUNT:
    RECIPIENT_COUNT = len(chat_items)

# === 發送訊息函式 ===
def send_message(text):
    for i in range(RECIPIENT_COUNT):
        win.set_focus()
        chat_items[i].click_input()
        time.sleep(0.5)
        edits = win.descendants(control_type="Edit")
        edit = edits[0]
        edit.click_input()
        send_keys(text)
        send_keys("{ENTER}")
        print(f"[{datetime.datetime.now()}] 已發送給第 {i+1} 個對話: {text}")

# === 排程設定 ===
with open(JSON_PATH, "r", encoding="utf-8") as f:
    messages = json.load(f)

for msg in messages:
    send_time = datetime.datetime.strptime(msg["datetime"], "%Y-%m-%d %H:%M")
    
    # schedule 每分鐘檢查
    schedule.every().day.at(send_time.strftime("%H:%M")).do(send_message, text=msg["message"])

print("排程已設定，等待執行...")

while True:
    schedule.run_pending()
    time.sleep(30)
