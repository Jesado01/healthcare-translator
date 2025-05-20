import os
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from gtts import gTTS
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def index(request):
    return render(request, "index.html")

@csrf_exempt
def translate_text(request):
    if request.method == "POST":
        input_text = request.POST.get("text")
        target_language = request.POST.get("language")

        try:
            # Traducción con OpenAI GPT
            prompt = f"Traduce este texto médico al {target_language}: {input_text}"
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un traductor médico experto."},
                    {"role": "user", "content": prompt}
                ]
            )
            translated = response.choices[0].message.content.strip()

            # Generar audio con gTTS
            tts = gTTS(text=translated, lang="es")  # o usa target_language si soporta
            filename = f"{uuid.uuid4()}.mp3"
            filepath = f"static/audio/{filename}"
            tts.save(filepath)

            return JsonResponse({
                "translated": translated,
                "audio_url": f"/static/audio/{filename}"
            })

        except Exception as e:
            print("❌ Error:", e)
            return JsonResponse({"error": "Error processing translation."}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)