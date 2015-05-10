
from sklearn.linear_model import LogisticRegression
from sklearn import svm
import pylab as pl
import numpy as np
from sklearn import cross_validation
from sklearn.grid_search import GridSearchCV
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

import json
import sys
import os

import matplotlib.pyplot as plt
from wordcloud import WordCloud

stopwords = ["&", "&amp;", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

tweets = [] #RAW, UNFILTERED TWEETS
for line in open('tweetDump.txt').readlines():
    tweets.append(line)

tweetsProcessed = [] #FILTERED TWEETS WITH STUFF LIKE STOPWORDS REMOVED
# Extract the vocabulary of keywords
# and put them into a dictionary
vocab = dict()
for eachTweet in tweets:
    filteredTweet = ""
    for term in eachTweet.split():
        term = term.lower()
		#filter removing terms under 2char, in stopwords, and links
        if len(term) > 2 and term not in stopwords and not term.startswith('http'):
            filteredTweet = filteredTweet + ' ' + term
            if vocab.has_key(term):
                vocab[term] = vocab[term] + 1
            else:
                vocab[term] = 1
    tweetsProcessed.append(filteredTweet)

# Remove terms whose frequencies are less than a threshold (e.g., 15)
vocab = {term: freq for term, freq in vocab.items() if freq > 20}
#sort of like x = x+1; term only gets added if its freq is > # in old vocab.items()

# Generate an id (starting from 0) for each term in vocab
vocab = {term: i for i, (term, freq) in enumerate(vocab.items())}

# Generate X
X = []
#basically, X = list of Ys
#Ys = counts of which words got hit in a single tweet instance
for text in tweets: #iterate through each tweet
    x = [0] * len(vocab) #x is now len(vocab) large
    #terms = list of terms that >2 in length in a tweet
    terms = [term for term in text.split() if len(term) > 2]
    for term in terms: # for each term in terms
        if vocab.has_key(term):
            x[vocab[term]] += 1 #increase that term's id by 1
    X.append(x)

################################################################################
numberOfClusters = 5

# K-means clustering
km = KMeans(n_clusters = numberOfClusters, n_init = 100) # try 100 different initial centroids
km.fit(X) #KMeans all those Ys

#make a directory for cluster files (if it doesn't exist already
subDirectory = "wordcloud"
if not os.path.exists( subDirectory ):
    os.makedirs( subDirectory )

#open cluster files for writing
clusterFilePtr = [] #set up cluster pointer array
for i in range(0, numberOfClusters):
    filename = "cluster" + str(i) + "_data.txt"
	#put categorized tweets in the subdirectory
    clusterFilePtr.append( open( os.path.join(subDirectory, filename), "w") )

counter = [] #counter for each cluster
for i in range(0, numberOfClusters):
    counter.append(0)

#write each tweet to the cluster file they belong to
for i, cls in enumerate(km.labels_):
    clusterFilePtr[cls].write( tweetsProcessed[i] + "\n" )
    counter[cls] += 1

#close cluster files
for eachPtr in clusterFilePtr:
    eachPtr.close()

print "Number of clusters:", len(counter)
#print count of each cluster
for i in range( 0, len(counter) ):
    print "cluster%d: %d" % (i, counter[i])


#####################################################wordcloud time
# get all the words from each cluster
for i in range(0, numberOfClusters):
	filename = "cluster" + str(i) + "_data.txt"
	wordball = []
	wordball = open(os.path.join(subDirectory, filename)).read()
	wc = WordCloud().generate(wordball)		#generate wordcloud
	picname = "cloud" + str(i) + ".png"
	wc.to_file(os.path.join(subDirectory, picname)) 	# store to file
