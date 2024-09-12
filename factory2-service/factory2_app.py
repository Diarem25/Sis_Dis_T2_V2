from flask import Flask, request, jsonify
from factory2 import Factory2

app = Flask(__name__)

factory2 = Factory2(8, 160)

@app.route('/produce', methods=['POST'])
def produce():
    data = request.get_json()
    demand = data.get('demand', 0)
    a = factory2.generate_random_binomial()
    b = factory2.generate_random_binomial()
    c = factory2.generate_random_binomial()
    d = factory2.generate_random_binomial()
    e = demand - a - b - c - d
    product_types = [a, b, c, d, e]

    produced = factory2.run_production(product_types)
    return jsonify({'produced': produced})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
