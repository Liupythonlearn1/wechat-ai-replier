from wxauto import *
import time

# WeChatオブジェクトを初期化
wx = WeChat()

def main():
    print("微信アシスタントが起動され、メッセージの監視を開始します...")

    while True:
        # 最新のチャット履歴を取得
        msgs = wx.GetAllMessage()

        for msg in msgs:
            # メッセージが「ファイル転送アシスタント」からのものかを確認
            if msg[0] == "ファイル転送アシスタント":
                user_message = msg[1]
                print(f"OK: {user_message}")

                # ここで特定の返信メッセージを設定できます
                reply_message = "これは自動返信メッセージです。"

                # WeChatに返信を送信
                wx.SendMsg(reply_message, "ファイル転送アシスタント")

        # 資源を過度に消費しないように短い休止時間を設定
        time.sleep(5)

if __name__ == "__main__":
    main()
