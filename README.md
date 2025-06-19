# 🤖 AIChatbot – Flask + Gemini 1.5 Flash (Google AI) Chatbot

This project is a simple web-based **AI chatbot** powered by **Google's Gemini 1.5 Flash model**, integrated through Flask. It takes user input (via speech or text), sends it to the Gemini API, and returns the first sentence of the generated response.

---

## 🧠 Key Features

- ✅ Integrates with **Google's Gemini 1.5 Flash API**
- ✅ Built with **Flask**
- ✅ Supports text input from client (designed for speech-to-text UI)
- ✅ Returns the **first sentence** of the generated content
- ✅ Simple web interface (`s.html`)

---

## 🗂️ Folder Structure

ai-chatbot/
├── app.py # Main Flask backend
├── templates/
│ └── s.html # Frontend HTML file

yaml
Copy
Edit

---

## 🚀 How It Works

1. User input is collected on the front-end (e.g., spoken via mic or typed).
2. The input is sent via a GET request to `/generate_content/<text>`.
3. Flask forwards the input to the Gemini 1.5 Flash model via Google's API.
4. Only the **first sentence** of the response is returned and shown to the user.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/fayaf2/aichatbot.git
cd aichatbot
2. Install Dependencies
bash

pip install flask requests
3. Run the App
bash

python app.py
