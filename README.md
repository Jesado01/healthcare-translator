# 🩺 Healthcare Translator Web App

A web application that enables real-time multilingual translation between patients and healthcare providers. Built with Django and OpenAI, it includes voice recognition, transcription, translation, and audio playback of the translated text.

## 🚀 Features

- 🎤 Voice recognition via browser (Web Speech API)
- 📝 Real-time transcription
- 🌍 AI-powered translation using OpenAI GPT
- 🔊 Text-to-speech playback using gTTS
- 📱 Mobile-first responsive interface
- ☁️ Deployed on Render

## 🛠️ Tech Stack

- Backend: **Python 3.10**, **Django 4+**
- AI: **OpenAI API (GPT-4)**
- Text-to-Speech: **gTTS**
- Frontend: **HTML5 + Bootstrap 5**
- Deployment: **Render**
- Server: **gunicorn**
- Env mgmt: **python-dotenv**

  ## 📂 Project Structure

```text
translator_app/
├── core/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── index.html
├── translator_app/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── manage.py
├── .gitignore
└── .env.example
```

## ⚙️ Environment Variables (`.env`)

This file must **NOT** be committed. Use `.env.example` as a reference:

```env
OPENAI_API_KEY=your-api-key-here
DJANGO_SETTINGS_MODULE=translator_app.settings
```

🧪 Run Locally
```clone
# Clone the repo
git clone https://github.com/Jesado01/healthcare-translator.git
cd healthcare-translator
```
```create
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
```install
# Install dependencies
pip install -r requirements.txt
```
```collect
# Collect static files
python manage.py collectstatic
```

```run
# Run the server
python manage.py runserver
```

🌐 Live Demo

Hosted on Render:
🔗 https://healthcare-translator-kq9w.onrender.com/

👤 Author

Developed by Jesus Coronado.
Contact: adolfo.coronado05@gmail.com
