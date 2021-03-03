import logging
from datetime import date
import traceback
from collections import defaultdict

from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template

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
def accueil():
    return render_template('render.html')

