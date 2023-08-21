import openai
import numpy as np

# OpenAI APIキーの設定
openai.api_key = 'YOUR_OPENAI_API_KEY'

# 既存のQAデータ
qa_data = [
    {"question": "質問1", "answer": "回答1"},
    {"question": "質問2", "answer": "回答2"},
    # ... 他のQAデータ
]

# すべての質問の埋め込みを取得
embeddings = []
for item in qa_data:
    response = openai.Embedding.create(input=[item["question"]], model="text-embedding-ada-002")
    embeddings.append(response['data'][0]['embedding'])

# 新しい質問に対する最も類似した回答を返す関数
def get_best_answer(new_question):
    new_embedding = openai.Embedding.create(input=[new_question], model="text-embedding-ada-002")['data'][0]['embedding']
    best_index = np.argmax([np.dot(new_embedding, e) for e in embeddings])
    return qa_data[best_index]["answer"]

# 新しい質問の例
new_question = "新しい質問"
print(get_best_answer(new_question))