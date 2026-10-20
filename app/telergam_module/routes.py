from flask import Blueprint, render_template

from telethon import TelegramClient


telegram_module_bp = Blueprint('tg', __name__)

@telegram_module_bp.route('/settings')
def settings():
    return render_template('telegram_module/settings.html')