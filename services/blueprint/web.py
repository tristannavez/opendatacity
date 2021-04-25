import logging
from datetime import date
import traceback
from collections import defaultdict
import datetime
import os
import mysql.connector
import pandas as pd
from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import Flask
from os.path import join, dirname, realpath

#from model.users import Users, save_user, update_user

logger = logging.getLogger(__name__)
blueprint = Blueprint('WebService', __name__, template_folder='template')

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'services/static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

#connexion à la BDD
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="api_python"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

# View All Database
for x in mycursor:
  print(x)

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


@blueprint.route('/Upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        upload_file = request.files['upload']
        if upload_file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], upload_file.filename)
            # set the file path
            upload_file.save(file_path)
        return redirect(url_for('WebService.success'))
    else:
        upload_name = request.args.get('upload')
        return redirect(url_for('WebService.success', name=upload_name))

#Garder le fichier sur la page traitement pour pouvoir le recup en argument pour la fonction parseCSV

def parseCSV(filePath):
    # CVS Column Names
    col_names = ['id', 'longitude', 'code_produit']
    # Use Pandas to parse the CSV file
    csvData = pd.read_csv(filePath, names=col_names, header=None)
    # Loop through the Rows
    for i, row in csvData.iterrows():
        sql = "INSERT INTO opendatacity (id, longitude, code_produit) VALUES (%s, %s, %s)"
        value = (row['id'], row['longitude'], row['code_produit'])
        mycursor.execute(sql, value, if_exists='append')
        mydb.commit()
        print(i, row['id'], row['longitude'], row['code_produit'])


@blueprint.route('/Success')
def success():
    return render_template('traitement.html')

