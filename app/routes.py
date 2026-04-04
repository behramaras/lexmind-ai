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


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
