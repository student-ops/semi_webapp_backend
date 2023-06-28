from flask import Flask, Response, request, jsonify
from src.llama import chat
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/llama_chat', methods=['POST'])
def llama_chat_route():
    data = request.json

    def generate():
        for response_text in chat.LlamaChat(data['prefecture'], data['question']):
            yield response_text  # Adding newline character for readability
    return Response(generate(), mimetype='text/plain')




# @app.route('/evaluate',methods =['POST'])
# def evaluate_route():
#     data = request.josn
#     evaluation.Evaluate(data['id'])

@app.route('/ping')
def ping(): return Response('Pong', mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
