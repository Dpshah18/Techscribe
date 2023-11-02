from flask import Flask, request, jsonify
from readability import Readability

app = Flask(__name)

@app.route('/calculate_fog_index', methods=['POST'])
def calculate_fog_index():
    data = request.get_json()
    text = data.get('text', '')

    r = Readability(text)
    fog_index = r.gunning_fog()

    return jsonify({'fogIndex': fog_index})

if __name__ == '__main__':
    app.run(debug=True)
