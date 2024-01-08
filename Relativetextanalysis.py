#imports the necessary libaries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
# Read words from love, fear and stop words files and splits the lines 
with open("roget-love", "r") as file:
    wlove = file.read().splitlines()
with open("roget-fear", "r") as file:
    wfear = file.read().splitlines()
with open("stopwords-big.txt", "r") as file:
    stopwords = file.read().splitlines()
# Clean up stopwords words by making lowercase, selecting certain length
stopwords = " ".join(stopwords).lower()
stopwords = re.findall(r'[^a-z0-9\s]+', stopwords)
 # Clean up love words by making lowercase, selecting certain length
wlove = " ".join(wlove).lower()
wlove = re.findall(r'[^a-z0-9\s]+', wlove)
 # Clean up fear words by making lowercase, selecting certain length
wfear = " ".join(wfear).lower()
wfear = re.findall(r'[^a-z0-9\s]+', wfear)
#makes a function to get the amount of love and fear words relative to the total words in text file
def text_analysis(text_file):
    with open(text_file, "r") as file:
        aus = file.read().lower()
        aus = re.findall(r'[^a-z0-9\s]+', aus)
        aus = [word for word in aus if word not in stopwords]
    total_words = len(aus)
    love_count = sum(1 for word in aus if word in wlove)
    fear_count = sum(1 for word in aus if word in wfear)
    love_relative = love_count /total_words
    fear_relative = fear_count /total_words

    return love_relative, fear_relative
#creates list to store data 
love_relative_counts = []
fear_relative_counts = []
book_titles=[]
#creates list of textfiles needed for this assignment 
texts = ["A-emma.txt", "A-mansfield.txt", "A-northanger.txt", "A-persuasion.txt", "A-pride.txt", "A-sense.txt", "C-afterdark.txt", "C-armadale.txt", "C-evilgenius.txt", "C-moonstone.txt", "C-noname.txt", "C-womanwhite.txt"]
#creates a for loop to appened data from function to list
for text_file in texts:
    love_rel, fear_rel = text_analysis(text_file)
    love_relative_counts.append(love_rel)
    fear_relative_counts.append(fear_rel)
    book_titles.append(text_file)
#creates plot and adds features to distinguish between files 
colors = plt.cm.tab20(np.linspace(0, 1, 12))
plt.figure(figsize=(10, 6))
plt.scatter(love_relative_counts, fear_relative_counts, marker='o', c=colors, label=text_file)
plt.xlabel('Counts of "Love" Words')
plt.ylabel('Counts of "Fear" Words')
plt.title('Relative Counts of "Love" and "Fear" Words in Different Books')
plt.grid(True)
for i, title in enumerate(book_titles):
    plt.annotate(title, (love_relative_counts[i], fear_relative_counts[i]))







