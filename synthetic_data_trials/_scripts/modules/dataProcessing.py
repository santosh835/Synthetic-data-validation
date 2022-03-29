import pandas as pd
df=pd.read_csv("data/trial_data_reference.csv")
# changing the dataTypes as per metadata
def identifyCategoricalColumsn(df,metadata):
    category_features = list(metadata.loc[metadata['DataType'] == 'object', 'Variable'])
    
    for each in category_features:
        df[each] = df[each].astype('object')
        
    return df



