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
    endpoints = [
        "https://translate.argosopentech.com/translate",
        "https://libretranslate.de/translate",
        "https://translate.astian.org/translate"
    ]

    for url in endpoints:
        try:
            response = requests.post(
                url,
                json={
                    "q": text,
                    "source": "auto",
                    "target": target_lang_code,
                    "format": "text"
                },
                timeout=10
            )
            data = response.json()
            translated = data.get("translatedText", "").strip()
            if translated:
                print(f"🟢 Traducción recibida desde {url}: {translated}")
                return translated
        except Exception as e:
            print(f"⚠️ Error usando {url}: {e}")
            continue

    print("❌ Todos los endpoints de LibreTranslate fallaron.")
    return None

@csrf_exempt
def translate_text(request):
    if request.method == "POST":
        input_text = request.POST.get("text")
        target_language = request.POST.get("language")

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