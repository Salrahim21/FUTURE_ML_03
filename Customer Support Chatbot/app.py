from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)

# Load model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    response_ids = model.generate(
        input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id
    )

    reply = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
