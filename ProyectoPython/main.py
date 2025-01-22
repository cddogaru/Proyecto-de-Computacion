from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# FALTA CARGAR EL MODELO

@app.route('/', methods=['GET'])
def index():
    # Renderiza la página inicial
    error = request.args.get('error', None)
    return render_template('index.html', error=error)

# COMPLETAR CON MODELO
@app.route('/resultados', methods=['POST'])
def resultados():
    comunidad = request.form.get('comunidad')
    if not comunidad:
        # Si no se selecciona ninguna comunidad, redirigir al index con un mensaje de error
        return redirect(url_for('index', error="Por favor, selecciona una comunidad autónoma para ver las predicciones."))

    # FALTA VER COMO PROCESAR LOS DATOS PARA EL MODELO
    resultado = "Resultado de la predicción para " + comunidad

    # Ver como poner el tema graficas etc

if __name__ == '__main__':
    app.run(debug=True)
