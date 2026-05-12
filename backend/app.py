from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import sys

app = Flask(__name__)
CORS(app)  # CORS'u açıyoruz, böylece tarayıcı uzantıları, farklı frontend'ler bağlanabilir

MODEL_PATH = "./model/sarkazm-model"

try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, use_fast=False)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
    model.eval()  # Değerlendirme moduna al
    print(" Model ve tokenizer başarıyla yüklendi.")
except Exception as e:
    print(f" Model veya tokenizer yüklenirken hata oluştu: {e}")
    sys.exit(1)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Lütfen 'text' alanı ile POST isteği gönderin."}), 400

    text = data["text"]

    try:
        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding="max_length",
            max_length=128
        )

        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            prediction = torch.argmax(logits, dim=1).item()

        return jsonify({
            "text": text,
            "prediction": prediction,
            "is_sarcastic": bool(prediction)
        })

    except Exception as e:
        return jsonify({"error": f"Model tahmininde hata: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
