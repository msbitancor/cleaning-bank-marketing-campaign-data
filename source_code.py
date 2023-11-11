import pandas as pd
import numpy as np

# Start coding here...

# Read csv data
data = pd.read_csv("bank_marketing.csv")

# Create client DataFrame
client = data[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']]

# Create campaign DataFrame
campaign = data[['client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts', 'previous_outcome', 'campaign_outcome']]

# Create economics DataFrame
economics = data[['client_id', 'cons_price_idx', 'euribor_three_months']]

# --------------------- CLEAN CLIENT DATA ---------------------

# Replace . with _ and unknown with NaN
client['education'] = client['education'].str.replace('.', '_')
client.loc[client['education'] == 'unknown', 'education'] = np.nan
client['job'] = client['job'].str.replace('.', '')

# Change Datatype to boolean
client[['credit_default', 'mortgage']] = client[['credit_default', 'mortgage']].astype(bool)

# -------------------- CLEAN CAMPAIGN DATA --------------------

# Change values to boolean values
campaign['campaign_outcome'] = campaign['campaign_outcome'].map({'yes': True, 'no' : False})
campaign['previous_outcome'] = campaign['previous_outcome'].map({'success': True, 'failure' : False, 'nonexistent' : False})

# Change datatype to bool
campaign[['campaign_outcome', 'previous_outcome']] = campaign[['campaign_outcome', 'previous_outcome']].astype(bool)

# Create last_contact_date column

# Create day, month, year columns
campaign['day'] = data['day'].astype(str)
campaign['month'] = data['month'].str.capitalize()
campaign['year'] = '2022'

# Pass to variables
day = campaign['day']
month = campaign['month']
year = campaign['year']

# Create date column to be prepared for formatting
campaign['date'] = year + '-' + month + '-' + day

# Pass to the desired column
campaign['last_contact_date'] = pd.to_datetime(campaign['date'], format='%Y-%b-%d')

# Drop tentative columns
campaign.drop(columns=['day', 'month', 'year', 'date'], inplace=True)

# ------------------- SAVE DATAFRAMES AS CSV -------------------

client.to_csv('client.csv', index=False)
campaign.to_csv('campaign.csv', index=False)
economics.to_csv('economics.csv', index=False)