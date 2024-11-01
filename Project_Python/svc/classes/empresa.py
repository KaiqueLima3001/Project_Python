class Empresa:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
    
    @classmethod
    def addEmpresa(cls,nome,cnpj):
        return cls(nome,cnpj)