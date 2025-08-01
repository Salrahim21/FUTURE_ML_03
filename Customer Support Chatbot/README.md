
# 💬 Customer Support Chatbot

### ✅ Final Project – Task 3: Build a Smart Chatbot for Real-Time Customer Support

---

## 🔍 Project Overview

This project involves building an intelligent customer support chatbot capable of responding to real-time user queries using natural language understanding. The chatbot is trained and fine-tuned on real-world customer service data from Twitter and deployed on a beautiful web interface for seamless user experience.

---

## 🚀 Features

- 💡 Conversational AI using a pre-trained Hugging Face model  
- 📚 Trained on **Customer Support Conversations** dataset (Kaggle)  
- 🧠 Handles inbound queries and generates contextual support responses  
- 🌐 Fully deployed using **Flask** and a custom **HTML/CSS/JavaScript UI**  
- ✨ Beautiful liquid-glass styled chat UI with a **starry sky background**  
- 🔁 Smart fallback for unrecognized queries  

---

## 📂 Dataset

- **Source**: [Customer Support Conversations – Kaggle](https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter)  
- Contains real-world support tweets between customers and service providers  
- Used to fine-tune the chatbot’s understanding of customer intents and concerns  

---

## 🛠 Tools & Technologies

| Category             | Tools Used |
|----------------------|------------|
| Conversational Design| Hugging Face Transformers (DialoGPT) |
| Frontend UI          | HTML, CSS, JavaScript |
| Backend Framework    | Python Flask |
| NLP & AI             | Transformers, Tokenizers |
| Dataset Handling     | Pandas, Kaggle |
| Deployment Ready     | Flask App + Static Assets |

---

## 🧰 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Salrahim21/customer-support-chatbot.git
cd customer-support-chatbot
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Download the Dataset**

- Create a Kaggle account and place your API token in the project directory
- Run:

```bash
kaggle datasets download -d thoughtvector/customer-support-on-twitter
```

4. **Run the Flask App**

```bash
python app.py
```

5. **Open in Browser**

Visit: `http://127.0.0.1:5000`

---

## 💻 Project Structure

```
customer-support-chatbot/
├── app.py                 # Flask backend
├── chatbot.py             # Chat logic using Hugging Face model
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Web UI
├── static/
│   ├── style.css          # Aesthetic styling with glassmorphism
│   └── bot.jpg            # Starry sky background image
├── notebook.ipynb         # Exploratory data analysis
└── README.md              # Project documentation
```

---

## 🧠 Skills Demonstrated

- Intent recognition and smart reply generation using NLP  
- Multi-turn conversation flow using Hugging Face Transformers  
- Flask-based backend integration for serving AI models  
- Frontend styling using glassmorphism and star-themed visuals  
- Data preprocessing and conversational modeling  

---

## 📸 Preview

*(Replace with a real screenshot once hosted or finalized)*  
![screenshot](https://user-images.githubusercontent.com/Salrahim21/starry-bot-screenshot.jpg)  

---

## ✅ Deliverables Recap

| Deliverable                             | Status       |
|-----------------------------------------|--------------|
| Conversational design with fallback     | ✅ Completed |
| Hugging Face model fine-tuning          | ✅ Completed |
| Beautiful deployed interface (HTML/CSS) | ✅ Completed |
| Real-time chatbot support               | ✅ Completed |
| FAQ and support intent handling         | ✅ Completed |

---

## 🙌 Acknowledgments

- Dataset by ThoughtVector via Kaggle  
- Hugging Face DialoGPT  
- Flask community & open-source CSS aesthetics  

---

## 👨‍💻 Developer

Built with ❤️ by **Ibrahim Salim**  
🔗 GitHub: [github.com/Salrahim21](https://github.com/Salrahim21)  
