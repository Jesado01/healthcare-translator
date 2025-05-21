import os
import uuid
import requests
from gtts import gTTS
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, "index.html")

def translate_libretranslate(text, target_lang_code):
    try:
        response = requests.post(
            "https://translate.argosopentech.com/translate",
            json={
                "q": text,
                "source": "auto",
                "target": target_lang_code,
                "format": "text"
            },
            timeout=10
        )
        data = response.json()
        print("🟢 Traducción recibida:", data)
        return data.get("translatedText", None)
    except Exception as e:
        print("❌ Error al traducir:", e)
        return None

@csrf_exempt
def translate_text(request):
    if request.method == "POST":
        input_text = request.POST.get("text")
        target_language = request.POST.get("language", "en")

        try:
            # Traducción segura con validación
            translated = translate_libretranslate(input_text, target_language)

            if not translated:
                return JsonResponse({
                    "translated": "❌ LibreTranslate not available or returned nothing.",
                    "audio_url": None
                })

            # Solo generar audio si hay texto válido
            tts = gTTS(text=translated, lang=target_language)
            filename = f"{uuid.uuid4()}.mp3"
            filepath = os.path.join("static", "audio", filename)
            tts.save(filepath)

            return JsonResponse({
                "translated": translated,
                "audio_url": f"/static/audio/{filename}"
            })

        except Exception as e:
            print("❌ Error al traducir o generar audio:", e)
            return JsonResponse({"error": "Server error. Check translation or audio step."}, status=500)

    return JsonResponse({"error": "Invalid method"}, status=405)