from flask import Flask, render_template, request, flash, session, jsonify
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def get_weather_data(city_name):
    """Busca coordenadas da cidade e retorna dados meteorológicos."""
    # Geocodificação
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": city_name, "count": 1, "language": "pt"}
    geo_resp = requests.get(geo_url, params=geo_params, timeout=10)
    geo_data = geo_resp.json()

    if "results" not in geo_data or len(geo_data["results"]) == 0:
        return None

    location = geo_data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]
    city_display = location.get("name", city_name)
    country = location.get("country", "")
    admin1 = location.get("admin1", "")

    # Buscar clima atual
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m",
        "timezone": "auto"
    }
    weather_resp = requests.get(weather_url, params=weather_params, timeout=10)
    weather_data = weather_resp.json()

    current = weather_data.get("current", {})
    temp_c = current.get("temperature_2m", 0)
    temp_f = (temp_c * 9 / 5) + 32
    apparent_c = current.get("apparent_temperature", 0)
    apparent_f = (apparent_c * 9 / 5) + 32
    humidity = current.get("relative_humidity_2m", 0)
    wind_speed = current.get("wind_speed_10m", 0)
    weather_code = current.get("weather_code", 0)

    return {
        "city": city_display,
        "admin1": admin1,
        "country": country,
        "temp_c": round(temp_c, 2),
        "temp_f": round(temp_f, 2),
        "apparent_c": round(apparent_c, 2),
        "apparent_f": round(apparent_f, 2),
        "humidity": humidity,
        "wind_speed": wind_speed,
        "weather_code": weather_code,
        "lat": lat,
        "lon": lon
    }

def weather_icon_and_label(code):
    """Retorna ícone FA e descrição para o weather_code do Open-Meteo."""
    mapping = {
        0: ("fa-sun", "Céu limpo", "sunny"),
        1: ("fa-sun", "Predominantemente limpo", "sunny"),
        2: ("fa-cloud-sun", "Parcialmente nublado", "cloudy"),
        3: ("fa-cloud", "Nublado", "overcast"),
        45: ("fa-smog", "Neblina", "foggy"),
        48: ("fa-smog", "Neblina com geada", "foggy"),
        51: ("fa-cloud-rain", "Garoa leve", "rainy"),
        53: ("fa-cloud-rain", "Garoa moderada", "rainy"),
        55: ("fa-cloud-showers-heavy", "Garoa intensa", "rainy"),
        61: ("fa-cloud-rain", "Chuva leve", "rainy"),
        63: ("fa-cloud-showers-heavy", "Chuva moderada", "rainy"),
        65: ("fa-cloud-showers-heavy", "Chuva forte", "rainy"),
        71: ("fa-snowflake", "Neve leve", "snowy"),
        73: ("fa-snowflake", "Neve moderada", "snowy"),
        75: ("fa-snowflake", "Neve forte", "snowy"),
        80: ("fa-cloud-rain", "Pancadas leves", "rainy"),
        81: ("fa-cloud-showers-heavy", "Pancadas moderadas", "rainy"),
        82: ("fa-cloud-showers-heavy", "Pancadas fortes", "rainy"),
        95: ("fa-bolt", "Tempestade", "stormy"),
        96: ("fa-bolt", "Tempestade com granizo", "stormy"),
        99: ("fa-bolt", "Tempestade forte com granizo", "stormy"),
    }
    return mapping.get(code, ("fa-cloud", "Indefinido", "cloudy"))

app.jinja_env.globals.update(weather_icon_and_label=weather_icon_and_label)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    historico = session.get('historico', [])
    weather = None

    if request.method == 'POST':
        # Verifica se é busca de clima ou conversão
        if 'cidade' in request.form:
            cidade = request.form.get('cidade', '').strip()
            if not cidade:
                flash("Digite o nome de uma cidade.", "warning")
            else:
                try:
                    weather = get_weather_data(cidade)
                    if weather is None:
                        flash(f"Cidade '{cidade}' não encontrada. Tente outro nome.", "error")
                    else:
                        flash(f"Clima atual de {weather['city']} carregado!", "success")
                except Exception:
                    flash("Erro ao buscar dados meteorológicos. Tente novamente.", "error")
        else:
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
                            resultado = (temp * 9 / 5) + 32
                            msg = f"{temp}°C → {resultado:.2f}°F"
                        elif escolha == "F para C":
                            resultado = (temp - 32) * 5 / 9
                            msg = f"{temp}°F → {resultado:.2f}°C"

                        historico.append(msg)
                        if len(historico) > 5:
                            historico.pop(0)
                        session['historico'] = historico
                        flash("Conversão realizada com sucesso!", "success")

    return render_template('index.html', resultado=resultado, historico=historico, weather=weather)

@app.route('/limpar')
def limpar():
    session.pop('historico', None)
    flash("Histórico limpo.", "info")
    return render_template('index.html', resultado=None, historico=[], weather=None)

if __name__ == '__main__':
    app.run(debug=True)