# Install dataset from https://www.yelp.com/dataset/download
# Extract wherever. Rename it yelp_dataset.tgz
# Re-extract. Now it has 5 files, place them in the root of this folder


import pandas as pd

#Pandas can read many data types. CSV and JSON are most common
#Lines = True means the JSON is written in lines with \n
df = pd.read_json('yelp_academic_dataset_business.json', lines=True)

#Allows us to view each column we have to work with
print(df.columns)
