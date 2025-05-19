import openai
from gtts import gTTS
from django.shortcuts import render
from django.http import JsonResponse
import os
from django.views.decorators.csrf import csrf_exempt
from translator_app.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def translate_text(request):
    if request.method == 'POST':
        text = request.POST.get("text")
        target_lang = request.POST.get("target_lang", "es")

        prompt = f"Translate the following medical conversation into {target_lang}: {text}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        translated = response.choices[0].message['content']

        tts = gTTS(translated, lang=target_lang)
        tts.save("core/static/translated.mp3")

        return JsonResponse({"translated": translated, "audio_url": "/static/translated.mp3"})