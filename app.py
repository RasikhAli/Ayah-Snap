from flask import Flask, render_template, jsonify
import requests
import random

app = Flask(__name__)

QURAN_API_URL = "http://api.alquran.cloud/v1/"
SURAH_RANGE = list(range(10, 29))  # Surahs from Yunus (10) to Qasas (28)
translation = None

# Function to get the total number of Ayahs in each Surah
def get_surah_ayah_counts():
    ayah_counts = {}
    for surah in SURAH_RANGE:
        response = requests.get(f"{QURAN_API_URL}surah/{surah}")
        if response.status_code == 200:
            data = response.json()
            ayah_counts[surah] = data["data"]["numberOfAyahs"]
        else:
            ayah_counts[surah] = 227  # Default fallback
    return ayah_counts

SURAH_AYAH_COUNTS = get_surah_ayah_counts()  # Cache Surah-Ayah mapping

# Function to get a random Ayah and its translation
def get_random_ayah():
    surah = random.choice(SURAH_RANGE)  # Pick a random Surah
    max_ayah = SURAH_AYAH_COUNTS.get(surah, 227)  # Get correct Ayah range
    ayah_number = random.randint(1, max_ayah)  

    # Fetch the Ayah from API
    response = requests.get(f"{QURAN_API_URL}ayah/{surah}:{ayah_number}")
    if response.status_code == 200:
        data = response.json()
        if "data" in data:
            arabic_ayah = data["data"]["text"]
            surah_name = data["data"]["surah"]["englishName"]
            ayah_number_in_surah = data["data"]["numberInSurah"]

            # Fetch translation
            translation_response = requests.get(f"{QURAN_API_URL}ayah/{surah}:{ayah_number}/en.asad")
            print(surah, ayah_number)
            print(surah, ayah_number_in_surah)
            translation_text = "No translation available"
            if translation_response.status_code == 200:
                translation_data = translation_response.json()
                if "data" in translation_data:
                    translation_text = translation_data["data"]["text"]
            global translation 
            translation = translation_text
            return arabic_ayah, surah_name, ayah_number_in_surah, translation_text

    return "Error fetching Ayah", "Unknown", "-", "Error fetching translation"

@app.route('/')
def home():
    ayah, surah_name, ayah_number, translation = get_random_ayah()
    return render_template("index.html", ayah=ayah, surah_name=surah_name, ayah_number=ayah_number, translation=translation)

@app.route('/get_translation')
def get_translation():
    return jsonify({'translation': translation})

if __name__ == "__main__":
    app.run(debug=True)
