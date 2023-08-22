from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    # ここでChatbotのロジックを書く
    if "こんにちは" in user_message:
        response = "こんにちは！どのようにお手伝いできますか？"
    elif "ありがとう" in user_message:
        response = "どういたしまして！"
    else:
        response = "申し訳ございません、理解できませんでした。"
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
