from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia
sourceFileName = '/Users/shimwooyul/Desktop/sentiment code/twintstuber.csv'
destinationFileName = '//Users/shimwooyul/Desktop/sentiment code/twintstuber2.csv'
count = 0
countPos = 0
countNeg = 0
countNeu = 0

def polarPecent (review,total):
    percentage = review / total
    return '{0:,.2f}'.format(percentage)
#Learned this code from class
with open(sourceFileName, 'r', encoding ='utf8') as csvFile, open(destinationFileName, 'w', encoding = 'utf8') as reviewFile:
    line = csvFile.readline()
    line = csvFile.readline().replace('\n' ,'') 
    header = 'tweets \n'
    reviewFile.write(header)
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
    print('count =', count)
    print('Positive = ', countPos)
    print('Negative = ', countNeg)
    print('Neutral = ', countNeu)
posPer = polarPecent (countPos, count)
negPer = polarPecent (countNeg, count)
neuPer = polarPecent (countNeu, count)
print('Positive Percentage=', posPer)
print('Negative Percentage=', negPer)
print('Neutral Percentage=', neuPer)