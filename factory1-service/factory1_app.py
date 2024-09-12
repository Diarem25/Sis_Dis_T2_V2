from flask import Flask, request, jsonify
from factory1 import Factory1

app = Flask(__name__)

# Initialize Factory 1
factory1 = Factory1(5, 960)

@app.route('/produce', methods=['POST'])
def produce():
    data = request.get_json()
    demand = data.get('demand', 0)
    active_lines = demand // 48
    produced = factory1.run_production(active_lines)
    return jsonify({'produced': produced})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
