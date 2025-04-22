import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha - AFD")
        self.jogador = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        self.criar_interface()

    def criar_interface(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                command=lambda i=i, j=j: self.jogada(i, j))
                btn.grid(row=i, column=j)
                self.botoes[i][j] = btn

    def jogada(self, i, j):
        if self.tabuleiro[i][j] == "":
            self.tabuleiro[i][j] = self.jogador
            self.botoes[i][j].config(text=self.jogador)

            if self.verificar_vitoria(self.jogador):
                messagebox.showinfo("Fim de jogo", f"🏆 Jogador {self.jogador} venceu!")
                self.reiniciar()
            elif self.tabuleiro_cheio():
                messagebox.showinfo("Fim de jogo", "🤝 Empate!")
                self.reiniciar()
            else:
                self.jogador = "O" if self.jogador == "X" else "X"

    def verificar_vitoria(self, jogador):
        for i in range(3):
            if all(self.tabuleiro[i][j] == jogador for j in range(3)) or all(self.tabuleiro[j][i] == jogador for j in range(3)):
                return True
        if all(self.tabuleiro[i][i] == jogador for i in range(3)) or all(self.tabuleiro[i][2 - i] == jogador for i in range(3)):
            return True
        return False

    def tabuleiro_cheio(self):
        return all(self.tabuleiro[i][j] != "" for i in range(3) for j in range(3))

    def reiniciar(self):
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.jogador = "X"
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
