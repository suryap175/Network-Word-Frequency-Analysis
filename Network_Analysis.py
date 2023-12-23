# -*- coding: utf-8 -*-
"""G61- FDA- Project3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fwyUHKbWraGVbWa0Nt4N8_rX97zaxVgs

## **FDA Project- 3**
# **Submission: 12/15/2022**
# **Surya Pratap Singh**

# **Task-1**
"""

#importing libraries
!pip uninstall networkx -y
!pip install networkx==2.4
# downgrading to networkx to avoid any conflict with scipy version
import numpy as np #importing numpy
import pandas as pd #importing pandas
import matplotlib.pyplot as plt #importing matplotlib for graph visualization
import networkx as nx #importing networkx for network analysis

from google.colab import files #uploading files from local
uploaded=files.upload() ##uploading files from local

keyword_network_analysis = pd.read_csv('Keyword.csv') #reading the dataset
keyword_network_analysis.index+=1 #incrementing the index by 1 because by default the index are generated from 0
keyword_network_analysis #displaying the raw dataset which is unfiltered.
#In the next segment, dataset is refined.

keyword_network_analysis.dropna(subset=['Keyword 1'], inplace = True) #removing null values beginning from column 1, because while checking, automatically it checks from column 1.
#Thus, susbet is keyword 1
keyword_network_analysis #displaying the refined data after dropping null values

keyword_data = keyword_network_analysis.set_index('Title').T.to_dict('list') #new variable named keyword_data which performs computation for the above refined data stored in keyword_network_analysis

analysis = keyword_network_analysis.iloc[:,1:] #new variable named analysis which stores keyword_network_analysis beginning from column 1

analysis.iloc[0,:] #location

keywords_unique = [] #new variable named keywords_unique to store empty list
for columns in analysis:#for loop to iterate a new variable named columns based on analysis- which stores the computation for the refined data
  for key in analysis[columns].dropna(): #for loop to iterate a new variable named key based on analysis and removing null
    if key not in keywords_unique: #if condition to check whether key is not in keywords_unique
      keywords_unique.append(key) #if key is not present in keywords_unique, then append key and keywords_unique

adjacency_matrix = np.zeros((len(keywords_unique), len(keywords_unique)), dtype = int) #new variable named adjacency_matrix to calculate adjacency_matrix on length of keywords_unique

for i in range(0, 248): #for loop to iterate i in range 0 to 248
  for j in range(0, 248): #for loop to iterate j in range 0 to 248
    if i != j : #if condition to check i is not equal to j
      if (adjacency_matrix[i][j] == 0) and (adjacency_matrix[j][i] == 0) : #if condition to check if adjacency_matrix[i][j] is equal to 0 and also adjacency_matrix[j][i] equals 0
        for t in keyword_data.keys():#for loop to iterate t in keyword_data
          if (keywords_unique[i] in (keyword_data[t])) and (keywords_unique[j] in (keyword_data[t])):#if condition to operate for keywords_unique[i] and keywords_unique[j] based on keyword_data[t]
            adjacency_matrix[i][j] = adjacency_matrix[i][j] + 1 #computing adjacency matrix
            adjacency_matrix[j][i] = adjacency_matrix[j][i] + 1 #computing adjacency matrix

name_columns= keywords_unique #new variable named name_columns which stores keywords_unique
name_rows= keywords_unique #new variable named name_rows which stores keywords_unique

weighted_network = nx.from_numpy_matrix(adjacency_matrix, parallel_edges=False) #new variable named weighted_network to read adj. matrix and compute the weighted network

plt.figure(figsize=(40,25)) #defining size of the plot
graph_position = nx.spring_layout(weighted_network) #new variable named graph_position that represents the position of the weighted_network
graph_edges = weighted_network.edges() #new variable named graph_edges that represents the edges of the weighted_network
nx.draw_networkx_nodes(weighted_network, graph_position, node_size=25, node_color='magenta', alpha=0.6) #drawing the network based on nodes having weighted_network, position of graph, color and size of node and aplha
nx.draw_networkx_edges(weighted_network, graph_position,width=0.5) #drawing the network based on edges having weighted_network, position of graph, and width
nx.draw_networkx_labels(weighted_network, graph_position, font_size=7, font_family='monospace',font_color='orange') #drawing the network based on labels having weighted_network, position of graph, color and size of node and aplha
plt.show() #displaying the network graph

node_degree = weighted_network.degree() #new variable named node_degree that stores degree of weighted_network
strength_compute = weighted_network.degree (weight = 'weight') #new variable named strength_compute that holds weighted_network.degree (weight = 'weight')

#computing degree
columns= ['TotalNodes', 'Degree'] #passing nodes and degree to columns
df_for_degree = pd.DataFrame(node_degree, columns = columns) #creting new dataframe that stores node_degree
df_for_words = pd.DataFrame(keywords_unique, columns = ['Keywords']) #creting new dataframe that stores keywords_unique having columns keywords
df_degwords = pd.merge(df_for_words, df_for_degree, left_index=True, right_index=True) #merging both the dataframes and assigning it to a new variable named df_degwords
df_degwords[['Keywords','Degree']].sort_values(by =['Degree'], ascending=False).head(10) #displaying the merged dataframe and sorting by values for top 10 nodes

#computing strength
df_strength = pd.DataFrame(strength_compute, columns = ['TotalNodes', 'Strength']) #creting new dataframe that stores strength_compute
df_res = pd.merge( df_degwords, df_strength, how="inner", on=['TotalNodes']) #merging both the dataframes( df_degwords,df_strength) and assigning it to a new variable named df_res
df_res[['Keywords','Strength']].sort_values(by =['Strength'], ascending=False).head(10) #displaying the merged dataframe and sorting by values for top 10 nodes

feature_data = pd.DataFrame() #new dataframe named feature_data to add the final data
for i in range(0, 248): #for loop to iterate i from range 0 to 248
  for j in range(0, 248): #for loop to iterate j from range 0 to 248
    if weighted_network.get_edge_data(i, j): #if condition to check for weighted_network.get_edge_data(i, j)
      data_row = { #new variable named data_row
          'Nd1': int(i), #working for node 1
          'Nd2': int(j), #working for node 2
          'Keyword-1':df_degwords.iat[int(i),0], #working for keyword 1
          'Keyword-2':df_degwords.iat[int(j),0], #working for keyword 2
          'Total_Weight': weighted_network.get_edge_data(i,j)['weight'] #computing total weight
      }
      feature_data=feature_data.append(data_row,ignore_index=True) #appending feature_data and data_row

feature_data[['Keyword-1','Keyword-2','Total_Weight']].sort_values(by='Total_Weight', ascending=False).head(10) #displaying the dataframe based on weights for keyword 1 and keyword 2

feature_data_res = pd.merge( df_for_degree, df_strength, how="inner", on=['TotalNodes']) #merging df_for_degree and df_strength on nodes and assigning it to a new variable named feature_data_res
final = feature_data_res[['Degree','Strength']].groupby('Degree').mean().reset_index() #new variable named final which stores feature_data_res[['Degree','Strength']] and grouping based on degree.
final.index+=1 #incrementing the index by 1
final #displaying the degree and the strength, based on which the final graph will be plotted.

#plotting the graph
plt.figure(figsize=(10,8)) #defining size of the plot
plt.title('Analysis of Degree vs Average Strength') #assigning the title to the graph plot
plt.xlabel('Degree') #title for x axis
plt.ylabel('Average Strength') #assigning title for y axis
plt.scatter(final['Degree'], final['Strength']) #scatter plot, passing final['Degree'] on x axis and final['Strength'] on y axis
plt.show() #displaying the graph

"""# **Task 2**"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
import seaborn as sns
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords

##############################
# since the 2020 file has data from 2016 to 2020, we are reading the files starting from 2020 till 2022
##############################

ti=[]
for i in range(2020,2023):
  path = str(i) + ".csv"
  fd = pd.read_csv(path)

  ti.append(fd)

  frame = pd.concat(ti, axis=0, ignore_index=True)

df=frame.copy() # create a copy of dataframe to work on

df = df.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii')) # remove emojis
df['tweet'] = df['tweet'].str.replace('(\@\w+.*?)',"") # remove all the mentions of accounts
df["tweet"] = df["tweet"].str.replace(r'\s*https?://\S+(\s+|$)', ' ').str.strip() # remove links starting with https
df["tweet"] = df["tweet"].str.replace(r'\s*http?://\S+(\s+|$)', ' ').str.strip()  # remove links starting with http
df['tweet'] = df['tweet'].str.replace('(\#\w+.*?)',"") # remove all hashtag mentions
df['tweet'] = df['tweet'].str.replace(r'[^\w\s]+', '') # remove all the remaining special characters
df['tweet'] = df['tweet'].str.replace('amp','') # remove amp word for &
df['tweet'] = df['tweet'].str.strip() # remove any empty spaces

# since the file 2020 has objects from 2016, we are filtering the data as per the question
df['year'] = pd.DatetimeIndex(df['date']).year
df = df.loc[df['year'] > 2016]

# remove stop words
stop = stopwords.words('english')
df['tweet'] = df['tweet'].apply(lambda x: ' '.join([word.lower() for word in x.split() if word.lower() not in (stop)]))

# removing any empty lines based on the tweet column
df['tweet'] = df['tweet'].replace(r'^s*$', float('NaN'), regex = True)
df.dropna(subset=['tweet'], inplace=True)

df1=df[['year','tweet']]
df1.tweet=df1.tweet.map(nltk.word_tokenize).tolist() # tokenize tweets
df1

df2 = df1.explode('tweet') # separating all the tweets to rows
df2

# calculating top 10 words for each year

df2['num'] = 1
df3 = df2.groupby(['year','tweet'],as_index=False)['num'].sum()

fi=[]
for i in range(2017,2023):

  dtf = df3.loc[df3['year'] == i]
  dtf = dtf.sort_values(by=['num'],ascending = False)
  dtf = dtf.head(10)
  fi.append(dtf)

  top10 = pd.concat(fi, axis=0, ignore_index=True)

top10.sort_values(by=['year','num'],ascending=False) # print top 10 words

# plot histogram for each year

for i in range(2017,2023):
  dat = df3.loc[df3['year'] == i]
  sns.histplot(data = dat, x = "num",bins= range(0,100,10))
  plt.title("Histogram for frequency of words for the year - " + str(i),fontweight="bold", fontsize=15)
  plt.show()

df5 = df3.copy()

df5['rank'] = df5.groupby(['year'])['num'].rank(ascending=False,method='first')
df5.sort_values(by=['year','num'],ascending=False)

# calculating total word frequency of each year
df6 = df3.groupby(['year'],as_index=False)['num'].sum()
df6 = df6.rename(columns={'num': 'total'})
df6

df7 = df5.merge(df6,on=['year'],how='left') # add the total count to each word
df7['term frequency'] = df7['num'] / df7['total'] # calculate term frequency by zipf's law

df7

# scalling to rank and term frequency to log
df8=df7.copy()
df8['log_tf'] = np.log(df8['term frequency'])
df8['log_rank'] = np.log(df8['rank'])

# plot log-log plots of word frequencies and rank for each year
sns.set(rc={'figure.figsize':(11,11)})
sns.lineplot(data = df8,x='log_rank',y="log_tf", hue = 'year',palette='hls')
plt.title(' log-log plots of word frequencies and rank for each year',fontweight="bold")
plt.show()

gram=df[['year','tweet']]
gram['bigrams'] = df1['tweet'].apply(lambda x: list(nltk.ngrams(x,2))) # calculating bigrams

bic = gram[['year','bigrams']]
bic = bic.explode('bigrams') # separate the bigrams to different rows
bic.dropna(subset=['bigrams'],inplace=True) # dropping any empty rows

# plotting bigram network graphs for each year
def networkgraph(thresh,year):

  bic3 = bic.loc[bic['year'] == year] # filter on  year
  bic3 = bic3[['bigrams']]

  bic3.reset_index(drop=True, inplace=True)
  bic4 = pd.DataFrame(bic3["bigrams"].to_list(), columns=['word1', 'word2']) # separating the bigrams to different columns
  bic4['num'] = 1
  bic4 = bic4.groupby(['word1','word2'],as_index=False)['num'].sum() # count pairs

  bic4.sort_values(by='num',ascending=False)
  bic4 = bic4.loc[bic4['num'] >=thresh] # consider pairs with count more than threshold
  G = nx.from_pandas_edgelist(bic4,source='word1',target='word2') # create graph from dataframe

  plt.figure(figsize=(40,30)) # set figure size
  nx.draw(G,with_labels= True) # plot the graph

networkgraph(2,2017) # network graph for year 2017

networkgraph(2,2018) # network graph for year 2018

networkgraph(2,2019) # network graph for year 2019

networkgraph(2,2020) # network graph for year 2020

networkgraph(2,2021) # network graph for year 2021

networkgraph(2,2022) # network graph for year 2022