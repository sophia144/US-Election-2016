import pandas as pd
from pandasql import sqldf
import matplotlib.pyplot as plt 

total_df = pd.read_csv("US-2016-primary.csv", sep=";")

#adds up all votes in whole df for each state
total_df['total_votes_state'] = total_df.groupby('state')['votes'].transform('sum')

#filters for one candidate
candidate_name = "Donald Trump"
candidate_df = total_df[total_df['candidate'] == candidate_name]
candidate_df['candidate_votes_state'] = candidate_df.groupby('state')['votes'].transform('sum')
#calculates fraction of votes for that candidate in each state
candidate_df['candidate_state_fraction'] = candidate_df['candidate_votes_state'] / candidate_df['total_votes_state']
candidate_df = candidate_df.drop_duplicates(subset=['state', 'state_abbreviation', 'total_votes_state', 'candidate_votes_state', 'candidate_state_fraction', 'party']).reset_index(drop=True)

#sort by fraction of votes
candidate_df.sort_values(by=['candidate_state_fraction'], ascending=False, inplace=True)

#creating bar chart
x_axis = candidate_df['state_abbreviation']
y_axis = candidate_df['candidate_state_fraction']*100

#responsive colors
party = candidate_df['party'].iloc[0]
if party == "Democrat":
    bar_color = 'cornflowerblue'
elif party == "Republican":
    bar_color = 'red'
else:
    bar_color = 'silver'

#formatting
plt.figure(figsize=(12,5))
plt.bar(x_axis, y_axis, color=bar_color)
plt.title(f'Votes for {candidate_name} by State')
plt.xlabel('State')
plt.ylabel('Percentage of Votes')
plt.xticks(rotation=90)
plt.show()