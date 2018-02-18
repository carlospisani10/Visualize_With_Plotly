
# coding: utf-8

# In[1]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func


# In[2]:


import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('nbagg')
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


# In[3]:


engine = create_engine("sqlite:///belly_button_biodiversity.sqlite", echo=False)


# In[4]:


session = Session(engine)


# In[5]:


Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()


# In[6]:


samples= Base.classes.samples
otu =Base.classes.otu
meta=Base.classes.samples_metadata


# #  """List of sample names.
# 
#     Returns a list of sample names in the format
#     [
#         "BB_940",
#         "BB_941",
#         "BB_943",
#         "BB_944",
#         "BB_945",
#         "BB_946",
#         "BB_947",
#         ...
#     ]
#     """

# In[7]:


def names():
inspector = inspect(engine)
columns = inspector.get_columns('otu')
for c in columns:
    print(c['name'], c["type"])


# In[8]:


inspector = inspect(engine)
columns = inspector.get_columns('samples')
sample_columns = []
for c in columns:
    sample_columns.append(c)


# In[70]:


sample_names= []
for names in sample_columns:
    sample_names.append(names["name"])

samplenames = sample_names[1:]



# In[10]:


return(jsonify(samplenames))


# #  """List of OTU descriptions.
# 
#     Returns a list of OTU descriptions in the following format
# 
#     [
#         "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
#         "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
#         "Bacteria",
#         "Bacteria",
#         "Bacteria",
#         ...
#     ]
#     """

# In[11]:


session.query(otu.lowest_taxonomic_unit_found).all()


# #    """MetaData for a given sample.
# 
#     Args: Sample in the format: `BB_940`
# 
#     Returns a json dictionary of sample metadata in the format
# 
#     {
#         AGE: 24,
#         BBTYPE: "I",
#         ETHNICITY: "Caucasian",
#         GENDER: "F",
#         LOCATION: "Beaufort/NC",
#         SAMPLEID: 940
#     }
#     """

# In[64]:


inspector = inspect(engine)
columns = inspector.get_columns('samples_metadata')
#stuff = []
for c in columns:
    print(c['name'], c["type"])
    #stuff.append(c)


# In[28]:


age = session.query(meta.AGE).all()
bbtype = session.query(meta.BBTYPE).all()
ethnicity = session.query(meta.ETHNICITY).all()
gender =  session.query(meta.GENDER).all()
location =  session.query(meta.LOCATION).all()
sampleid =  session.query(meta.SAMPLEID).all()


# In[51]:


sampleid[2]


# In[44]:


meta_list = []
counter = 0
while counter < 153:
    meta_dic[counter] = {}
    meta_dic[counter]["AGE"] = age[counter]
    meta_dic[counter]["BBTYPE"] = bbtype[counter]
    meta_dic[counter]["ETHNICITY"] = ethnicity[counter]
    meta_dic[counter]["GENDER"] = gender[counter]
    meta_dic[counter]["LOCATION"] = location[counter]
    meta_dic[counter]["SAMPLEID"] = sampleid[counter]
    meta_list.append(meta_dic[counter])
    counter = counter + 1
    


# In[46]:





# #     """Weekly Washing Frequency as a number.
# 
#     Args: Sample in the format: `BB_940`
# 
#     Returns an integer value for the weekly washing frequency `WFREQ`
#     """
# ```

# In[55]:


def wash_frequency(sample_input):

    for SAMPLEID, WFREQ in session.query(meta.SAMPLEID, meta.WFREQ).        filter_by(SAMPLEID = sample_input):
        return print(WFREQ)

wash_frequency("940")


# # """OTU IDs and Sample Values for a given sample.
# 
#     Sort your Pandas DataFrame (OTU ID and Sample Value)
#     in Descending Order by Sample Value
# 
#     Return a list of dictionaries containing sorted lists  for `otu_ids`
#     and `sample_values`
# 
#     [
#         {
#             otu_ids: [
#                 1166,
#                 2858,
#                 481,
#                 ...
#             ],
#             sample_values: [
#                 163,
#                 126,
#                 113,
#                 ...
#             ]
#         }
#     ]
#     """
# ```

# In[69]:


#session.query(meta.SAMPLEID).all()
session.query(samples.BB_940).order_by(samples.BB_940.desc()).all()

