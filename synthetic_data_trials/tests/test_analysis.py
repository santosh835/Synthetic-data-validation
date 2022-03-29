from sdv.evaluation import evaluate
import pandas as pd

real_data = pd.DataFrame({
    'Name': ['A','B','C','D','E'],
    'Age': [4, 5, 6, 7,8],
    'gender':['M','M','F','F','M'],
    'Salary':[200,500,300,100,400]
})

best_synthectic = pd.DataFrame({
    'Name': ['A','E','C','D','B'],
    'Age': [4, 8, 6, 7,5],
    'gender':['M','M','F','F','M'],
    'Salary':[200,500,300,100,400]
})


worst_synthetic = pd.DataFrame({
    'Name': ['A','E','C','D','B'],
    'Age': [10,3,9,4,12],
    'gender':['M','M','M','F','M'],
    'Salary':[20,50,30,10,40]
})


def test_quantitative_score_best_fit():
    score = evaluate(best_synthectic, real_data, metrics=['CSTest','KSTest'])
    if score>=0.9:
        print( "Best Fit")

def test_quantitative_score_worst_match():
    score = evaluate(worst_synthetic, real_data, metrics=['CSTest','KSTest'])
    if score<=0.9:
        print( "Worst Fit")
    
def test_evaluate_score_best_fit():
    score = evaluate(best_synthectic, real_data, metrics=['CSTest','KSTest','LogisticDetection','SVCDetection'])
    if score>=0.9:
        print(  "Best Fit")

def test_evaluate_score_worst_match():
    score = evaluate(worst_synthetic, real_data, metrics=['CSTest','KSTest','LogisticDetection','SVCDetection'])
    if score<=0.9:
        print( "Worst Fit")
    