import tkinter as tk
from tkinter import messagebox
from .estoque import Estoque
from .produto import Produto
from .empresa import Empresa
from .bancodedados import BancoDeDados

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Estoque")
        self.root.geometry("800x600")  # Definindo tamanho da janela

        # Frame para o menu superior
        self.frame_menu = tk.Frame(root, bg="#2e4053", height=70)
        self.frame_menu.pack(fill=tk.X)

        # Cria um Canvas
        canvas = tk.Canvas(root, width=400, height=300)

        img = tk.PhotoImage(file=r"svc/img/logo.png")
        img = img.subsample(1, 3)

        # Mantém a referência da imagem
        canvas.image = img

        # Cria um label para exibir a imagem
        label_imagem = tk.Label(self.frame_menu, image=img, bg="#2e4053")
        label_imagem.place(x=40, y=5)

        # Configuração do menu
        self.create_menu_buttons()

        # Frame para a página inicial
        self.home_frame = tk.Frame(root, bg="#ecf0f1")
        self.create_home_page()

        # Frame para a página de estoque
        self.stock_frame = tk.Frame(root, bg="#ecf0f1")
        self.stock_frame.pack(fill=tk.BOTH, expand=True)
        
        self.create_stock_page()

        # Inicializa com a página de estoque
        self.show_frame(self.home_frame)

    def create_menu_buttons(self):
        # Adicionando um texto que se assemelha a um h2
        header_text = "Sistema de Estoque"
        header_label = tk.Label(self.frame_menu, text=header_text, font=("Times New Roman", 18, "bold", "italic"), fg="#f7dc6f", bg="#2e4053")
        header_label.place(x=260, y=20)

        # Adicionando botões
        button = tk.Button(self.frame_menu, text="Inicio", width=10, command=lambda: self.show_frame(self.home_frame))
        button.place(x=1000, y=25)

        button2 = tk.Button(self.frame_menu, text="Estoque", width=10, command=lambda: self.show_frame(self.stock_frame))
        button2.place(x=1100, y=25)

        button3 = tk.Button(self.frame_menu, text="Sobre", width=10)
        button3.place(x=1200, y=25)

    def create_home_page(self):
        try:
            # Carregar e exibir a imagem
            canvas2 = tk.Canvas(self.home_frame, width=400, height=300)
            home_img = tk.PhotoImage(file=r"svc/img/logo.png")
            label_imagem = tk.Label(self.home_frame, image=home_img)
            canvas2.image = home_img  # Mantém a referência da imagem
            label_imagem.pack(fill=tk.BOTH, expand=True)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")

        # Texto da página inicial
        label = tk.Label(self.home_frame, text="Página de Produtos", font=("Arial", 16, "bold"), fg="red")
        label.place(relx=0.5, rely=0.2, anchor='center')

        # Botão para ir ao estoque
        back_button = tk.Button(self.home_frame, text="Ir para o Estoque", command=lambda: self.show_frame(self.stock_frame))
        back_button.place(relx=0.5, rely=0.8, anchor='center')

    def show_stock_page(self):
        self.show_frame(self.stock_frame)

    def create_stock_page(self):
        # Frame para adicionar produtos
        self.form_frame = tk.Frame(self.stock_frame, bg="#ecf0f1")
        self.form_frame.pack(fill=tk.X, padx=80, pady=10)

        tk.Label(self.form_frame, text="Adicionar Produto", font=("Arial", 14, "bold"), fg="#212e3c", bg="#ecf0f1").grid(row=0, column=0, columnspan=2)

        # Campos do formulário dispostos horizontalmente
        tk.Label(self.form_frame, text="Nome:", fg="White", bg="#2f4052", width=12).grid(row=1, column=0, pady=15)
        self.nome_entry = tk.Entry(self.form_frame, width=20)
        self.nome_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Empresa:", fg="White", bg="#2f4052", width=12).grid(row=1, column=2)
        self.empresa_entry = tk.Entry(self.form_frame, width=20)
        self.empresa_entry.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(self.form_frame, text="Tipo:", fg="White", bg="#2f4052", width=12).grid(row=2, column=0)
        self.tipo_entry = tk.Entry(self.form_frame, width=20)
        self.tipo_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Quantidade:", fg="White", bg="#2f4052", width=12).grid(row=2, column=2)
        self.quantidade_entry = tk.Entry(self.form_frame, width=20)
        self.quantidade_entry.grid(row=2, column=3, padx=5, pady=5)

        tk.Button(self.form_frame, text="Adicionar", command=self.adicionar_produto).grid(row=0, column=1, columnspan=4, pady=10)

        # Frame para a lista de produtos com scrollbar
        self.product_list_frame = tk.Frame(self.stock_frame, bg="#ecf0f1")
        self.product_list_frame.pack(fill=tk.BOTH, expand=True)

        # Criar um canvas e scrollbar
        self.canvas = tk.Canvas(self.product_list_frame, bg="#ecf0f1")
        self.scrollbar = tk.Scrollbar(self.product_list_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#ecf0f1")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configurar scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Adicionando o cabeçalho da lista de produtos
        self.create_product_header()

        # Carregando a lista de produtos
        self.atualizar_produtos()

    def create_product_header(self):
        header_frame = tk.Frame(self.scrollable_frame, bg="#e1e1e2")
        header_frame.pack(fill=tk.X)

        tk.Label(header_frame, text="Produto", font=("Arial", 12), bg="#e1e1e2").grid(row=0, column=0, padx=100, pady=10)
        tk.Label(header_frame, text="Empresa", font=("Arial", 12), bg="#e1e1e2").grid(row=0, column=1, padx=100)
        tk.Label(header_frame, text="Tipo", font=("Arial", 12), bg="#e1e1e2").grid(row=0, column=2, padx=100)
        tk.Label(header_frame, text="Quantidade", font=("Arial", 12), bg="#e1e1e2").grid(row=0, column=3, padx=100)
        tk.Label(header_frame, text="Editar", font=("Arial", 12), bg="#e1e1e2").grid(row=0, column=4, padx=100)
        tk.Label(header_frame, text="Excluir", font=("Arial", 12), bg="#e1e1e2").grid(row=0, column=5, padx=100)

    def adicionar_produto(self):
        nome = self.nome_entry.get()
        empresa = self.empresa_entry.get()
        tipo = self.tipo_entry.get()
        quantidade = self.quantidade_entry.get()

        try:
            db = BancoDeDados('produtos.db')
            quantidade = int(quantidade)
            db.inserir_produto(nome, tipo, quantidade, empresa)
            self.atualizar_produtos()
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            self.limpar_campos()
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número!")

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.empresa_entry.delete(0, tk.END)
        self.tipo_entry.delete(0, tk.END)
        self.quantidade_entry.delete(0, tk.END)

    def atualizar_produtos(self):
        # Obtemos os produtos do Banco de dados!
        self.select_produtos()
        
        # Limpa a lista de produtos atual
        for widget in self.scrollable_frame.winfo_children():
            if widget != self.canvas:
                widget.destroy()

        # Recria o cabeçalho
        self.create_product_header()

        # Aqui Adicionamos os produtos
        cores = ["#F0F0F0", "#ececec"]
        for index, produto in enumerate(Estoque.produtos):
            cor_fundo = cores[index % len(cores)]
            frame_item = tk.Frame(self.scrollable_frame, bg=cor_fundo, padx=10, pady=5)
            frame_item.pack(fill=tk.X)

            tk.Label(frame_item, text=produto.nome, font=("Arial", 12), bg=cor_fundo).grid(row=0, column=0, padx=60, pady=5, sticky="ew")
            tk.Label(frame_item, text=produto.empresa, font=("Arial", 12), bg=cor_fundo).place(x=352, y=5)
            tk.Label(frame_item, text=produto.tipo, font=("Arial", 12), bg=cor_fundo).place(x=620, y=5)
            tk.Label(frame_item, text=produto.quantidade, font=("Arial", 12), bg=cor_fundo).place(x=861, y=5)

            tk.Button(frame_item, text="Editar", bg="#f5b7b1", command=lambda item=produto: self.editar_produto(item)).place(x=1150, y=5)
            tk.Button(frame_item, text="Excluir", bg="#f5b7b1", command=lambda id=produto.id: self.excluir_produto(id)).place(x=1395, y=5)

    def select_produtos(self):
        db = BancoDeDados('produtos.db')
        produtos = db.select_produtos()

        Estoque.produtos = []
        for n in produtos:
            produto = Produto(n[0],n[1],n[2],n[3],n[4])
            Estoque.addProduto(produto)

    def show_frame(self, frame):
        # Esconde todos os frames e mostra o frame desejado
        self.home_frame.pack_forget()
        self.stock_frame.pack_forget()
        frame.pack(fill=tk.BOTH, expand=True)

    def excluir_produto(self, produto_id):
        resposta = messagebox.askyesno("Confirmar Exclusão", "Você realmente deseja excluir?")
        if resposta:
            Estoque.excluir_produto(produto_id)
            self.atualizar_produtos()  # Atualiza a lista de produtos após a exclusão
            print("Item excluído.")
        else:
            print("Exclusão cancelada.")

    def editar_produto(self, produto):
        label_edit = tk.Toplevel(self.root)
        label_edit.title("Editar Produto")
        label_edit.geometry("300x200")

        tk.Label(label_edit, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
        nome_entry = tk.Entry(label_edit)
        nome_entry.insert(0, produto.nome)
        nome_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(label_edit, text="Tipo:").grid(row=1, column=0, padx=10, pady=10)
        tipo_entry = tk.Entry(label_edit)
        tipo_entry.insert(0, produto.tipo)
        tipo_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(label_edit, text="Quantidade:").grid(row=2, column=0, padx=10, pady=10)
        quantidade_entry = tk.Entry(label_edit)
        quantidade_entry.insert(0, produto.quantidade)
        quantidade_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(label_edit, text="Salvar", command=lambda item=produto: update_produto(produto)).grid(row=3, column=1, pady=20)

        def update_produto(produto):
            try:
                db = BancoDeDados('produtos.db')

                # Atualiza o produto no banco de dados e na lista
                produto.nome = nome_entry.get()
                produto.tipo = tipo_entry.get()
                produto.quantidade = int(quantidade_entry.get())

                db.update_produto(produto)

                # Atualiza a interface
                self.atualizar_produtos()

                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
                label_edit.destroy()

            except Exception:
                messagebox.showerror("Erro", "Erro ao atualizar o item!")

        