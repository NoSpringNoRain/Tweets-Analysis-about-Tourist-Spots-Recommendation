import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

client = language.LanguageServiceClient()
filelist=os.listdir('/Users/jackhu/Projects/GCP1/test_file')#make sure no DS.Store file includes in the folder
print(filelist)
filenum=len(filelist)
sequence={}
M=0
for i in range(0,filenum):
    filename=filelist[i]
    review_file=os.path.join('/Users/jackhu/Projects/GCP1/test_file',filename)
    name=(os.path.splitext(filename)[0])
    with open(review_file, 'r') as review_file:
# Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    # Print the results
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    '''for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))
    '''
    sequence[name]=score #save the popular list
    print('Overall Sentiment of {}: score of {} with magnitude of {}'.format(
        name, score, magnitude))

sortedsequence=(sorted(sequence.items(), key=lambda x: x[1]))
b = [i[0] for i in sortedsequence]
result=open('/Users/jackhu/Projects/GCP1/result.txt','a')
result.write('Top 10 US cities most welcome on Twitter for a short trip'+'\n')
for n in range(0,9):
    result.write (str(n+1)+'.'+b[n]+'\n')