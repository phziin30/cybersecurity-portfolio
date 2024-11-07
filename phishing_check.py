import re

# Função para verificar se a URL tem características de phishing
def check_phishing(url):
    # Lista de palavras-chave que são frequentemente usadas em URLs de phishing
    phishing_keywords = ['secure', 'verify', 'login', 'account', 'update', 'support']

    # Verificando se a URL contém qualquer uma das palavras-chave suspeitas
    for word in phishing_keywords:
        if word in url.lower():
            return True
    return False

# Testando a função
url = input("Enter the URL to check: ")
if check_phishing(url):
    print("Warning: This URL may be a phishing attempt.")
else:
    print("This URL appears to be safe.")
