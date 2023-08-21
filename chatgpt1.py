import openai

class Chatbot:
    def __init__(self, api_key, qa_data):
        self.qa_data = qa_data
        openai.api_key = api_key

    def get_response(self, user_input):
        best_score = 0
        best_answer = ""

        for question, answer in self.qa_data:
            # ChatGPT APIを使用して、入力された質問と既存の質問の類似度を計算
            response = openai.Completion.create(
                engine="davinci",
                prompt=f"How similar are these two questions?\nQuestion 1: {user_input}\nQuestion 2: {question}\n",
                max_tokens=10
            )
            score = float(response.choices[0].text.strip().replace("%", ""))

            if score > best_score:
                best_score = score
                best_answer = answer

        return best_answer

if __name__ == "__main__":
    # サンプルのQAデータ
    qa_data = [
        ("何時に退社しますか？", "通常は18時に退社します。"),
        ("昼休みは何時ですか？", "昼休みは12時から13時です。"),
        # ... 他のQAデータ ...
    ]

    API_KEY = "YOUR_OPENAI_API_KEY"
    chatbot = Chatbot(API_KEY, qa_data)

    user_input = input("質問を入力してください: ")
    response = chatbot.get_response(user_input)
    print(f"回答: {response}")
