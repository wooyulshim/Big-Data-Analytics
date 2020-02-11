# Big-Data-Analytics Assignment 1 
## Python code for Sentimental Analysis


**Python Package**
- nltk

** Purpose of the code**
- This code is to do Sentimental Analysis and calucate the percentage of it. 
- The code imports excel fill that contains reviews of certain movie, and reviews were crawled from movie review site. 

## Function 

- [Import](#Import)
- [Define](#Define)
- [With Open](#With Open)
- [while Loop](#while Loop)


---

## Import

```python
// Import code

from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia
sourceFileName = '/Users/shimwooyul/Desktop/sentiment code/twintstuber.csv'
destinationFileName = '//Users/shimwooyul/Desktop/sentiment code/twintstuber2.csv'
```

---

## Define

```python
// Define

def polarPecent (review,total):
    percentage = review / total
    return '{0:,.2f}'.format(percentage)
```

---

## With Open

```python
// With Open

with open(sourceFileName, 'r', encoding ='utf8') as csvFile, open(destinationFileName, 'w', encoding = 'utf8') as reviewFile:
    line = csvFile.readline()
    line = csvFile.readline().replace('\n' ,'') 
    header = 'tweets \n'
    reviewFile.write(header)
```

---


## while loop

```python
// while loop

while line != '':
        try:
            lineList =line.split(',')
            tweets = lineList[10]
            outputline =  tweets + '\n'
            reviewFile.write(outputline)
            line = csvFile.readline().replace('\n' ,'')
            comment = tweets
            sid = sia()
            sentimentScores = sid.polarity_scores(comment)
            count +=1
        except SyntaxError: 
            print('No review found')
        if sentimentScores['compound'] > 0:
            countPos +=1
        elif sentimentScores['compound'] <0:
            countNeg +=1
        elif sentimentScores['compound'] ==00 :
            countNeu+=1
```

---


## Steps

> To get started...

### Step 1

- Scrawl data from review websit

### Step 2

- Input location of csv or excel file of scrawled data into sourceFileName

### Step 3

- Input destination file location into destinationFileName 

### Step 4

- run the code!
---
