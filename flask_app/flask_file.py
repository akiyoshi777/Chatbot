from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    bot_reply = get_bot_reply(user_message)
    return jsonify({'bot_reply': bot_reply})

def get_bot_reply(message):
    # ここでボットの返答を定義します。簡単な例として、以下のようにしていますが、
    # 実際にはもっと複雑なロジックや外部APIの呼び出しを行うことができます。
    if "こんにちは" in message:
        return "こんにちは！"
    elif "名前" in message:
        return "私の名前はChatGPTです。"
    else:
        return "すみません、わかりません。"

if __name__ == '__main__':
    app.run(debug=True)
