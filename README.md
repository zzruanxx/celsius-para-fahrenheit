# Conversor de Temperatura 🌡️

Um aplicativo web moderno e responsivo em Python usando Flask para converter temperaturas entre Celsius e Fahrenheit. Com interface bonita e intuitiva, validações robustas e histórico de conversões.

## ✨ Funcionalidades

- **Conversão Bidirecional**: Converta de Celsius para Fahrenheit e vice-versa com validações físicas.
- **Histórico de Conversões**: Armazena as últimas 5 conversões realizadas.
- **Validação de Entrada**: Aceita apenas números válidos, com mensagens de erro claras.
- **Validação Física**: Impede temperaturas abaixo do zero absoluto (-273.15°C ou -459.67°F).
- **Interface Responsiva**: Design moderno e adaptável a dispositivos móveis, tablets e desktops.
- **Feedback Visual**: Mensagens de sucesso, erro, aviso e info com estilos atraentes.
- **UI/UX Aprimorada**: Gradientes, ícones e animações sutis para uma experiência agradável.

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.x com Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5, Font Awesome, Google Fonts (Roboto)
- **Validação**: Lógica integrada no Flask
- **Sessões**: Gerenciamento de histórico com sessões do Flask

## 📋 Requisitos

- Python 3.6 ou superior
- Bibliotecas: Instale com `pip install -r requirements.txt`
  - Flask
  - Pillow (para futuras expansões)
  - pyperclip (para futuras expansões)

## 🚀 Instalação e Execução

1. **Clone ou baixe o repositório**:
   ```bash
   git clone https://github.com/zzruanxx/celsius-para-fahrenheit.git
   cd celsius-para-fahrenheit
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o aplicativo**:
   ```bash
   python celsiustofahrenheit.py
   ```

4. **Acesse no navegador**:
   - Abra `http://127.0.0.1:5000/` (ou a porta indicada no terminal, ex.: 5001 se houver conflito).

## 📖 Uso

1. Selecione o tipo de conversão (Celsius para Fahrenheit ou vice-versa).
2. Digite a temperatura desejada (ex.: 25).
3. Clique em "Converter" para ver o resultado.
4. Visualize o histórico das últimas 5 conversões.
5. Use "Limpar Histórico" para resetar o histórico.

### Exemplo
- Entrada: 25°C → Saída: 77.00°F
- Entrada: 77°F → Saída: 25.00°C

## 🎨 Interface

A interface foi redesenhada para ser bonita e responsiva:
- Gradiente de fundo atrativo.
- Ícones do Font Awesome para melhor usabilidade.
- Formulários com foco visual e validação.
- Layout centrado e moderno.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:
- Abrir issues para relatar bugs ou sugerir melhorias.
- Enviar pull requests com novas funcionalidades ou correções.

## 📄 Licença

Este projeto é de código aberto. Consulte o arquivo LICENSE para mais detalhes (se aplicável).

---

**Desenvolvido com ❤️ usando Flask e Bootstrap.**
