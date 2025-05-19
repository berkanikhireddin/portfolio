import time
import socket
from datetime import datetime

def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

def log_disconnection():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(f"❌ Connexion perdue à {now}\n")

def main():
    print("📡 Surveillance de la connexion Internet en cours...")
    while True:
        if not check_internet():
            print("❌ Pas de connexion Internet!")
            log_disconnection()
        else:
            print("✅ Connexion OK.")
        time.sleep(10)

if __name__ == "__main__":
    main()
