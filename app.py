# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    jsonify)


import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('nbagg')
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Datasets/belly_button_biodiversity.sqlite")


#Map the base keys to find the sql lite tables
Base = automap_base()
Base.prepare(engine, reflect=True)

#Assign tables to variables for quering
samples= Base.classes.samples
otu =Base.classes.otu
meta=Base.classes.samples_metadata

session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("/index.html")


@app.route('/names')
def names():
    #find the columns with the inspector
    inspector = inspect(engine)
    columns = inspector.get_columns('samples')
    sample_columns = []
    for c in columns:
        sample_columns.append(c)
    
    #get the values of the columns and append to list
    sample_names= []
    for names in sample_columns:
        sample_names.append(names["name"])

    #return the jsonified list
    samplenames = sample_names[1:]
    return jsonify(samplenames)
    

@app.route('/otu')
def otu_description():
    #otu_list = session.query(otu.lowest_taxonomic_unit_found).all()
    return session.query(otu.lowest_taxonomic_unit_found).all()

@app.route('/metadata/<sample>')
def metadata(metainput):
    for AGE, BBTYPE, ETHNICITY, GENDER, LOCATION, SAMPLEID in session.query(meta.AGE, meta.BBTYPE, meta.ETHNICITY, meta.GENDER, meta.LOCATION, meta.SAMPLEID).\
        filter_by(SAMPLEID = metainput):
            metadict = {'AGE': AGE, 
                          "BBTY": BBTYPE, 
                          'ETHINICITY': ETHNICITY,
                          'GENDER': GENDER,
                          'LOCATION': LOCATION,
                          'SAMPLEID': SAMPLEID 
                        }
    return metadict

@app.route('/wfreq/<sample>')
def wash_frequency(sample_input):
    for SAMPLEID, WFREQ in session.query(meta.SAMPLEID, meta.WFREQ).\
        filter_by(SAMPLEID = sample_input):
        return WFREQ

if __name__ == "__main__":
    app.run(debug=True)