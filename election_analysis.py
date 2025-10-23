import pandas as pd
from pandasql import sqldf

total_df = pd.read_csv("US-2016-primary.csv", sep=";")

state_county_breakdown = sqldf('''
SELECT *, votes/fraction_votes AS "total_county_votes"
FROM total_df 
''')

state_totals = sqldf('''                               
SELECT state_abbreviation, SUM(total_county_votes) AS "total_state_votes"
FROM state_county_breakdown
GROUP BY state_abbreviation
''')

state_county_breakdown = sqldf('''
SELECT b.*, t.total_state_votes, b.total_county_votes/t.total_state_votes AS county_weighting
FROM state_county_breakdown b
LEFT JOIN state_totals t ON b.state_abbreviation = t.state_abbreviation
''')

print(state_county_breakdown)