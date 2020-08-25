from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

def split_dataset_by_brand(dataset):
    brands = set(dataset["Brand"])
    return { brand: dataset[dataset["Brand"] == brand] for brand in brands }

def reset_index(df):
    return df.reset_index(drop=True)

def shuffle_df(df):
    df.sample(frac=1)

def train_validate_test_split(df, train_percent=.8, validate_percent=.1, seed=None):
    np.random.seed(seed)
    df = reset_index(df)
    perm = np.random.permutation(df.index)
    m = len(df.index)
    train_end = int(train_percent * m)
    validate_end = int(validate_percent * m) + train_end
    print(train_end, validate_end, m)
    train = df.iloc[perm[:train_end]]
    validate = df.iloc[perm[train_end:validate_end]]
    test = df.iloc[perm[validate_end:]]
    return train, validate, test


def split_dataset(ds_by_brand, train=0.8,val=0.1,test=0.1):
    train = pd.DataFrame()
    val = pd.DataFrame()
    test = pd.DataFrame()
    
    for brand in ds_by_brand:
        tr,v,ts = train_validate_test_split(ds_by_brand[brand])        
        train = train.append(tr)
        val = val.append(v)
        test = test.append(ts)
    train = reset_index(train)
    val = reset_index(val)
    test = reset_index(test)
    return train,val,test