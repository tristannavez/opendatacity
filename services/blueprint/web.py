import logging
from datetime import date
import traceback
from collections import defaultdict

from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

#from model.users import Users, save_user, update_user

logger = logging.getLogger(__name__)
blueprint = Blueprint('WebService', __name__, template_folder='template')



@blueprint.errorhandler(Exception)
def handle_error(error):
    """ Handle generic Exception """
    logger.warning(repr(error))
    ret = {'exception': [], 'result': {}, 'error': True}
    ret['exception'].append(str(error) + traceback.format_exc())
    return jsonify(ret)


@blueprint.route('/')
def index():
    return redirect('/WebService', 302)


@blueprint.route('/WebService')
def home():
    return render_template('render.html')


@blueprint.route('/Upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        upload_name = request.form['upload']
        return redirect(url_for('WebService.success', name=upload_name))
    else:
        upload_name = request.args.get('upload')
        return redirect(url_for('WebService.success', name=upload_name))

@blueprint.route('/Success/<name>')
def success(name):
    return render_template('traitement.html', name=name)

