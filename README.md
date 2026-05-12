# ai-sarcasm-detector
# 🛡️ AI-Based Sarcasm & Cyberbullying Detection Chrome Extension

An AI-powered Chrome extension that detects sarcastic and cyberbullying content on web pages in real time. The system analyzes user-generated text using a multilingual RoBERTa-based Large Language Model (LLM) and warns users about harmful content while optionally censoring detected messages.

---

## 📌 Project Overview

This project was developed as a Computer Engineering graduation project to create a safer online environment by detecting:
- Sarcastic comments
- Toxic language
- Cyberbullying content

The extension works directly on websites and social media platforms by analyzing text dynamically in the browser.

---

## 🚀 Features

- ✅ Real-time text analysis
- ✅ AI-powered sarcasm detection
- ✅ Cyberbullying detection
- ✅ Multilingual support
- ✅ Chrome Extension integration
- ✅ Warning notification system
- ✅ Optional automatic censorship
- ✅ LLM-based text classification
- ✅ User-friendly interface

---

## 🧠 AI Model

The project uses a multilingual **RoBERTa-based LLM** fine-tuned for:
- Sarcasm detection
- Toxic content analysis
- Cyberbullying detection
- Sentiment understanding

### Dataset
- Approximately **28000 manually labeled samples**
- Multilingual text data
- Social media comments and user messages

### Labels
- Normal
- Sarcastic

---

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### AI / NLP
- Python
- Hugging Face Transformers
- RoBERTa
- PyTorch
- Scikit-learn

### Browser Technologies
- Chrome Extension API

---

## ⚙️ How It Works

1. The user visits a website.
2. The Chrome extension scans visible text.
3. The text is sent to the AI model.
4. The RoBERTa-based model analyzes the content.
5. If harmful or sarcastic content is detected:
   - A warning is displayed
   - The content can be censored automatically


---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/project-name.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Load the Chrome Extension

- Open Chrome browser
- Go to:

```bash
chrome://extensions/
```

- Enable **Developer Mode**
- Click **Load unpacked**
- Select the `extension/` folder

---

## ▶️ Usage

- Activate the Chrome extension
- Open any website or social media platform
- The system automatically analyzes text content
- Harmful content triggers warnings or censorship

---

## 📊 Training Process

The model was trained using:
- Manual data labeling
- Text preprocessing techniques
- Fine-tuning methods
- Multilingual NLP datasets

---

## 🔒 Privacy

This project does not permanently store user data. Text analysis is performed only for harmful content detection purposes.

---

## 📈 Future Improvements

- Larger multilingual datasets
- Improved AI accuracy
- Mobile browser support
- User-customizable filtering
- Advanced LLM integration

---

## 👨‍💻 Developer

Computer Engineering Graduation Project

---

## 📜 License

This project was developed for educational and research purposes.


<img width="1280" height="236" alt="image" src="https://github.com/userattachments/assets/7667b5a3-81ce-4d42-88d0-9f3a62961867" />

<img width="1280" height="299" alt="image" src="https://github.com/userattachments/assets/12f74de3-0de6-466b-aa33-c1cc19526765" />
<img width="1280" height="371" alt="image" src="https://github.com/userattachments/assets/f62a2ce9-2767-42b2-87b4-4ae1926693b1" />

