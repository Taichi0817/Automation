# src/telnet_client.py
import telnetlib
import time
from my_logger import get_logger
import yaml

with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

host = config['telnet']['host']
port = config['telnet']['port']
username = config['telnet']['username']
password = config['telnet']['password']

# ロガーの取得
logger = get_logger()


def connect_telnet():
    try:
        tn = telnetlib.Telnet(host, port)
        tn.write(b"\n")
        time.sleep(1)
        output = tn.read_very_eager().decode('utf-8')
        if "~ #" in output: # for developer telnet
            logger.info(f"[Telnet] For Developer Connect Success: {host}:{port}")
            tn.write(b"telnet localhost\n")
            time.sleep(1)
            tn.read_until(b"login: ", timeout=5)
            tn.write(username.encode('ascii') + b"\n")
            tn.read_until(b"Password: ", timeout=5)
            tn.write(password.encode('ascii') + b"\n")
            time.sleep(1)
            output = tn.read_very_eager().decode('utf-8')
            if "Welcome to BUFFALO CLI !" in output:
                logger.info("[Telnet] Login Success")
                tn.write(b"terminal pager enable\n")
                tn.write(b"show status all\n")
                time.sleep(5)
                output = tn.read_very_eager().decode('utf-8')
                logger.info(f"Command Output: {output}")
            if "Connection closed by foreign host" in output:
                logger.info("[Telnet] Connection closed by foreign host")
        tn.write(b"exit\n")
        tn.close()
        
        logger.info("[Telnet]End of session")
    
    except Exception as e:
        logger.error(f"[Telnet]Error during connection: {e}")

if __name__ == "__main__":
    connect_telnet()