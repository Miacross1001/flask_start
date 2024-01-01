from flask import Flask, jsonify, request

app = Flask('app')
base = []

@app.route('/announce', methods=['POST'])
def create_announce():
    data = request.json

    new_announce = {
        'title': data.get('title'),
        'descript': data.get('description'),
        'date_created': data.get('date_created'),
        'owner': data.get('owner')
    }

    base.append(new_announce)

    return jsonify(new_announce), 201

@app.route('/announce/<int:announce_id>', methods=['GET'])
def get_annouce(announce_id):
    step = next((ad for ad in base if ad['id'] == announce_id), None)

    if step:
        return jsonify(step), 200
    else:
        return jsonify({'error': 'No found'}), 400

@app.route('/announce/<int:announce_id>', methods=['DELETE'])
def delete_announce(announce_id):
    for ad in base:
        if ad['id'] == announce_id:
            base.remove(ad)
            return '', 204

    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')