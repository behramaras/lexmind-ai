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

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
