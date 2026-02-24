# Conversor de Temperatura 🌡️

Um aplicativo web moderno e responsivo em Python usando Flask para converter temperaturas entre Celsius e Fahrenheit, além de consultar o **clima em tempo real** de qualquer cidade do mundo.

## ✨ Funcionalidades

- **Conversão Bidirecional**: Converta de Celsius para Fahrenheit e vice-versa com validações físicas.
- **🌍 Clima por Localidade**: Digite o nome de qualquer cidade e veja a temperatura atual em Celsius e Fahrenheit, sensação térmica, umidade e velocidade do vento — tudo com ícones dinâmicos e visuais atraentes.
- **Histórico de Conversões**: Armazena as últimas 5 conversões realizadas.
- **Validação de Entrada**: Aceita apenas números válidos, com mensagens de erro claras.
- **Validação Física**: Impede temperaturas abaixo do zero absoluto (-273.15°C ou -459.67°F).
- **Interface Responsiva**: Design moderno com glassmorphism, abas e animações, adaptável a dispositivos móveis, tablets e desktops.
- **Feedback Visual**: Mensagens de sucesso, erro, aviso e info com estilos atraentes.
- **UI/UX Aprimorada**: Gradientes, ícones animados, cards dinâmicos de clima e tipografia moderna (Poppins).

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.x com Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5, Font Awesome 6, Google Fonts (Poppins)
- **APIs**: [Open-Meteo](https://open-meteo.com/) (geocodificação e clima — gratuita, sem API key)
- **Validação**: Lógica integrada no Flask
- **Sessões**: Gerenciamento de histórico com sessões do Flask

## 📋 Requisitos

- Python 3.6 ou superior
- Bibliotecas: Instale com `pip install -r requirements.txt`
  - Flask
  - requests
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
   - Abra `http://127.0.0.1:5000/`

## 📖 Uso

### Aba "Converter"
1. Selecione o tipo de conversão (Celsius → Fahrenheit ou vice-versa).
2. Digite a temperatura desejada.
3. Clique em **Converter** para ver o resultado.

### Aba "Clima por Local"
1. Digite o nome de uma cidade (ex.: São Paulo, Tokyo, London).
2. Clique em **Buscar**.
3. Veja a temperatura atual em °C e °F, sensação térmica, umidade e vento.

### Exemplo
- Conversão: 25°C → 77.00°F
- Clima: São Paulo → 22.5°C / 72.50°F, Parcialmente nublado

## 🎨 Interface

- Design glassmorphism moderno com fundo gradiente escuro.
- Abas animadas para alternar entre conversão e clima.
- Card de clima dinâmico que muda de cor conforme a condição (sol, chuva, neve, etc.).
- Ícone animado de clima com efeito flutuante.
- Totalmente responsivo para mobile.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:
- Abrir issues para relatar bugs ou sugerir melhorias.
- Enviar pull requests com novas funcionalidades ou correções.

## 📄 Licença

Este projeto é de código aberto. Consulte o arquivo LICENSE para mais detalhes (se aplicável).

---

**Desenvolvido com ❤️ usando Flask, Bootstrap e Open-Meteo API.**
