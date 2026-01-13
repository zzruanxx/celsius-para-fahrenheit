from flask import Flask, render_template, request, flash, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Para usar flash messages

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    historico = session.get('historico', [])
    
    if request.method == 'POST':
        entrada = request.form.get('temperatura', '').strip()
        escolha = request.form.get('escolha', 'C para F')
        
        if not entrada:
            flash("Digite uma temperatura antes de converter.", "warning")
        else:
            try:
                temp = float(entrada)
            except ValueError:
                flash("Digite um número válido (ex.: 25 ou -10.5).", "error")
            else:
                if escolha == "C para F" and temp < -273.15:
                    flash("Temperatura em Celsius não pode ser inferior a -273.15°C.", "error")
                elif escolha == "F para C" and temp < -459.67:
                    flash("Temperatura em Fahrenheit não pode ser inferior a -459.67°F.", "error")
                else:
                    if escolha == "C para F":
                        resultado = (temp * 9/5) + 32
                        msg = f"{temp}°C → {resultado:.2f}°F"
                    elif escolha == "F para C":
                        resultado = (temp - 32) * 5/9
                        msg = f"{temp}°F → {resultado:.2f}°C"
                    
                    historico.append(msg)
                    if len(historico) > 5:
                        historico.pop(0)
                    session['historico'] = historico
                    flash("Conversão realizada com sucesso!", "success")
    
    return render_template('index.html', resultado=resultado, historico=historico)

@app.route('/limpar')
def limpar():
    session.pop('historico', None)
    flash("Histórico limpo.", "info")
    return render_template('index.html', resultado=None, historico=[])

if __name__ == '__main__':
    app.run(debug=True)