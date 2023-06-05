# Задача №40
'''
import pandas as pd

df = pd.read_csv('sample_data/california_housing_test.csv')

df[df['population']<501]['median_house_value'].agg(['mean']
'''
# Задача №42
'''
import pandas as pd

df = pd.read_csv('sample_data/california_housing_test.csv')

df[df['population']==df['population'].min()]['households'].max()
'''