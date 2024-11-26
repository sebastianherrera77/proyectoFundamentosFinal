from flask import Flask, render_template, request, redirect, url_for, jsonify
 
app = Flask(__name__)

@app.route('/')
def index():
    #devuelve la plantilla html
    return render_template("index.html")


@app.route('/calcular_imc', methods=['POST'])
def calcular_imc():
    # Obtener los datos del formulario
    nombre = request.form.get('nombre')
    altura = float(request.form.get('altura')) / 100  # Convertir de cm a metros
    peso = float(request.form.get('peso'))

    # Calcular el IMC
    imc = peso / (altura ** 2)

    # Redirigir a la página correspondiente según el IMC
    if imc < 18.5:
        return redirect(url_for('bajo_peso', imc=round(imc, 2), nombre=nombre))
    elif 18.5 <= imc < 25:
        return redirect(url_for('peso_normal', imc=round(imc, 2), nombre=nombre))
    elif 25 <= imc < 30:
        return redirect(url_for('sobrepeso', imc=round(imc, 2), nombre=nombre))
    else:
        return redirect(url_for('obesidad', imc=round(imc, 2), nombre=nombre))


# Rutas para cada rango de IMC
@app.route('/bajo_peso', methods=['GET'])
def bajo_peso():
    imc = request.args.get('imc')
    nombre = request.args.get('nombre')
    return render_template('bajo_peso.html', imc=imc, nombre=nombre)

@app.route('/peso_normal', methods=['GET'])
def peso_normal():
    imc = request.args.get('imc')
    nombre = request.args.get('nombre')
    return render_template('peso_normal.html', imc=imc, nombre=nombre)

@app.route('/sobrepeso', methods=['GET'])
def sobrepeso():
    imc = request.args.get('imc')
    nombre = request.args.get('nombre')
    return render_template('sobrepeso.html', imc=imc, nombre=nombre)

@app.route('/obesidad', methods=['GET'])
def obesidad():
    imc = request.args.get('imc')
    nombre = request.args.get('nombre')
    return render_template('obesidad.html', imc=imc, nombre=nombre)

@app.route('/preguntas', methods=['GET'])
def preguntas():
    #devuelve la plantilla html
    return render_template("preguntas.html")


#### REGISTRO DE AGUA
# Lista para almacenar los registros de agua
registro = []

@app.route('/registro', methods=['GET', 'POST'])
def registro_agua():
    # Si el método es POST (cuando el formulario es enviado)
    if request.method == 'POST':
        dia = request.form.get('dia')
        vasos = request.form.get('vasos')

        # Si ambos campos están presentes, agregar el registro a la lista
        if dia and vasos:
            registro.append({'dia': dia, 'vasos': vasos})

    # Renderiza la página y pasa los registros actuales
    return render_template('registro_agua.html', registros=registro)

@app.route('/get_registros', methods=['GET'])
def get_registros():
    # Devuelve los registros en formato JSON
    return jsonify(registro)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
