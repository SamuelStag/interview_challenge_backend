from flask import Blueprint
from flask import jsonify, make_response, request
from presenter.hoa import get_hoas, add_hoas, get_hoas_by_id
import json


hoa_views = Blueprint("hoa", __name__)


@hoa_views.route('/hoas', methods=['GET'])
def get_hoa():
    hoas = get_hoas()
    r = []
    for hoa in hoas:
        r.append(hoa.__dict__)
    return make_response(jsonify({"hoas": r}), 200)

@hoa_views.route('/hoa', methods=['GET'])
def get_single_hoa():
    val = int(request.args.get("id"))
    hoas = get_hoas_by_id(val)
    r = []
    for hoa in hoas:
        r.append(hoa.__dict__)
    return make_response(jsonify({"hoas": r}), 200)

@hoa_views.route('/hoa', methods=['POST'])
def add_hoa_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if "hoa_name" not in data:
        return make_response(jsonify({"status": "bad request"}), 400)

    hoa_name = data["hoa_name"]
    hoa_address = data["hoa_address"]

    add_hoa(hoa_name,hoa_address)
    return make_response(jsonify({"status": "success"}), 200)
