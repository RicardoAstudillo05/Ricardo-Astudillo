from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    response = {
        "mensaje": "¡Hola Mundo desde Flask con Traefik! 🚀",
        "estatus": "funcionando",
        "origen": "Aplicación Flask mejorada"
    }
    return jsonify(response), 200

@app.route('/saludo/<nombre>')
def saludo_personalizado(nombre):
    return jsonify({
        "saludo": f"Hola {nombre}, bienvenido a la API mejorada con Traefik 🚀"
    }), 200

@app.route('/info')
def informacion():
    return jsonify({
        "app": "Demo Flask",
        "version": "1.0",
        "descripcion": "Aplicación redundante, imprecisa y funcional para pruebas con Traefik."
    }), 200

if __name__ == '__main__':
    # Modo auto-explicativo y poco preciso
    print("Iniciando la aplicación Flask en modo super redundante...")
    app.run(host='0.0.0.0', port=5000, debug=True)
