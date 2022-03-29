from sdv.evaluation import evaluate

# evaluation score based on  CSTest,KSTest,LogisticDetection,SVCDetection
def evaluationMetrics(synthectic_data,real_data):
    return evaluate(synthectic_data, real_data, metrics=['CSTest','KSTest','LogisticDetection','SVCDetection'])
    

# evaluation score based on  CSTest,KSTest
def evaluationMetricsQunatitative(synthectic_data,real_data):
    return evaluate(synthectic_data, real_data, metrics=['CSTest','KSTest'])
    