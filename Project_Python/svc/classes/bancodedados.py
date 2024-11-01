import sqlite3

class BancoDeDados:
    def __init__(self, nome_banco):
        self.conn = sqlite3.connect(nome_banco)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                empresa TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def inserir_produto(self, nome, tipo, quantidade, empresa):
        self.cursor.execute('''
            INSERT INTO produtos (nome, tipo, quantidade, empresa)
            VALUES (?, ?, ?, ?)
        ''', (nome, tipo, quantidade, empresa))
        self.conn.commit()

    def select_produtos(self):
        self.cursor.execute('SELECT * FROM produtos')
        return self.cursor.fetchall()
    
    def delete_produtos(self):
        self.cursor.execute('DELETE FROM produtos')
        self.conn.commit()

    def update_produto(self, produto):
        # Atualiza no banco de dados
        db = BancoDeDados('produtos.db')
        db.cursor.execute('UPDATE produtos SET nome = ?, tipo = ?, quantidade = ? WHERE id = ?', (produto.nome, produto.tipo, produto.quantidade, produto.id))
        db.conn.commit()

    def fechar_conexao(self):
        self.conn.close()

# Dar carga de produtos no Banco de dados!
if __name__ == "__main__":
    db = BancoDeDados('produtos.db')

    # db.delete_produtos()

    # # Inserindo produtos
    db.inserir_produto("Picolé de Morango", "Picolé", 1400, "Moleka")
    db.inserir_produto("Sorvete de Flocos", "Sorvete", 889, "Moleka")
    db.inserir_produto("Picolé de Baunilha", "Picolé", 223, "Moleka")
    db.inserir_produto("Picolé de Flocos", "Picolé", 345, "Moleka")
    
    db.inserir_produto("Picolé de Chocolate", "Picolé", 908, "Moleka")
    db.inserir_produto("Sorvete de Napolitano", "Sorvete", 381, "Moleka")
    db.inserir_produto("Sorvete de Baunilha", "Sorvete", 15, "Moleka")
    db.inserir_produto("Sorvete de Framboesa", "Sorvete", 74, "Moleka")

    # Buscando produtos
    produtos = db.select_produtos()
    for produto in produtos:
        print(produto)

    # Fechando a conexão
    db.fechar_conexao()
