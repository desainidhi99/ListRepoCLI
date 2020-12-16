import json
from operator import itemgetter
from .printOutput import outputData
import pandas as pd



def sort_data_key(keyvalue,noOfRecords):
    data=[]
    with open('result_info.json', 'r') as f:
        data = json.load(f)


    sort_data = sorted(data, key = itemgetter(keyvalue), reverse = True)
    outputData(sort_data, keyvalue, noOfRecords)
    return sort_data




                