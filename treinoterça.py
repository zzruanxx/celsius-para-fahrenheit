import tkinter as tk
from tkinter import ttk

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def converter():
    try:
        if escolha_var.get() == "C para F":
            celsius = float(entry_temperatura.get())
            fahrenheit = celsius_para_fahrenheit(celsius)
            resultado_var.set(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
        elif escolha_var.get() == "F para C":
            fahrenheit = float(entry_temperatura.get())
            celsius = fahrenheit_para_celsius(fahrenheit)
            resultado_var.set(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
        else:
            resultado_var.set("Escolha inválida")
    except ValueError:
        resultado_var.set("Entrada inválida")

def enter_press(event):
    converter()


root = tk.Tk()    
root.title("Conversor de Temperatura")


ttk.Label(root, text="Escolha a conversão:").grid(column=0, row=0, padx=10, pady=10)

escolha_var = tk.StringVar()
escolha_combox = ttk.Combobox(root, textvariable=escolha_var)
escolha_combox['values'] = ("C para F", "F para C")
escolha_combox.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="Digite a temperatura:").grid(column=0, row=1, padx=10, pady=10)
entry_temperatura = tk.Entry(root)
entry_temperatura.grid(column=1, row=1, padx=10, pady=10)

botao_converter = ttk.Button(root, text="Converter", command=converter)
botao_converter.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

resultado_var = tk.StringVar()
resultado_label = ttk.Label(root, textvariable=resultado_var)
resultado_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)


root.mainloop()
