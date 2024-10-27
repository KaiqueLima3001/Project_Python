import tkinter as tk
from .estoque import Estoque

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Estoque")

        # Frame para o menu horizontal com altura fixa de 60 pixels
        frame_menu = tk.Frame(root, bg="#2e4053", height=70)
        frame_menu.pack(fill=tk.X)  # Preenche toda a largura da janela

        # Criação de um Frame para cada "página"
        self.home_frame = tk.Frame(self.root, bg="#ecf0f1")
        self.stock_frame = tk.Frame(self.root, bg="#ecf0f1")

        # Cria um Canvas
        canvas = tk.Canvas(root, width=400, height=300)
        # canvas.pack()

        img = tk.PhotoImage(file=r"svc/img/logo.png")
        img = img.subsample(1, 3)

        # Mantém a referência da imagem
        canvas.image = img

        # Cria um label para exibir a imagem
        label_imagem = tk.Label(frame_menu, image=img, bg="#2e4053")
        label_imagem.place(x=40)

        # Adicionando um texto que se assemelha a um h2
        header_text = "Sistema de Estoque"
        header_label = tk.Label(frame_menu, text=header_text, font=("Times New Roman", 18, "bold", "italic"), fg="#f7dc6f", bg="#2e4053")
        header_label.place(x=260, y=20)

        # Adicionando botões
        button = tk.Button(frame_menu, text="Inicio", width=10, command=lambda: self.show_frame(self.home_frame))
        button.place(x=1000, y=25)

        button2 = tk.Button(frame_menu, text="Estoque", width=10, command=lambda: self.show_frame(self.stock_frame))
        button2.place(x=1100, y=25)

        button3 = tk.Button(frame_menu, text="Sobre", width=10)
        button3.place(x=1200, y=25)

        # Adicionando conteúdo à página inicial
        self.create_home_page()

        # Adicionando conteúdo à página de produtos
        self.create_stock_page()

        # Exibindo a página inicial
        self.show_frame(self.home_frame)

    def create_home_page(self):
        label = tk.Label(self.home_frame, text="Página de Produtos", font=("Arial", 16, "bold"), bg="#6597ce")
        label.pack(pady=20)

        back_button = tk.Button(self.home_frame, text="Voltar para Início", command=lambda: self.show_frame(self.home_frame))
        back_button.pack(pady=10)

        self.home_frame.pack(fill=tk.BOTH, expand=True)

    def create_stock_page(self):
        tk.Label(self.stock_frame, text="Bem-vindo ao Sistema de Estoque!", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)

        global frame_topo
        frame_topo = tk.Frame(self.stock_frame, bg="#ecf0f1", height=90)
        frame_topo.pack(fill=tk.X)

        cabecalho = ["Produto", "Empresa", "Tipo", "Quantidade"]
        self.frame_produtos = self.frameProdutos(cabecalho)  # Salva o frame de produtos

        self.atualizar_produtos()

        self.stock_frame.pack(fill=tk.BOTH, expand=True)

    def show_frame(self, frame):
        self.home_frame.pack_forget()
        self.stock_frame.pack_forget()
        frame.pack(fill=tk.BOTH, expand=True)

    def frameProdutos(self, cabecalho):
        frame_produtos = tk.Frame(self.stock_frame, bg="yellow")
        frame_produtos.pack(fill=tk.X)

        # Criação do cabeçalho apenas uma vez
        frame_topo_produtos = tk.Frame(frame_produtos, bg="#e1e1e2", height=45)
        frame_topo_produtos.pack(fill=tk.X)

        x = 40
        for n in cabecalho:
            tk.Label(frame_topo_produtos, text=n, font=("Arial", 12, "italic"), bg="#e1e1e2").place(x=x, y=10)
            x += 300

        tk.Label(frame_topo_produtos, text="Editar", font=("Arial", 12, "italic"), bg="#e1e1e2").place(x=1160, y=10)
        tk.Label(frame_topo_produtos, text="Remover", font=("Arial", 12, "italic"), bg="#e1e1e2").place(x=1320, y=10)

        self.produtos_frame = tk.Frame(frame_produtos)  # Frame para os itens dos produtos
        self.produtos_frame.pack(fill=tk.X)

        return frame_produtos

    def atualizar_produtos(self):
        # Limpa produtos exibidos antes de adicionar novos
        for widget in self.produtos_frame.winfo_children():
            widget.destroy()

        qtd_produtos = len(Estoque.produtos)
        tk.Label(frame_topo, text="Produtos", font=("Arial", 16, "bold")).place(x=40)
        tk.Label(frame_topo, text=f"| {qtd_produtos} itens cadastrados", font=("Arial", 12)).place(x=150, y=3)
        entrada = tk.Entry(frame_topo, font=("Arial", 12), width=30).place(x=40, y=40)
        tk.Button(frame_topo, text="Pesquisar").place(x=320, y=38)

        # Adiciona os produtos
        cores = ["#F0F0F0", "#ececec"]
        for index, item in enumerate(Estoque.produtos):
            cor_fundo = cores[index % len(cores)]
            frame_item = tk.Frame(self.produtos_frame, height=45, bg=cor_fundo)
            frame_item.pack(fill=tk.X)

            tk.Label(frame_item, text=item.nome, font=("Arial", 12), bg=cor_fundo).place(x=40, y=10)
            tk.Label(frame_item, text=item.empresa.nome, font=("Arial", 12), bg=cor_fundo).place(x=340, y=10)
            tk.Label(frame_item, text=item.tipo, font=("Arial", 12), bg=cor_fundo).place(x=640, y=10)
            tk.Label(frame_item, text=item.quantidade, font=("Arial", 12), bg=cor_fundo).place(x=960, y=10)

            # Adicionando a lógica de exclusão
            btn_excluir = tk.Button(frame_item, text="Excluir", bg="#f5b7b1", command=lambda id=item.id: self.excluir_produto(id))
            btn_excluir.place(x=1320, y=10)

    def excluir_produto(self, produto_id):
        Estoque.excluir_produto(produto_id)
        self.atualizar_produtos()  # Atualiza a lista de produtos após a exclusão