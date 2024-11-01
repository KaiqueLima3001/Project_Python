from .bancodedados import BancoDeDados

class Estoque:
    # Supondo que você tenha um método para buscar produtos
    produtos = []

    @classmethod
    def addProduto(cls,produto):
        cls.produtos.append(produto)

    @classmethod
    def getProdutos(cls):
        return cls.produtos
    
    @staticmethod
    def inserir_produto(nome,tipo,quantidade,empresa):
        db = BancoDeDados('produtos.db')
        db.cursor.execute('''
            INSERT INTO produtos (nome, tipo, quantidade, empresa)
            VALUES (?, ?, ?, ?)
        ''', (nome, tipo, quantidade, empresa))
        db.conn.commit()
        db.fechar_conexao()
        # Atualize a lista de produtos após a exclusão
        Estoque.produtos = [p for p in Estoque.produtos]

    @staticmethod
    def excluir_produto(produto_id):
        # Implemente a lógica para excluir o produto do banco de dados
        # Exemplo:
        db = BancoDeDados('produtos.db')
        db.cursor.execute('DELETE FROM produtos WHERE id = ?', (produto_id,))
        db.conn.commit()
        db.fechar_conexao()
        # Atualize a lista de produtos após a exclusão
        Estoque.produtos = [p for p in Estoque.produtos if p.id != produto_id]
