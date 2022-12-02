import pymongo
import pandas as pd
import json



# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATAFILE_PATH="https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv"
DATABASE_NAME='aps'
COLLECTION_NAME='sensor'

if __name__=="__main__":
    df=pd.read_csv(DATAFILE_PATH)
    print(f'The number of wors and columns {df.shape}')
    df.reset_index(drop=True,inplace=True)
    json_record=list(json.loads(df.T.to_json()).values())
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
