# Conversor de Temperatura

Um aplicativo web simples em Python usando Flask para converter temperaturas entre Celsius e Fahrenheit.

## Funcionalidades
- Conversão bidirecional com validações físicas.
- Histórico de conversões (últimas 5).
- Validação de entrada: Apenas números são aceitos.
- Validação física: Impede temperaturas abaixo do zero absoluto.
- Interface web responsiva.
- Mensagens de feedback para ações.

## Requisitos
- Python 3.x
- Bibliotecas: Instale com `pip install -r requirements.txt`
  - Flask

## Instalação
1. Clone ou baixe o repositório.
2. Navegue até o diretório: `cd /workspaces/celsius-para-fahrenheit`
3. Instale dependências: `pip install -r requirements.txt`
4. Execute: `python celsiustofahrenheit.py`

## Uso
- Abra o navegador e acesse `http://127.0.0.1:5000/`
- Selecione conversão, digite temperatura e converta.
- Visualize histórico de conversões.
- Use "Limpar Histórico" para resetar.

## Exemplo
- Entrada: 25 (C para F) → Saída: 25.00°C é igual a 77.00°F

## Contribuição
Sinta-se à vontade para abrir issues ou pull requests para melhorias.
