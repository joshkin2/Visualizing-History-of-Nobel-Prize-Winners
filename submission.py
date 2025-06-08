# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')
nobel = pd.read_csv('data/nobel.csv')

print(f"The most common gender and birth country are {nobel['sex'].value_counts().index[0]} and {nobel['birth_country'].value_counts().index[0]}.")
top_gender = 'Male'
top_country = 'United States of America'

nobel['usa_native']= nobel['birth_country']=='United States of America'
nobel['decade']=np.floor(nobel['year']/10)*10
nobel['decade']=nobel['decade'].astype(int)
df_n=nobel.groupby('decade',as_index=False)['usa_native'].mean()
max_decade_usa=df_n[df_n['usa_native']==df_n['usa_native'].max()]['decade'].values[0]

nobel['female_winner'] = nobel['sex'] == 'Female'
df_female = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()
max_female_dict = {
    df_female[df_female['female_winner'] == df_female['female_winner'].max()]['decade'].values[0]: df_female[df_female['female_winner'] == df_female['female_winner'].max()]['category'].values[0]
}
max_female_dict

new_df = nobel[nobel['female_winner']]
min_row = new_df[new_df['year'] == new_df['year'].min()]
first_woman_name, first_woman_category = min_row['full_name'].values[0], min_row['category'].values[0]
print(first_woman_name)
print(first_woman_category)

repeat_winners = pd.DataFrame(nobel['full_name'].value_counts()).reset_index()
repeat_winners.columns = ['full_name', 'count']
repeat_list = list(repeat_winners[repeat_winners['count'] >= 2]['full_name'])
repeat_list
