import pandas as pd
import matplotlib.pyplot as plt 

total_df = pd.read_csv("US-2016-primary.csv", sep=";")

#add up all votes in whole df for each state
total_df['total_votes_state'] = total_df.groupby('state')['votes'].transform('sum')

#filter for one candidate
candidate_name = "Donald Trump"
candidate_df = total_df[total_df['candidate'] == candidate_name]
#add up votes in each state for that candidate
candidate_df['candidate_votes_state'] = candidate_df.groupby('state')['votes'].transform('sum')
#calculate fraction of votes for that candidate in each state
candidate_df['candidate_state_fraction'] = candidate_df['candidate_votes_state'] / candidate_df['total_votes_state']
#drop duplicates to have one row per state
candidate_df = candidate_df.drop_duplicates(subset=['state', 'state_abbreviation', 'total_votes_state', 'candidate_votes_state', 'candidate_state_fraction']).reset_index(drop=True)

#creating bar chart
x_axis = candidate_df['state_abbreviation']
y_axis = candidate_df['candidate_state_fraction']*100

plt.figure(figsize=(15,6))
plt.bar(x_axis, y_axis)
plt.title(f'Votes for {candidate_name} by State')
plt.xlabel('State')
plt.ylabel('Percentage of Votes')
plt.xticks(rotation=90)
plt.show()