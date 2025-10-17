import customtkinter as ctk
from tkinter import messagebox
import pyperclip  # Para copiar para área de transferência (adicione ao requirements.txt se necessário)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class ConversorTemperatura:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Temperatura")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.historico = []
        self.setup_ui()
        self.entry_temperatura.focus()  # Foco automático no campo de entrada

    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_para_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def validar_entrada(self, entrada):
        try:
            float(entrada)
            return True
        except ValueError:
            return False

    def converter(self):
        entrada = self.entry_temperatura.get().strip()
        if not entrada:
            messagebox.showwarning("Aviso", "Digite uma temperatura antes de converter.")
            return
        self.entry_temperatura.configure(fg_color="white" if ctk.get_appearance_mode() == "Light" else "#2b2b2b")
        if not self.validar_entrada(entrada):
            messagebox.showerror("Erro", "Digite um número válido (ex.: 25 ou -10.5).")
            self.entry_temperatura.configure(fg_color="lightcoral")
            return
        temp = float(entrada)
        if self.escolha_var.get() == "C para F" and temp < -273.15:
            messagebox.showerror("Erro", "Temperatura em Celsius não pode ser inferior a -273.15°C.")
            self.entry_temperatura.configure(fg_color="lightcoral")
            return
        elif self.escolha_var.get() == "F para C" and temp < -459.67:
            messagebox.showerror("Erro", "Temperatura em Fahrenheit não pode ser inferior a -459.67°F.")
            self.entry_temperatura.configure(fg_color="lightcoral")
            return
        if self.escolha_var.get() == "C para F":
            resultado = self.celsius_para_fahrenheit(temp)
            msg = f"{temp}°C → {resultado:.2f}°F"
        elif self.escolha_var.get() == "F para C":
            resultado = self.fahrenheit_para_celsius(temp)
            msg = f"{temp}°F → {resultado:.2f}°C"
        else:
            messagebox.showerror("Erro", "Selecione uma conversão válida.")
            return
        self.resultado_var.set(msg)
        self.adicionar_historico(msg)
        # Feedback visual: piscar em verde
        self.entry_temperatura.configure(fg_color="lightgreen")
        self.root.after(500, lambda: self.entry_temperatura.configure(fg_color="white" if ctk.get_appearance_mode() == "Light" else "#2b2b2b"))

    def adicionar_historico(self, msg):
        self.historico.append(msg)
        if len(self.historico) > 5:
            self.historico.pop(0)
        self.historico_textbox.delete("1.0", ctk.END)
        self.historico_textbox.insert(ctk.END, "\n".join(self.historico))

    def limpar(self):
        self.entry_temperatura.delete(0, ctk.END)
        self.resultado_var.set("")
        self.entry_temperatura.configure(fg_color="white" if ctk.get_appearance_mode() == "Light" else "#2b2b2b")
        self.historico.clear()
        self.historico_textbox.delete("1.0", ctk.END)

    def copiar_resultado(self):
        resultado = self.resultado_var.get()
        if resultado:
            pyperclip.copy(resultado)
            messagebox.showinfo("Copiado", "Resultado copiado para a área de transferência!")
        else:
            messagebox.showwarning("Aviso", "Nenhum resultado para copiar.")

    def alternar_tema(self):
        modo_atual = ctk.get_appearance_mode()
        novo_modo = "Dark" if modo_atual == "Light" else "Light"
        ctk.set_appearance_mode(novo_modo)
        self.entry_temperatura.configure(fg_color="white" if novo_modo == "Light" else "#2b2b2b")

    def enter_press(self, event):
        self.converter()

    def setup_ui(self):
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(main_frame, text="Conversor de Temperatura", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=15)

        # Grupo de seleção
        select_frame = ctk.CTkFrame(main_frame)
        select_frame.pack(pady=10, fill=ctk.X)
        ctk.CTkLabel(select_frame, text="Escolha a conversão:").pack(pady=5)
        self.escolha_var = ctk.StringVar(value="C para F")
        self.escolha_combobox = ctk.CTkComboBox(select_frame, variable=self.escolha_var, values=["C para F", "F para C"])
        self.escolha_combobox.pack(pady=5)

        # Grupo de entrada
        input_frame = ctk.CTkFrame(main_frame)
        input_frame.pack(pady=10, fill=ctk.X)
        ctk.CTkLabel(input_frame, text="Digite a temperatura:").pack(pady=5)
        self.entry_temperatura = ctk.CTkEntry(input_frame, placeholder_text="Ex.: 25")
        self.entry_temperatura.pack(pady=5)
        self.entry_temperatura.bind("<Return>", self.enter_press)

        # Botões
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(pady=15)
        self.botao_converter = ctk.CTkButton(button_frame, text="Converter", command=self.converter)
        self.botao_converter.pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(button_frame, text="Limpar", command=self.limpar).pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(button_frame, text="Copiar Resultado", command=self.copiar_resultado).pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(button_frame, text="Alternar Tema", command=self.alternar_tema).pack(side=ctk.LEFT, padx=5)

        # Tooltips (simples, usando after para simular)
        self.botao_converter.bind("<Enter>", lambda e: self.mostrar_tooltip("Clique para converter a temperatura"))
        self.botao_converter.bind("<Leave>", lambda e: self.ocultar_tooltip())

        # Resultado
        result_frame = ctk.CTkFrame(main_frame)
        result_frame.pack(pady=10, fill=ctk.X)
        self.resultado_var = ctk.StringVar()
        ctk.CTkLabel(result_frame, textvariable=self.resultado_var, font=ctk.CTkFont(size=14)).pack(pady=5)

        # Histórico
        hist_frame = ctk.CTkFrame(main_frame)
        hist_frame.pack(pady=10, fill=ctk.BOTH, expand=True)
        ctk.CTkLabel(hist_frame, text="Histórico (últimas 5):").pack(pady=5)
        self.historico_textbox = ctk.CTkTextbox(hist_frame, height=100, wrap="word")
        self.historico_textbox.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5)

    def mostrar_tooltip(self, texto):
        self.tooltip = ctk.CTkLabel(self.root, text=texto, fg_color="gray", corner_radius=5)
        self.tooltip.place(x=50, y=50)

    def ocultar_tooltip(self):
        if hasattr(self, 'tooltip'):
            self.tooltip.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = ConversorTemperatura(root)
    root.mainloop()