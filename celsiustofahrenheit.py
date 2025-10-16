import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")  # Modo de aparência inicial (System, Dark, Light)
ctk.set_default_color_theme("dark-blue")  # Tema de cor

class ConversorTemperatura:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Temperatura")
        self.root.geometry("450x400")
        self.root.resizable(False, False)
        self.historico = []  # Lista para armazenar histórico de conversões
        self.setup_ui()

    def celsius_para_fahrenheit(self, celsius):
        """Converte Celsius para Fahrenheit."""
        return (celsius * 9/5) + 32

    def fahrenheit_para_celsius(self, fahrenheit):
        """Converte Fahrenheit para Celsius."""
        return (fahrenheit - 32) * 5/9

    def validar_entrada(self, entrada):
        """Valida se a entrada é um número."""
        try:
            float(entrada)
            return True
        except ValueError:
            return False

    def converter(self):
        entrada = self.entry_temperatura.get()
        entrada = entrada.strip()
        self.entry_temperatura.configure(fg_color="white" if ctk.get_appearance_mode() == "Light" else "#2b2b2b")  # Resetar cor
        if not self.validar_entrada(entrada):
            messagebox.showerror("Erro", "Por favor, digite um número válido (ex.: 25 ou -10.5).")
            self.entry_temperatura.configure(fg_color="lightcoral")
            return
        temp = float(entrada)
        if self.escolha_var.get() == "C para F" and temp < -273.15:
            messagebox.showerror("Erro", "Temperatura em Celsius não pode ser inferior a -273.15°C (zero absoluto).")
            self.entry_temperatura.configure(fg_color="lightcoral")
            return
        elif self.escolha_var.get() == "F para C" and temp < -459.67:
            messagebox.showerror("Erro", "Temperatura em Fahrenheit não pode ser inferior a -459.67°F (zero absoluto).")
            self.entry_temperatura.configure(fg_color="lightcoral")
            return
        if self.escolha_var.get() == "C para F":
            resultado = self.celsius_para_fahrenheit(temp)
            msg = f"{temp}°C é igual a {resultado:.2f}°F"
        elif self.escolha_var.get() == "F para C":
            resultado = self.fahrenheit_para_celsius(temp)
            msg = f"{temp}°F é igual a {resultado:.2f}°C"
        else:
            messagebox.showerror("Erro", "Selecione uma opção de conversão válida.")
            return
        self.resultado_var.set(msg)
        self.adicionar_historico(msg)

    def adicionar_historico(self, msg):
        """Adiciona conversão ao histórico e atualiza a lista."""
        self.historico.append(msg)
        if len(self.historico) > 5:  # Manter apenas últimas 5
            self.historico.pop(0)
        self.historico_listbox.delete(0, ctk.END)
        for item in self.historico:
            self.historico_listbox.insert(ctk.END, item)

    def limpar(self):
        """Limpa entrada, resultado e histórico."""
        self.entry_temperatura.delete(0, ctk.END)
        self.resultado_var.set("")
        self.entry_temperatura.configure(fg_color="white" if ctk.get_appearance_mode() == "Light" else "#2b2b2b")
        self.historico.clear()
        self.historico_listbox.delete(0, ctk.END)

    def alternar_tema(self):
        """Alterna entre modo claro e escuro."""
        modo_atual = ctk.get_appearance_mode()
        novo_modo = "Dark" if modo_atual == "Light" else "Light"
        ctk.set_appearance_mode(novo_modo)
        self.entry_temperatura.configure(fg_color="white" if novo_modo == "Light" else "#2b2b2b")

    def enter_press(self, event):
        self.converter()

    def setup_ui(self):
        # Frame principal
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        # Título
        ctk.CTkLabel(main_frame, text="Conversor de Temperatura", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)

        # Seleção de conversão
        ctk.CTkLabel(main_frame, text="Escolha a conversão:").pack(pady=5)
        self.escolha_var = ctk.StringVar(value="C para F")
        self.escolha_combobox = ctk.CTkComboBox(main_frame, variable=self.escolha_var, values=["C para F", "F para C"])
        self.escolha_combobox.pack(pady=5)

        # Entrada de temperatura
        ctk.CTkLabel(main_frame, text="Digite a temperatura:").pack(pady=5)
        self.entry_temperatura = ctk.CTkEntry(main_frame, placeholder_text="Ex.: 25")
        self.entry_temperatura.pack(pady=5)
        self.entry_temperatura.bind("<Return>", self.enter_press)

        # Botões
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(pady=10)
        ctk.CTkButton(button_frame, text="Converter", command=self.converter).pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(button_frame, text="Limpar", command=self.limpar).pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(button_frame, text="Alternar Tema", command=self.alternar_tema).pack(side=ctk.LEFT, padx=5)

        # Resultado
        self.resultado_var = ctk.StringVar()
        ctk.CTkLabel(main_frame, textvariable=self.resultado_var, wraplength=400).pack(pady=10)

        # Histórico
        ctk.CTkLabel(main_frame, text="Histórico (últimas 5 conversões):").pack(pady=5)
        self.historico_listbox = ctk.CTkScrollableFrame(main_frame, height=100)
        self.historico_listbox.pack(fill=ctk.X, padx=10, pady=5)

if __name__ == "__main__":
    root = ctk.CTk()
    app = ConversorTemperatura(root)
    root.mainloop()