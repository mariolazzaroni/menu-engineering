import pandas as pd
dataset = pd.read_csv('data_set_bar.csv')
dataset.info
dataset.isnull().sum()
dataset.duplicated().sum()
dataset = dataset.drop_duplicates()
dataset.to_csv('cleaned_datset_bar.csv', index = False)