import numpy as np
import pandas as pd

def get_features(fname, feature_name):
    df = pd.read_csv(fname)
    return df[feature_name]



def get_data(fname, feature_name, class_file):
    df = get_features(fname, feature_name)
    classes = np.loadtxt(class_file)
    df['class'] = classes
    return df