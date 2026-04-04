from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User, Chat
import requests

main = Blueprint("main", __name__)

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "gemma3:4b"
SYSTEM_PROMPT = """Sen LexMind'ın hukuki asistanısın. Yalnızca Türk hukuku hakkında sorulara cevap veriyorsun. 
Cevapların açık, anlaşılır ve Türkçe olmalı. Her cevabın sonunda hukuki tavsiye vermediğini, 
yalnızca bilgi sunduğunu belirt."""

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if User.query.filter_by(username=username).first():
            return render_template("register.html", error="Bu kullanıcı adı zaten alınmış.")
        
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.login"))
    
    return render_template("register.html")

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("main.chat"))
        
        return render_template("login.html", error="Kullanıcı adı veya şifre hatalı.")
    
    return render_template("login.html")

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@main.route("/chat", methods=["GET", "POST"])
@login_required
def chat():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")
        
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question}
            ],
            "stream": False
        })
        
        answer = response.json()["message"]["content"]
        
        chat = Chat(user_id=current_user.id, question=question, answer=answer)
        db.session.add(chat)
        db.session.commit()
    
    return render_template("chat.html", answer=answer)

@main.route("/history")
@login_required
def history():
    chats = Chat.query.filter_by(user_id=current_user.id).order_by(Chat.created_at.desc()).all()
    return render_template("history.html", chats=chats)
