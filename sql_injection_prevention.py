import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Criar tabela de usuários
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')

# Função para adicionar usuário de forma segura
def add_user(username, password):
    # Usando parâmetros para evitar SQL Injection
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

# Função para buscar usuário
def get_user(username):
    # Usando parâmetros para evitar SQL Injection
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    return c.fetchone()

# Testando
add_user('admin', 'securepassword123')
user = get_user('admin')
print(user)

conn.close()
