import pandas as pd

vendite_bar = pd.read_csv('data_set_bar.csv')
vendite_bar.info
vendite_bar.isnull().sum()
vendite_bar.duplicated().sum()
vendite_bar = vendite_bar.drop_duplicates()
vendite_bar.to_csv('cleaned_datset_bar.csv', index = False)