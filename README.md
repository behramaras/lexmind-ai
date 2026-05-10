LexMind is a Turkish legal information assistant powered by local AI models via Ollama. It allows users to ask questions about Turkish law and receive clear, informative answers — all running locally without sending data to external servers.

> **Disclaimer:** LexMind provides general legal information only. It is not a substitute for professional legal advice.

---

## Features

- Topic-based legal assistance (Labor, Family, Criminal, Rental, Consumer, Inheritance Law)
- User authentication (register, login, logout)
- Chat history with accordion view
- KVKK-compliant personal data masking (TC ID, phone, email, license plate, IBAN)
- Markdown rendering for AI responses
- Dark/light sidebar with topic switching
- Fully local — no data sent to external AI services

---

## Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Login
- **Database:** SQLite
- **AI:** Ollama (gemma3:4b)
- **Frontend:** HTML, CSS, JavaScript

---

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed and running
- `gemma3:4b` model pulled

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/lexmind-ai.git
cd lexmind-ai
```

**2. Install dependencies**
```bash
pip3 install -r requirements.txt
```

**3. Pull the AI model**
```bash
ollama pull gemma3:4b
```

**4. Start Ollama**
```bash
ollama serve
```

**5. Run the app**
```bash
python3 run.py
```

**6. Open in browser**
```
http://localhost:5500
```

---

## Project Structure

```
lexmind-ai/
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── routes.py          # URL routes and logic
│   ├── models.py          # Database models
│   ├── masking.py         # KVKK personal data masking
│   ├── static/
│   │   └── favicon.svg
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       ├── chat.html
│       └── history.html
├── run.py
├── requirements.txt
└── README.md
```

---

## Screenshots

> Coming soon
---

## License

MIT License
```
