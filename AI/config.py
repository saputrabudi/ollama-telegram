"""
Konfigurasi untuk Chatbot AI Telegram
Model: saputrabudi/exabot-micro
"""

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Ollama Configuration - Model saputrabudi/exabot-micro
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "saputrabudi/exabot-micro:latest"
OLLAMA_TAGS_URL = "http://localhost:11434/api/tags"

# Bot Settings
MAX_CONVERSATION_HISTORY = 10
AI_TEMPERATURE = 0.7
AI_TOP_P = 0.9
AI_MAX_TOKENS = 500
REQUEST_TIMEOUT = 60

# Logging Configuration
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'INFO' 
