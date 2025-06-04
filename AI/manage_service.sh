#!/bin/bash

SERVICE_NAME="telegram_bot"
SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"
CURRENT_DIR=$(pwd)

case "$1" in
    install)
        echo "📦 Menginstal service ${SERVICE_NAME}..."
        sudo cp telegram_bot.service $SERVICE_FILE
        sudo systemctl daemon-reload
        sudo systemctl enable $SERVICE_NAME
        echo "✅ Service berhasil diinstal!"
        echo "💡 Gunakan: sudo systemctl start $SERVICE_NAME"
        ;;
    start)
        echo "▶️  Memulai service ${SERVICE_NAME}..."
        sudo systemctl start $SERVICE_NAME
        echo "✅ Service dimulai!"
        ;;
    stop)
        echo "⏹️  Menghentikan service ${SERVICE_NAME}..."
        sudo systemctl stop $SERVICE_NAME
        echo "✅ Service dihentikan!"
        ;;
    restart)
        echo "🔄 Merestart service ${SERVICE_NAME}..."
        sudo systemctl restart $SERVICE_NAME
        echo "✅ Service direstart!"
        ;;
    status)
        echo "📊 Status service ${SERVICE_NAME}:"
        sudo systemctl status $SERVICE_NAME
        ;;
    logs)
        echo "📄 Log service ${SERVICE_NAME}:"
        sudo journalctl -u $SERVICE_NAME -f
        ;;
    uninstall)
        echo "🗑️  Menghapus service ${SERVICE_NAME}..."
        sudo systemctl stop $SERVICE_NAME
        sudo systemctl disable $SERVICE_NAME
        sudo rm -f $SERVICE_FILE
        sudo systemctl daemon-reload
        echo "✅ Service berhasil dihapus!"
        ;;
    *)
        echo "🤖 Telegram Bot Service Manager"
        echo "================================"
        echo "Penggunaan: $0 {install|start|stop|restart|status|logs|uninstall}"
        echo ""
        echo "Perintah:"
        echo "  install   - Instal service"
        echo "  start     - Mulai service"
        echo "  stop      - Hentikan service"
        echo "  restart   - Restart service"
        echo "  status    - Cek status service"
        echo "  logs      - Lihat log service"
        echo "  uninstall - Hapus service"
        exit 1
        ;;
esac 