from flask import Flask, Response, request, jsonify
from src.llama import chat
from flask_cors import CORS
from flask import stream_with_context
import sys

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/llama_chat', methods=['POST'])
def llama_chat_route():
    data = request.json
    question = data['question']
    question += "\n日本語で回答して"

    def generate():
        buffer = ""
        buffer_size = 0
        for response_text in chat.LlamaChat(bot_name=data['bot_name'], question=question):
            buffer += response_text
            buffer_size += len(response_text.encode('utf-8'))  # Get the byte size of the response_text in UTF-8

            if buffer_size >= 8:  # Send the buffer when its size reaches 20 bytes (5 characters in UTF-8)
                yield f"data: {buffer}\n\n"
                buffer = ""
                buffer_size = 0

        # Send any remaining data in the buffer
        if buffer:
            yield f"data: {buffer}\n\n"

    return Response(stream_with_context(generate()), mimetype='text/event-stream')
# @app.route('/evaluate',methods =['POST'])
# def evaluate_route():
#     data = request.josn
#     evaluation.Evaluate(data['id'])

@app.route('/ping')
def ping(): return Response('Pong', mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
