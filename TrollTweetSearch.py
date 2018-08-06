# Goes through list and greps out queries and prints them all pretty
# CSV Source: https://github.com/fivethirtyeight/russian-troll-tweets/

import os
import csv

print('Troll Tweet Finder by Colin Burke:\n')
query = str(input('Please enter search string: '))

# collections
ourlist = next(os.walk('tweets/'))[2]
tweetlist = []
authorlist = []

# Retrieving results section:
for tweetfile, index in zip(ourlist, range(0, len(ourlist))):
    print('Now searching through ' + str(tweetfile) + '...')
    with open('./tweets/' + str(tweetfile), encoding="utf8") as fin:
        dr = csv.DictReader(fin)
        for row in dr:
            if query.lower() in row['content'].lower():
                tweetlist.append(row['content'])
                authorlist.append(row['author'])
print(str(len(tweetlist)) + ' results found.')

"""ROWS FOR QUERYING YOURSELF: 
          row['external_author_id'], 
          row['author'], 
          row['content'], 
          row['region'],
          row['language'], 
          row['publish_date'], 
          row['harvested_date'], 
          row['following'],
          row['followers'], 
          row['updates'], 
          row['post_type'], 
          row['account_type'],
          row['retweet'], 
          row['account_category'], 
          row['new_june_2018'])
          """

# Processing results section:
for tweet, author in zip(tweetlist, authorlist):
    print('Troll account name: ' + str(author))
    print('Tweet: \n' + str(tweet) + '\n')

