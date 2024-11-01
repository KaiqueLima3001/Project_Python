from svc.classes.empresa import Empresa

class Produto:
    def __init__(self, id, nome, tipo, quantidade, empresa=Empresa):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade
        self.empresa = empresa
    