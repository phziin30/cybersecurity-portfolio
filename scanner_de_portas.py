import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"Porta {port} aberta!")
        else:
            print(f"Porta {port} fechada.")
        
        sock.close()
    except socket.error as err:
        print(f"Erro ao tentar conectar à {host}:{port} - {err}")

def main():
    host = input("Digite o IP ou domínio do alvo: ")
    start_port = int(input("Digite a porta inicial: "))
    end_port 
