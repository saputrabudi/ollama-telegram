#!/usr/bin/env python3
"""
Script untuk memvalidasi setup virtual environment dan dependencies
"""

import sys
import os
import subprocess

def check_virtual_env():
    """Cek apakah virtual environment aktif"""
    venv_path = os.environ.get('VIRTUAL_ENV')
    if venv_path:
        print(f"✅ Virtual environment aktif: {venv_path}")
        return True
    else:
        print("❌ Virtual environment tidak aktif")
        print("💡 Jalankan: source telegram_bot_env/bin/activate")
        return False

def check_python_version():
    """Cek versi Python"""
    version = sys.version_info
    print(f"🐍 Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 11:
        print("✅ Python version compatible")
        return True
    else:
        print("❌ Python version tidak compatible (perlu 3.11+)")
        return False

def check_dependencies():
    """Cek dependencies yang diperlukan"""
    dependencies = [
        "telegram",
        "requests"
    ]
    
    all_ok = True
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✅ {dep} tersedia")
        except ImportError:
            print(f"❌ {dep} tidak tersedia")
            all_ok = False
    
    return all_ok

def check_ollama_connection():
    """Cek koneksi ke Ollama"""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            print(f"✅ Ollama terhubung ({len(models)} model tersedia)")
            
            # Cek model saputrabudi/exabot-micro
            model_names = [model['name'] for model in models]
            if "saputrabudi/exabot-micro:latest" in model_names:
                print("✅ Model saputrabudi/exabot-micro tersedia")
                return True
            else:
                print("❌ Model saputrabudi/exabot-micro tidak ditemukan")
                print("💡 Jalankan: ollama run saputrabudi/exabot-micro")
                return False
        else:
            print(f"❌ Ollama error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Gagal terhubung ke Ollama: {str(e)}")
        return False

def check_files():
    """Cek file-file yang diperlukan"""
    required_files = [
        "telegram_bot.py",
        "config.py",
        "requirements.txt",
        "run_bot.sh",
        "README.md"
    ]
    
    all_ok = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} tersedia")
        else:
            print(f"❌ {file} tidak ditemukan")
            all_ok = False
    
    return all_ok

def main():
    """Fungsi utama validasi"""
    print("🔍 VALIDASI SETUP CHATBOT AI")
    print("Model: saputrabudi/exabot-micro")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version),
        ("Virtual Environment", check_virtual_env),
        ("Dependencies", check_dependencies),
        ("Required Files", check_files),
        ("Ollama Connection", check_ollama_connection)
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n📋 Mengecek {name}...")
        result = check_func()
        results.append((name, result))
    
    print("\n" + "=" * 50)
    print("📊 HASIL VALIDASI")
    print("=" * 50)
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name:20} : {status}")
        if not result:
            all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("🎉 SEMUA VALIDASI BERHASIL!")
        print("🚀 Bot siap dijalankan!")
        print("\n💡 Untuk menjalankan bot:")
        print("   python3 telegram_bot.py")
        print("   atau")
        print("   ./run_bot.sh")
    else:
        print("⚠️  ADA MASALAH YANG PERLU DIPERBAIKI!")
        print("\n🔧 Solusi:")
        print("1. Pastikan virtual environment aktif")
        print("2. Install dependencies: pip install -r requirements.txt")
        print("3. Setup Ollama: ollama run saputrabudi/exabot-micro")
        print("4. Cek koneksi internet")

if __name__ == '__main__':
    main() 