import tkinter as tk
from svc.classes.estoque import Estoque
from svc.classes.empresa import Empresa
from svc.classes.produto import Produto
from svc.classes.bancodedados import BancoDeDados
from svc.classes.app import App

def main():
    Moleka = Empresa.addEmpresa("Moleka","313.845.744/0001-98") # Iniciamos a empresa "Moleka"

    db = BancoDeDados('produtos.db')
    produtos = db.select_produtos()
    for n in produtos:
        produto = Produto(n[0],n[1],n[2],n[3],Moleka)
        Estoque.addProduto(produto)

    root = tk.Tk()
    app = App(root)
    # Maximiza a janela
    root.state('zoomed')
    # Início do loop principal
    root.mainloop()
    

if __name__ == '__main__':
    main()