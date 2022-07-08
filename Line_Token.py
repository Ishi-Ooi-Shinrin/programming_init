import requests

#アクセストークン
acc_token = 'AjGu9v6X1SjmARagmSEWSAC3MKGXJ2uLnu4Ed6yn33Y'

def send_line(msg):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}
    requests.post(url, headers=headers, params=payload)

if __name__ == '__main__':
    #メッセージ送信
    send_line('テスト')