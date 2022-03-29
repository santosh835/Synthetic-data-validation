import pandas as pd
from _scripts.modules.dataProcessing import identifyCategoricalColumsn
from _scripts.modules import similarity_metric


#import metadata
metadata=pd.read_csv("data/trial_data_description.csv")
#import refernce data
reference_data=pd.read_csv("data/trial_data_reference.csv")
# importing synthetic data
trial_data_A=pd.read_csv("data/trial_data_A.csv")
trial_data_B=pd.read_csv("data/trial_data_B.csv")
trial_data_C=pd.read_csv("data/trial_data_C.csv")

#this function will return the overall similarity score bewteen synthectic data and real data
def initiateSimilaritybMetrics(real_data,synthectic_data,metadata):
    #changing data types of the refernce and synthetic data as per metadata
    # Object datatype will be converted to Category later
    real_data=identifyCategoricalColumsn(real_data,metadata)
    synthectic_data=identifyCategoricalColumsn(synthectic_data,metadata)
    return similarity_metric.evaluationMetricsQunatitative(synthectic_data,real_data)
    
if __name__ == "__main__": 
    score_A=initiateSimilaritybMetrics(reference_data,trial_data_A,metadata)
    score_B=initiateSimilaritybMetrics(reference_data,trial_data_B,metadata)
    score_C=initiateSimilaritybMetrics(reference_data,trial_data_C,metadata)
    
    max_score=max(score_A,score_B,score_C)
    if max_score==score_A:
        print("trial_data_A is best synthetic version of refrence dataset")
    elif max_score==score_B:
        print("trial_data_B is best synthetic version of refrence dataset")
    elif max_score==score_C:
        print("trial_data_C is best synthetic version of refrence dataset")



