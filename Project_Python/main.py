import tkinter as tk
from svc.classes.estoque import Estoque
from svc.classes.empresa import Empresa
from svc.classes.produto import Produto
from svc.classes.bancodedados import BancoDeDados
from svc.classes.app import App

def main():
    root = tk.Tk()
    app = App(root)
    # Maximiza a janela
    root.state('zoomed')
    # Início do loop principal
    root.mainloop()
    

if __name__ == '__main__':
    main()