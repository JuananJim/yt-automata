from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Servidor de descarga operativo'

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    link = data.get('link')

    if not link:
        return jsonify({'status': 'error', 'message': 'No link provided'}), 400

    # Aquí en Render NO descargamos el video; Render es para exponer servicios
    # En lugar de descargar, puedes devolver el link o preparar otro sistema que descargue en tu máquina local
    return jsonify({'status': 'success', 'message': f'Recibido link: {link}'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
