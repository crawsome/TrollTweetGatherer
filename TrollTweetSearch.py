# Goes through list and greps out queries and prints them all pretty
# CSV Source: https://github.com/fivethirtyeight/russian-troll-tweets/

import os
import re
import csv
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

print('Troll Tweet Grep:\n')
"""
Makes a word-occurrence chart based on search string

Input: query - str() - search query
"""
query = str(input('Please enter search string: '))

# collections
ourlist = next(os.walk('tweets/'))[2]
weight_dict = {}
tweetlist = []
authorlist = []
word_list = []
garbage_list = list(
    ['about', 'all', 'among', 'and', 'are', 'ass', 'because', 'become', 'but', 'can', 'could', 'don', 'dont', 'down',
     'for', 'from', 'fuck', 'fucked', 'fuckin', 'fucking', 'fucks', 'get', 'give', 'got', 'had', 'has', 'have', 'her',
     'hers', 'him', 'his', 'how', 'http', 'https', 'into', 'just', 'know', 'like', 'may', 'might', 'must', 'not', 'now',
     'off', 'one', 'out', 'say', 'shall', 'she', 'shit', 'should', 'some', 'still', 'that', 'the', 'their', 'their,',
     'them', 'then', 'there', 'these', 'they', 'this', 'three', 'two', 'up', 'want', 'was', 'wasnt', 'were', 'what',
     'when', 'where', 'who', 'why', 'will', 'with', 'without', 'would', 'you', 'your', 'than','lol','video','look'])
garbage_list.append(query)

# used for getting a sorted copy of the above text after you update it :)
# print(sorted(set(garbage_list)))


# Retrieving results section:
for tweetfile, index in zip(ourlist, range(0, len(ourlist))):
    print('Now searching through ' + str(tweetfile) + '...')
    with open('./tweets/' + str(tweetfile), encoding="utf8") as fin:
        dr = csv.DictReader(fin)
        for row in dr:
            if query.lower() in row['content'].lower():
                tweetlist.append(row['content'].lower())
                authorlist.append(row['author'].lower())
print(str(len(tweetlist)) + ' results found.')
garbage_list.append(authorlist)

"""ROWS FOR QUERYING YOURSELF
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
# for tweet, author in zip(tweetlist, authorlist):
#     print('Troll account name: ' + str(author))
#     print('Tweet: \n' + str(tweet) + '\n')

# turn all lists of all tweets into a big string
tweetlist = str(tweetlist)

# remove all whitespaces, and turn each word back into an array
tweetlist = re.findall(r'\w+', tweetlist)

for word in tweetlist:
    # print(word)
    ALREADY_IN_LIST = False
    try:
        if word.lower() not in weight_dict and len(word) > 2 and word.lower() not in garbage_list:
            weight_dict.update({word: 0})
        elif word.lower() in weight_dict:
            ALREADY_IN_LIST = True
            weight_dict[word] += 1
    except KeyError as e:
        # print('keyerror on: ' + str(word))
        # if ALREADY_IN_LIST:
        # print(str(word) + ' is already in the list')
        continue

weight_dict = dict(sorted(weight_dict.items(), key=itemgetter(1), reverse=True))
MAX_PLOTTED_VALS = 20
bar_width = 0.30
y = weight_dict.values()
x = weight_dict.keys()
max_x_range = np.arange(MAX_PLOTTED_VALS)
max_y = int(max(y)) if y else None
plt.xticks(np.arange(MAX_PLOTTED_VALS), x, rotation=45)
plt.ylabel('Most common words with \"' + str(query) + '\" in it')
plt.xlabel('Words')
plt.bar(np.arange(MAX_PLOTTED_VALS) + bar_width, list(y)[:MAX_PLOTTED_VALS], width=bar_width, facecolor='#9999ff',
        edgecolor='white')
fig = plt.gcf()
fig.canvas.set_window_title(str(MAX_PLOTTED_VALS) + ' most common words with \"' + str(query) + '\" in it')
plt.show()
