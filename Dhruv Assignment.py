
# coding: utf-8

# In[7]:


import glob
from textblob import TextBlob # We use this library to find the sentiment score
import numpy as np


# In[3]:


path = 'C:/Users/Dhruv/Desktop/Text files/*.txt'


# In[8]:


files = glob.glob(path)


# In[11]:


maleFiles = []
femaleFiles = []
for file in files:
    if 'fe' in file.lower() or 'she' in file.lower() or 'wom' in file.lower():
        femaleFiles.append(file)
    else:
        maleFiles.append(file)


# In[41]:


# Merging Male Data together
maleData = []
for i in range (len(maleFiles)):
       with open(maleFiles[i]) as file: 
           lines=[(line) for line in (file)]
           if len(lines) == 1:              
               pass
           else:
               maleData.extend(lines)


# In[42]:


# Merging Female Data together
femaleData = []
for i in range (len(femaleFiles)):
        with open(femaleFiles[i]) as file: 
            lines=[(line) for line in (file)]
            if len(lines) == 1:              
                pass
            else:
                femaleData.extend(lines)


# In[58]:


# The overall merged data
data = maleData + femaleData


# In[51]:


# Getting the best and worst male sentiments
maleSentiment = []
for sentence in maleData:        
    maleSentiment.append(TextBlob(sentence).sentiment[0])
    
bestMale = maleData[np.argmax(maleSentiment)]
print(bestMale)

worstMale = maleData[np.argmin(maleSentiment)]
print(worstMale)


# In[52]:


# Getting the best and worst female sentiments
femaleSentiment = []
for sentence in femaleData:        
    femaleSentiment.append(TextBlob(sentence).sentiment[0])
    
bestFemale = femaleData[np.argmax(femaleSentiment)]
print(bestFemale)

worseFemale = femaleData[np.argmin(femaleSentiment)]
print(worseFemale)


# In[68]:


# Finding top 10 most common descriptions for characters

# Finding all the adjectives
adjectives = []
for i in range(len(data)):
    adjectives.extend(data[i].strip(' ').split(' ')[2:4])
Adjectives = ' '.join(adjectives)

# Counting the occurance of each adjective
descriptions = {}
for adjective in Adjectives.split(' '):
    if adjective in descriptions:
        descriptions[adjective] += 1
    else:
        descriptions[adjective] = 1

# taking the top 10 ones
topTenCommon = sorted(descriptions.items(), key=lambda x: x[1], reverse = True)[0:10]

print(topTenCommon)

