from flask import Flask, request
from ollama import chat
from ollama import ChatResponse


app = Flask(__name__)

@app.route('/mistral', methods=['POST'])
def mistral():
    data = request.get_json()
    prompt = data.get('prompt')
    response: ChatResponse = chat(model='mistral:7b', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])
    print(response)
    return response, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
