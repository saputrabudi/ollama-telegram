# 🤖 Chatbot AI Telegram dengan Ollama

Aplikasi chatbot AI yang terintegrasi dengan Telegram Bot API dan Ollama model **saputrabudi/exabot-micro**.

## 📋 Fitur

- ✅ **Percakapan Natural**: Berkomunikasi dengan AI secara natural dalam Bahasa Indonesia
- ✅ **Memory Konteks**: AI mengingat percakapan sebelumnya untuk konteks yang lebih baik
- ✅ **Multi-User Support**: Mendukung banyak pengguna dengan riwayat terpisah
- ✅ **Command System**: Berbagai perintah untuk mengontrol bot
- ✅ **Error Handling**: Penanganan error yang robust
- ✅ **Logging System**: Sistem logging lengkap untuk monitoring

## 🚀 Instalasi

### Prerequisites

1. **Python 3.11+** sudah terinstal
2. **pip3** sudah terinstal
3. **python3-venv** untuk membuat virtual environment
4. **Ollama** sudah terinstal dan berjalan
5. **Model saputrabudi/exabot-micro** sudah di-clone dari Ollama Hub
6. **Token Telegram Bot** (sudah dikonfigurasi)

### Langkah Instalasi

1. **Clone atau unduh project ini**
   ```bash
   cd /root/AI
   ```

2. **Install python3-venv jika belum ada**
   ```bash
   apt update
   apt install python3.11-venv -y
   ```

3. **Buat Virtual Environment**
   ```bash
   python3 -m venv telegram_bot_env
   ```
   
   > Virtual environment akan dibuat di direktori `telegram_bot_env/`

4. **Aktifkan Virtual Environment**
   ```bash
   source telegram_bot_env/bin/activate
   ```
   
   > Setelah aktif, prompt akan menunjukkan `(telegram_bot_env)`

5. **Install Dependencies Python**
   ```bash
   pip install python-telegram-bot requests
   ```
   
   > Atau gunakan requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

6. **Clone Model AI dari Ollama Hub**
   ```bash
   ollama run saputrabudi/exabot-micro
   ```
   
   > Model ini akan otomatis diunduh dan tersedia sebagai `saputrabudi/exabot-micro:latest`

7. **Validasi Setup (Opsional)**
   ```bash
   python3 validate_setup.py
   ```
   
   > Script ini akan memvalidasi semua komponen sudah terinstall dengan benar

## 🧠 Model AI

Bot ini menggunakan **saputrabudi/exabot-micro**, sebuah model AI yang dioptimalkan untuk:
- 🇮🇩 **Bahasa Indonesia** - Respons natural dalam bahasa Indonesia
- ⚡ **Performa Cepat** - Model ringan dengan response time optimal
- 🎯 **Konteks Akurat** - Memahami konteks percakapan dengan baik
- 💬 **Conversational** - Gaya percakapan yang ramah dan informatif

### Clone Model:
```bash
# Clone model dari Ollama Hub
ollama run saputrabudi/exabot-micro

# Atau pull manual
ollama pull saputrabudi/exabot-micro

# Cek model tersedia
ollama list
```

## 🎯 Cara Menjalankan

### Metode 1: Menggunakan Script
```bash
./run_bot.sh
```

### Metode 2: Manual
```bash
# Aktifkan virtual environment
source telegram_bot_env/bin/activate

# Pastikan Ollama berjalan
ollama serve

# Jalankan bot
python3 telegram_bot.py
```

### Metode 3: Sebagai Service
```bash
# Install service
./manage_service.sh install

# Start service
./manage_service.sh start

# Cek status
./manage_service.sh status
```

## 🔧 Konfigurasi

Edit file `config.py` untuk menyesuaikan pengaturan:

```python
# Telegram Bot Token
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"

# Ollama Settings - Model saputrabudi/exabot-micro
OLLAMA_MODEL = "saputrabudi/exabot-micro:latest"
OLLAMA_URL = "http://localhost:11434/api/generate"

# AI Parameters
AI_TEMPERATURE = 0.7
AI_TOP_P = 0.9
AI_MAX_TOKENS = 500
```

## 📱 Perintah Bot

| Perintah | Deskripsi |
|----------|-----------|
| `/start` | Menampilkan pesan selamat datang |
| `/help` | Menampilkan bantuan lengkap |
| `/clear` | Menghapus riwayat percakapan |
| `/info` | Informasi tentang bot dan model AI |

## 💬 Cara Menggunakan

1. **Mulai percakapan** dengan mengirim `/start` ke bot
2. **Kirim pesan** apa saja untuk berbicara dengan AI
3. **AI akan merespon** berdasarkan konteks percakapan
4. **Gunakan `/clear`** untuk memulai percakapan baru

## 🏗️ Struktur Project

```
AI/
├── telegram_bot.py      # File utama bot
├── config.py           # Konfigurasi
├── requirements.txt    # Dependencies
├── run_bot.sh         # Script untuk menjalankan bot
├── manage_service.sh  # Script untuk mengelola service
├── telegram_bot.service # File systemd service
├── validate_setup.py  # Script validasi setup
├── README.md          # Dokumentasi
└── telegram_bot_env/  # Virtual environment (dibuat saat instalasi)
    ├── bin/           # Executable files
    ├── lib/           # Python packages
    └── ...
```

## 🔍 Monitoring

Bot dilengkapi dengan sistem logging yang mencatat:
- Pesan masuk dari pengguna
- Respons yang dikirim
- Error yang terjadi
- Status koneksi Ollama

## ⚠️ Troubleshooting

### Virtual Environment Issues
```bash
# Hapus virtual environment lama
rm -rf telegram_bot_env

# Buat ulang virtual environment
python3 -m venv telegram_bot_env

# Aktifkan
source telegram_bot_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Validasi Setup
```bash
# Jalankan script validasi
source telegram_bot_env/bin/activate
python3 validate_setup.py
```

### Bot tidak merespon
1. Pastikan virtual environment aktif: `source telegram_bot_env/bin/activate`
2. Pastikan Ollama berjalan: `ollama serve`
3. Cek model tersedia: `ollama list`
4. Cek koneksi internet untuk Telegram API

### Error "Model not found"
1. Clone model: `ollama run saputrabudi/exabot-micro`
2. Atau pull manual: `ollama pull saputrabudi/exabot-micro`
3. Cek nama model di `ollama list`
4. Update `OLLAMA_MODEL` di config.py jika diperlukan

### Memory habis
1. Restart Ollama: `pkill ollama && ollama serve`
2. Gunakan `/clear` untuk menghapus riwayat
3. Kurangi `MAX_CONVERSATION_HISTORY` di config.py

### Permission Error
```bash
# Berikan permission pada script
chmod +x run_bot.sh
chmod +x manage_service.sh
chmod +x validate_setup.py
```

## 🛠️ Development

### Setup Development Environment
```bash
# Clone project
cd /root/AI

# Buat virtual environment
python3 -m venv telegram_bot_env

# Aktifkan virtual environment
source telegram_bot_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup model
ollama run saputrabudi/exabot-micro

# Validasi setup
python3 validate_setup.py
```

### Menambah Fitur Baru
1. Edit `telegram_bot.py`
2. Tambahkan handler baru
3. Update dokumentasi

### Testing
```bash
# Aktifkan virtual environment
source telegram_bot_env/bin/activate

# Validasi setup lengkap
python3 validate_setup.py

# Test koneksi Ollama
curl http://localhost:11434/api/tags

# Test model saputrabudi/exabot-micro
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "saputrabudi/exabot-micro:latest", "prompt": "Halo"}'
```

## 📋 Model Information

**saputrabudi/exabot-micro** adalah model AI yang:
- 📥 **Dikembangkan khusus** untuk bahasa Indonesia
- 🚀 **Optimal untuk chatbot** dengan response cepat
- 💾 **Ukuran efficient** (~1.3GB) untuk deployment
- 🎯 **Fine-tuned** untuk conversational AI

### Cara mendapatkan model:
```bash
# Metode 1: Run langsung (otomatis download)
ollama run saputrabudi/exabot-micro

# Metode 2: Pull manual
ollama pull saputrabudi/exabot-micro

# Cek model tersedia
ollama list
```

## 🚀 Quick Start

Untuk pengguna baru, ikuti langkah cepat ini:

```bash
# 1. Masuk ke direktori
cd /root/AI

# 2. Buat virtual environment
python3 -m venv telegram_bot_env

# 3. Aktifkan virtual environment
source telegram_bot_env/bin/activate

# 4. Install dependencies
pip install python-telegram-bot requests

# 5. Download model AI
ollama run saputrabudi/exabot-micro

# 6. Validasi setup
python3 validate_setup.py

# 7. Jalankan bot
python3 telegram_bot.py
```

## 📄 Lisensi

Project ini dibuat untuk pembelajaran dan pengembangan chatbot AI dengan model saputrabudi/exabot-micro.

## 🤝 Kontribusi

Silakan berkontribusi dengan:
1. Melaporkan bug
2. Menambah fitur baru
3. Memperbaiki dokumentasi
4. Testing dengan model AI lain

## 📞 Support

Jika ada masalah, silakan:
1. Jalankan script validasi: `python3 validate_setup.py`
2. Cek log untuk error details
3. Pastikan model `saputrabudi/exabot-micro` sudah ter-download
4. Pastikan virtual environment `telegram_bot_env` sudah dibuat dan aktif
5. Verifikasi konfigurasi Ollama dan Telegram

---

**Selamat menggunakan Chatbot AI dengan saputrabudi/exabot-micro! 🎉** 