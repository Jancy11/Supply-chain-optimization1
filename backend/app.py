from flask import Flask, jsonify, request
from app.demand_forecasting.model import forecast_sales
from app.route_optimization.graph import create_graph, get_shortest_path
from app.inventory_management.eoq import calculate_eoq
from app.resource_allocation.allocation import optimize_resources

app = Flask(__name__)

@app.route('/forecast', methods=['POST'])
def forecast():
    data = request.json
    forecasted = forecast_sales(data['data_path'], steps=data.get('steps', 30))
    return jsonify(forecasted.tolist())

@app.route('/shortest-path', methods=['POST'])
def shortest_path():
    data = request.json
    graph = create_graph(data['edges'])
    path, distance = get_shortest_path(graph, data['source'], data['target'])
    return jsonify({"path": path, "distance": distance})

@app.route('/eoq', methods=['POST'])
def eoq():
    data = request.json
    eoq = calculate_eoq(data['demand'], data['ordering_cost'], data['holding_cost'])
    return jsonify({"eoq": eoq})

@app.route('/resource-allocation', methods=['GET'])
def resource_allocation():
    result = optimize_resources()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
