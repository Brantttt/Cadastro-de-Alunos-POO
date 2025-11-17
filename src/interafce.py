import tkinter as tk
 
def criar_janela_principal():

    # Janela principal

    janela = tk.Tk()

    janela.title("Sistema de Cadastro de Alunos - TechEduca")

    janela.geometry("400x450")

    janela.configure(bg="#f0f0f0")
 
    # Título

    tk.Label(

        janela,

        text="Cadastro de Alunos",

        font=("Arial", 16, "bold"),

        bg="#f0f0f0"

    ).pack(pady=10)
 
    # Campo Nome

    tk.Label(janela, text="Nome do Aluno:", bg="#f0f0f0").pack()

    entrada_nome = tk.Entry(janela, width=40)

    entrada_nome.pack(pady=5)
 
    # Campo CPF

    tk.Label(janela, text="CPF:", bg="#f0f0f0").pack()

    entrada_cpf = tk.Entry(janela, width=40)

    entrada_cpf.pack(pady=5)
 
    # Campo Status

    tk.Label(janela, text="Status (Ativo/Inativo):", bg="#f0f0f0").pack()

    entrada_status = tk.Entry(janela, width=40)

    entrada_status.pack(pady=5)
 
    # Botões

    tk.Button(

        janela, text="Cadastrar", width=15,

        bg="#4CAF50", fg="white"

    ).pack(pady=5)
 
    tk.Button(

        janela, text="Atualizar", width=15,

        bg="#2196F3", fg="white"

    ).pack(pady=5)
 
    tk.Button(

        janela, text="Excluir", width=15,

        bg="#f44336", fg="white"

    ).pack(pady=5)
 
    tk.Button(

        janela, text="Consultar", width=15,

        bg="#9C27B0", fg="white"

    ).pack(pady=5)
 
    janela.mainloop()
 
 
if __name__ == "__main__":

    criar_janela_principal()
