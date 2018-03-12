import pandas as pd
import numpy as np
dc_listings = pd.read_csv('dc_airbnb.csv')

# [3723 rows x 19 columns]
# there are some missing values for bedrooms, bathrooms & beds
# print(dc_listings.describe())

# fetch a specific row
# print(dc_listings.iloc[0])

# define your accommodation
mine_accomodates = 3
# find the difference with the first listings
first_accommodates = dc_listings.iloc[0]['accommodates']
first_distance = np.abs(first_accommodates - mine_accomodates)
print('Simialrity with the first row: ' + str(first_distance) + '\n')

# compute the similarity metric for the rest of the browse

dc_listings['distance'] = dc_listings['accommodates'].apply(lambda x: np.abs(x - mine_accomodates))

# print frequncy table for the similarity metrics
# 461 listings have a distance 0
print('Frequency table:')
print(dc_listings['distance'].value_counts())

# LOOKUP ON RANDOMISATION Randomising and sorting
np.random.seed(1)
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
dc_listings = dc_listings.sort_values('distance')
print(dc_listings.iloc[0:10]['price'])
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
mean_price = dc_listings.iloc[0:5]['price'].mean()
print(mean_price)
