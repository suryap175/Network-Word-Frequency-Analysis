# Twitter Data Analysis and Network Visualization
## Overview
This project encompassed the extraction and analysis of keyword data from various texts, resulting in the creation of a weighted adjacency matrix. The matrix facilitated the construction and examination of a weighted network. Additionally, the project analyzed Elon Musk's Twitter data from 2017-2022, applying various text analysis techniques to identify word usage trends and network dynamics.

## Key Contributions
**Keyword Extraction and Adjacency Matrix Construction:** Leveraged natural language processing (NLP) techniques to extract keywords from textual data. Converted the extracted keywords into a weighted adjacency matrix, representing the co-occurrence and relationships between keywords. This matrix enabled the quantification of connections between nodes (keywords) based on their co-occurrence frequency.

**Network Analysis and Visualization:** Utilized the adjacency matrix to construct a weighted network. Computed key network metrics, including node degree (number of connections) and node strength (sum of edge weights). Identified and visualized the top 10 nodes by degree and strength, highlighting the most influential keywords. Also, determined the top 10 node pairs by edge weight, illustrating the strongest keyword associations.

**Elon Musk Twitter Data Analysis:** Analyzed tweets from Elon Musk between 2017 and 2022, treating each year as a separate document. Conducted word frequency analysis to exclude common stop words and identify the most frequently occurring terms. Plotted histograms of word frequencies for each year, illustrating the distribution of word usage. Applied Zipf's law to analyze the rank-frequency relationship, generating log-log plots to demonstrate the power-law distribution of word frequencies. Created bigram network graphs to visualize the relationships between word pairs.

## Tools and Technologies
#### Programming Languages: Python
#### Analysis Techniques: Keyword Extraction, Word Frequency Analysis, Network Analysis, Zipf's Law
#### Frameworks and Libraries: NetworkX, Matplotlib, NLTK, Pandas, NumPy
#### Skills: Python Programming, Data Analysis, Natural Language Processing, Network Analysis, Data Visualization
## Objectives
**Keyword Data Processing:** Extract and transform keyword data into a structured format suitable for network analysis.
**Network Characterization:** Analyze the weighted network to identify key nodes and relationships, using degree and strength as primary metrics.
**Social Media Data Analysis:** Examine word frequency patterns and relationships in Elon Musk's tweets, employing various NLP and visualization techniques.
## Results
1. Comprehensive Keyword Network: Successfully extracted keywords and constructed a weighted adjacency matrix, leading to the visualization of a comprehensive keyword network. Identified and ranked keywords based on their connectivity and influence within the network.
2. Insightful Network Metrics: Calculated node degree and strength, uncovering the most influential keywords and the strongest keyword associations. Visualized these metrics to provide a clear understanding of the network's structure and key components.
3. In-depth Twitter Analysis: Revealed key trends and patterns in Elon Musk's Twitter data. Demonstrated the power-law distribution of word frequencies using Zipf's law. The bigram network graphs provided a visual representation of common word pairs, offering insights into common topics and phrases in the tweets.

## Conclusion
This project effectively demonstrated the application of advanced natural language processing and network analysis techniques to extract, analyze, and visualize keyword data. The construction of a weighted adjacency matrix and the subsequent analysis provided a robust framework for understanding complex keyword relationships. The examination of Elon Musk's Twitter data, including the application of Zipf's law and bigram network graphs, highlighted significant linguistic patterns and trends. This work underscores the potential of combining NLP and network analysis to gain deep insights into textual data.
