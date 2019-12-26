from flask import Flask, request
import utils

app = Flask(__name__)

@app.route('/get_info')
def get_info():
    id = request.args.get('id')
    platform = request.args.get('platform')
    return utils.get_detail(platform, id)

@app.route('/get_weapons')
def get_weapons():
    id = request.args.get('id')
    platform = request.args.get('platform')
    return utils.get_weapons(platform, id)

@app.route('/get_vehicles')
def get_vehicles():
    id = request.args.get('id')
    platform = request.args.get('platform')
    return utils.get_vehicles(platform, id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
