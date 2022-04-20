import pandas as pd
import random


def load_wassa_dataset():
    train_data = pd.read_csv('./data/messages_train_ready_for_WS.tsv', sep='\t')
    dev_data = pd.read_csv('./data/messages_dev_features_ready_for_WS_2022.tsv', sep='\t')
    test_data = pd.read_csv('./data/messages_test_features_ready_for_WS_2022.tsv', sep='\t')
    return train_data, dev_data, test_data


def random_baseline_predictions(size:int, label_counts, seed=20):
    random.seed(seed)
    
    label_distribution = [] 
    for label, count in label_counts.items():
        for i in range(count):
            label_distribution.append(label)
            
            
    predictions = [random.choice(label_distribution) for i in range(size)]
    return predictions