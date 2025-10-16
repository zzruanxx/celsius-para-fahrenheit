import tkinter as tk
from tkinter import ttk

class ConversorTemperatura:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Temperatura")
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
        entrada = entrada.strip()  # Limpeza de entrada: remove espaços em branco
        if not self.validar_entrada(entrada):
            self.resultado_var.set("Erro: Digite um número válido")
            return
        temp = float(entrada)  # Removido try desnecessário, pois validar_entrada já garante que é um número
        # Validação física de temperatura
        if self.escolha_var.get() == "C para F" and temp < -273.15:
            self.resultado_var.set("Erro: Temperatura em Celsius não pode ser inferior a -273.15°C (zero absoluto)")
            return
        elif self.escolha_var.get() == "F para C" and temp < -459.67:
            self.resultado_var.set("Erro: Temperatura em Fahrenheit não pode ser inferior a -459.67°F (zero absoluto)")
            return
        if self.escolha_var.get() == "C para F":
            resultado = self.celsius_para_fahrenheit(temp)
            self.resultado_var.set(f"{temp}°C é igual a {resultado:.2f}°F")
        elif self.escolha_var.get() == "F para C":
            resultado = self.fahrenheit_para_celsius(temp)
            self.resultado_var.set(f"{temp}°F é igual a {resultado:.2f}°C")
        else:
            self.resultado_var.set("Erro: Escolha uma conversão válida")

    def enter_press(self, event):
        self.converter()

    def setup_ui(self):
        # Configurações de layout
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(3, weight=1)

        ttk.Label(self.root, text="Escolha a conversão:").grid(column=0, row=0, padx=10, pady=10, sticky="w")
        self.escolha_var = tk.StringVar()
        self.escolha_combobox = ttk.Combobox(self.root, textvariable=self.escolha_var)  # Corrigido: escolha_combox para escolha_combobox
        self.escolha_combobox['values'] = ("C para F", "F para C")
        self.escolha_combobox.grid(column=1, row=0, padx=10, pady=10, sticky="ew")

        ttk.Label(self.root, text="Digite a temperatura:").grid(column=0, row=1, padx=10, pady=10, sticky="w")
        self.entry_temperatura = tk.Entry(self.root)
        self.entry_temperatura.grid(column=1, row=1, padx=10, pady=10, sticky="ew")
        self.entry_temperatura.bind("<Return>", self.enter_press)

        self.botao_converter = ttk.Button(self.root, text="Converter", command=self.converter)
        self.botao_converter.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        self.resultado_var = tk.StringVar()
        self.resultado_label = ttk.Label(self.root, textvariable=self.resultado_var)
        self.resultado_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10, sticky="nsew")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorTemperatura(root)
    root.mainloop()