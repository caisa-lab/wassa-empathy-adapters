from math import sqrt
from transformers import EvalPrediction
from scipy.stats import pearsonr as pearsonr_scipy
import numpy as np
from sklearn.metrics import f1_score, recall_score, precision_score


def pearsonr(x, y):
    """ this function provided by WASSA """
    to_round = 4
    """
    Calculates a Pearson correlation coefficient. 
    """

    assert len(x) == len(y), 'Prediction and gold standard does not have the same length...'

    xm = sum(x)/len(x)
    ym = sum(y)/len(y)

    xn = [k-xm for k in x]
    yn = [k-ym for k in y]

    r = 0 
    r_den_x = 0
    r_den_y = 0
    for xn_val, yn_val in zip(xn, yn):
        r += xn_val*yn_val
        r_den_x += xn_val*xn_val
        r_den_y += yn_val*yn_val

    r_den = sqrt(r_den_x*r_den_y)

    if r_den:
        r = r / r_den
    else:
        r = 0

    # Presumably, if abs(r) > 1, then it is only some small artifact of floating
    # point arithmetic.
    r = max(min(r, 1.0), -1.0)

    return round(r,to_round)



def calculate_pearson(gold, prediction):
    """ this function provided by WASSA """
    
    """
    gold/prediction are a list of lists [ emp pred , distress pred ]
    """
    # converting to float
    gold = [float(k) for k in gold]
    prediction = [float(k) for k in prediction]

    return pearsonr(gold, prediction)


def compute_pearsonr(p: EvalPrediction):
    preds = p.predictions[:, 0]
    pr, pval = pearsonr_scipy(p.label_ids, preds)
    return {"pearsonr": calculate_pearson(p.label_ids, preds), "pearsonr_scipy": pr, "pval": pval}
