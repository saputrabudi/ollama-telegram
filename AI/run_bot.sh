#!/bin/bash

echo "🚀 Memulai Chatbot AI Telegram..."
echo "================================="

# Mengaktifkan virtual environment
echo "📦 Mengaktifkan virtual environment..."
source telegram_bot_env/bin/activate

# Memeriksa apakah Ollama berjalan
echo "🔍 Memeriksa status Ollama..."
if ! curl -s http://localhost:11434/api/tags > /dev/null; then
    echo "❌ Ollama tidak berjalan. Memulai Ollama..."
    ollama serve &
    sleep 5
fi

# Menjalankan bot
echo "🤖 Menjalankan Chatbot..."
python3 telegram_bot.py

echo "🛑 Bot telah dihentikan." 