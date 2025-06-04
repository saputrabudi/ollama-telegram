#!/usr/bin/env python3
"""
Chatbot AI Telegram dengan integrasi Ollama
Model: saputrabudi/exabot-micro
"""

import asyncio
import logging
import requests
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Konfigurasi
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "saputrabudi/exabot-micro:latest"

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class OllamaBot:
    def __init__(self):
        self.conversation_history = {}

    def get_ollama_response(self, prompt: str, user_id: int) -> str:
        """Mendapatkan response dari Ollama AI"""
        try:
            # Membuat context percakapan
            if user_id not in self.conversation_history:
                self.conversation_history[user_id] = []
            
            # Menambahkan pesan user ke history
            self.conversation_history[user_id].append(f"User: {prompt}")
            
            # Membatasi history agar tidak terlalu panjang
            if len(self.conversation_history[user_id]) > 10:
                self.conversation_history[user_id] = self.conversation_history[user_id][-10:]
            
            # Membuat context dari history
            context = "\n".join(self.conversation_history[user_id])
            
            payload = {
                "model": OLLAMA_MODEL,
                "prompt": f"{context}\nAssistant:",
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "max_tokens": 500
                }
            }
            
            response = requests.post(OLLAMA_URL, json=payload, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                ai_response = result.get('response', 'Maaf, saya tidak dapat memproses permintaan Anda.')
                
                # Menambahkan response AI ke history
                self.conversation_history[user_id].append(f"Assistant: {ai_response}")
                
                return ai_response
            else:
                logger.error(f"Ollama API error: {response.status_code} - {response.text}")
                return "Maaf, terjadi kesalahan saat berkomunikasi dengan AI."
                
        except requests.exceptions.Timeout:
            logger.error("Timeout saat menghubungi Ollama")
            return "Maaf, response memakan waktu terlalu lama. Silakan coba lagi."
        except Exception as e:
            logger.error(f"Error dalam get_ollama_response: {str(e)}")
            return "Maaf, terjadi kesalahan internal. Silakan coba lagi nanti."

    def clear_history(self, user_id: int):
        """Menghapus history percakapan user"""
        if user_id in self.conversation_history:
            del self.conversation_history[user_id]

# Inisialisasi bot
ollama_bot = OllamaBot()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler untuk command /start"""
    welcome_message = """
🤖 **Selamat datang di Chatbot AI!**

Saya adalah asisten AI yang ditenagai oleh model **saputrabudi/exabot-micro** melalui Ollama.

**Perintah yang tersedia:**
- Kirim pesan apa saja untuk berbicara dengan AI
- /start - Menampilkan pesan selamat datang
- /help - Menampilkan bantuan
- /clear - Menghapus riwayat percakapan
- /info - Informasi tentang bot

Silakan mulai berbicara dengan saya! 💬
    """
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler untuk command /help"""
    help_text = """
🆘 **Bantuan Chatbot AI**

**Cara menggunakan:**
1. Kirim pesan teks biasa untuk berbicara dengan AI
2. AI akan merespon berdasarkan konteks percakapan
3. Gunakan /clear untuk memulai percakapan baru

**Contoh penggunaan:**
- "Halo, siapa kamu?"
- "Jelaskan tentang kecerdasan buatan"
- "Buatkan saya resep nasi goreng"
- "Ceritakan lelucon yang lucu"

**Tips:**
- Berbicaralah dengan natural seperti kepada manusia
- AI akan mengingat konteks percakapan sebelumnya
- Jika response lambat, tunggu sebentar karena AI sedang berpikir

**Model AI:** saputrabudi/exabot-micro
**Optimized for:** Bahasa Indonesia

Selamat mengobrol! 🎉
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler untuk command /clear"""
    user_id = update.effective_user.id
    ollama_bot.clear_history(user_id)
    await update.message.reply_text("✅ Riwayat percakapan telah dihapus. Mari mulai percakapan baru!")

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler untuk command /info"""
    info_text = """
ℹ️ **Informasi Bot**

**Model AI:** saputrabudi/exabot-micro
**Platform:** Ollama
**Framework:** Python Telegram Bot
**Versi:** 1.0

**Tentang Model:**
- 🇮🇩 Optimized untuk Bahasa Indonesia
- ⚡ Response time cepat (~1.3GB)
- 🎯 Fine-tuned untuk conversational AI
- 💬 Natural conversation style

**Fitur:**
- ✅ Percakapan natural dengan AI
- ✅ Memory konteks percakapan
- ✅ Respons dalam Bahasa Indonesia
- ✅ Response time yang optimal
- ✅ Multi-user support

**Dikembangkan dengan ❤️ menggunakan:**
- Python 3.11
- python-telegram-bot
- Ollama API
- saputrabudi/exabot-micro Model

Bot ini berjalan 24/7 untuk melayani Anda!
    """
    await update.message.reply_text(info_text, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler untuk pesan teks dari user"""
    user_id = update.effective_user.id
    user_name = update.effective_user.first_name or "User"
    user_message = update.message.text
    
    logger.info(f"Pesan dari {user_name} (ID: {user_id}): {user_message}")
    
    # Mengirim typing indicator
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    
    try:
        # Mendapatkan response dari Ollama
        ai_response = ollama_bot.get_ollama_response(user_message, user_id)
        
        # Mengirim response ke user
        await update.message.reply_text(ai_response)
        
        logger.info(f"Response dikirim ke {user_name}")
        
    except Exception as e:
        logger.error(f"Error dalam handle_message: {str(e)}")
        await update.message.reply_text(
            "Maaf, terjadi kesalahan saat memproses pesan Anda. Silakan coba lagi."
        )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler untuk error"""
    logger.error(f"Update {update} menyebabkan error {context.error}")

def check_ollama_connection():
    """Memeriksa koneksi ke Ollama"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            model_names = [model['name'] for model in models]
            
            if OLLAMA_MODEL in model_names:
                print(f"✅ Ollama terhubung. Model {OLLAMA_MODEL} tersedia.")
                return True
            else:
                print(f"❌ Model {OLLAMA_MODEL} tidak ditemukan.")
                print(f"💡 Untuk menginstall model: ollama run saputrabudi/exabot-micro")
                print(f"Model yang tersedia: {', '.join(model_names)}")
                return False
        else:
            print(f"❌ Ollama API error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Tidak dapat terhubung ke Ollama: {str(e)}")
        return False

def main() -> None:
    """Fungsi utama untuk menjalankan bot"""
    print("🚀 Memulai Chatbot AI Telegram...")
    print("Model: saputrabudi/exabot-micro")
    print("=" * 40)
    
    # Memeriksa koneksi Ollama
    if not check_ollama_connection():
        print("❌ Gagal terhubung ke Ollama.")
        print("💡 Pastikan Ollama berjalan dan model saputrabudi/exabot-micro tersedia.")
        print("🔧 Jalankan: ollama run saputrabudi/exabot-micro")
        return
    
    # Membuat aplikasi bot
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Menambahkan handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("clear", clear_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Menambahkan error handler
    application.add_error_handler(error_handler)
    
    print("✅ Bot siap berjalan!")
    print("📱 Anda bisa mulai menggunakan bot di Telegram")
    print("🛑 Tekan Ctrl+C untuk menghentikan bot")
    
    # Menjalankan bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main() 
