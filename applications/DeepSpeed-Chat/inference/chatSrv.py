import chatbot
from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

json_encoder = json.JSONEncoder()

@app.route('/chat_test', methods=['POST'])
def chat_test():
    data = json.loads(request.get_data())
    print(data)
    print('Model: ' + data['model'])
    print('Prompt: ' + data['prompt'])
    response = {'status': input('type status: '), 'message': input('type response: ')}
    response = json_encoder.encode(response)
    return response, 200

@app.route('/chat', methods=['POST'])
def chat():
    data = json.loads(request.get_data())
    print(data)
    print('Model: ' + data['model'])
    print('Prompt: ' + data['prompt'])

    # load global variable
    global generator
    global args

    # Let's play!

    prompt_to_gpt = f"Human: {data['prompt']}\n Assistant: "

    response = chatbot.get_model_response(generator, prompt_to_gpt, args.max_new_tokens)
    response = response[0]["generated_text"].replace("<|endoftext|></s>", "")
    response = response.split(prompt_to_gpt)[1].strip() # remove prompt header (Sounds stupid)
    print(f'Stage 1 response: {response}')
    response = response.split('Human: ')[0].strip() # remove illusion
    print(f'Stage 2 response: {response}')

    #response = input('Put your patched response here: ')
    response = {'status': 'OK', 'message': response}
    return response, 200

if __name__ == '__main__':
    args = chatbot.parse_args()
    generator = chatbot.get_generator(args.path)
    app.run(host='0.0.0.0', port=5000)