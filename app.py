from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Mi Súper App Flask 🔥</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #4b79a1, #283e51);
                color: white;
                text-align: center;
            }

            .navbar {
                width: 100%;
                background: rgba(0,0,0,0.3);
                padding: 15px 0;
                backdrop-filter: blur(8px);
                position: fixed;
                top: 0;
                left: 0;
            }

            .navbar a {
                margin: 0 20px;
                text-decoration: none;
                font-size: 18px;
                color: #f0f0f0;
                padding: 8px 14px;
                border-radius: 8px;
                transition: 0.3s;
            }

            .navbar a:hover {
                background: rgba(255,255,255,0.2);
            }

            .content {
                margin-top: 120px;
            }

            h1 {
                font-size: 40px;
                margin-bottom: 10px;
            }

            p {
                font-size: 20px;
                opacity: 0.9;
            }

            .card {
                background: rgba(255,255,255,0.15);
                padding: 20px;
                margin: 40px auto;
                width: 60%;
                border-radius: 15px;
                backdrop-filter: blur(10px);
            }
        </style>
    </head>

    <body>
        <div class="navbar">
            <a href="/">Inicio</a>
            <a href="/info">Información</a>
            <a href="/contacto">Contacto</a>
        </div>

        <div class="content">
            <h1>🚀 ¡Hola Mundo con Flask y Traefik!</h1>
            <p>Esta es una versión un poco más colorida, brillante y no tan seria 😅.</p>

            <div class="card">
                <h2>💡 Mini Tarjeta Informativa</h2>
                <p>
                    Esta app está corriendo en Flask, probablemente con Traefik,
                    y tiene estilos directamente embebidos con HTML + CSS.
                </p>
            </div>
        </div>

    </body>
    </html>
    """

@app.route('/info')
def info():
    return "<h1 style='color: blue;'>Información básica de prueba 😅</h1>"

@app.route('/contacto')
def contacto():
    return "<h1 style='color: green;'>Contacto (aunque no contacta a nadie) 😂</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
