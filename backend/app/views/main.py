from flask import Blueprint, send_file, abort, Response, jsonify,request
from app.util import recomendation_system
from flask_cors import cross_origin

blueprint = Blueprint('main',__name__)

@blueprint.route('/uid/',methods=['GET','POST'])
@cross_origin()
def list_uid():
	uid = request.args.get('url')
	print('oi')
	return jsonify(recomendation_system.show_top_five(uid))

