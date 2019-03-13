from flask import Flask, abort
from classes.car_data import Car

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    abort(500)


@app.route('/api/data/<string:args>', methods=['GET'])
def get_data(args):
    if len(args) == 11:
        return Car.find_by_phone(args)
    elif len(args) == 17:
        return Car.find_by_vin(args)
    elif len(args) == 9:
        return Car.find_by_number(args)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
