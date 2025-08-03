from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import torch

app = Flask(__name__)

# Initialize the chatbot pipeline with a free model
# Using a smaller model that can run without API keys
chatbot = pipeline("text-generation", model="gpt2")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({'reply': "🤖 Please enter a message."})

    try:
        # Generate response with local model
        response = chatbot(
            user_input,
            max_length=100,
            num_return_sequences=1,
            pad_token_id=50256,  # End of text token for GPT-2
            no_repeat_ngram_size=2
        )
        
        if response and isinstance(response, list):
            reply = response[0]['generated_text'].strip()
            # Remove the input text from the response if it's included
            if reply.startswith(user_input):
                reply = reply[len(user_input):].strip()
        else:
            reply = "🤖 I didn't understand that. Could you rephrase?"

        return jsonify({'reply': f"🤖 {reply}"})
    except Exception as e:
        print("❌ Exception:", e)
        return jsonify({'reply': "🤖 Error generating response. Please try again."})

if __name__ == '__main__':
    app.run(debug=True)