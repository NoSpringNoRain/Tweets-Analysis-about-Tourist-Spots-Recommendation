import six
import sys
import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types



filelist=os.listdir('/Users/jackhu/Projects/GCP1/test_file')
print(filelist)
filenum=len(filelist)
for i in range(0,filenum):
    filename=filelist[i]
    review_file=os.path.join('/Users/jackhu/Projects/GCP1/test_file',filename)

    with open(review_file, 'r') as review_file:
# Instantiates a plain text document.
         text = review_file.read()

    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8','ignore')

    document = types.Document(
        content=text.encode('utf-8','ignore'),
        type=enums.Document.Type.PLAIN_TEXT)

# Detect and send native Python encoding to receive correct word offsets.
    encoding = enums.EncodingType.UTF32
    if sys.maxunicode == 65535:
        encoding = enums.EncodingType.UTF16

    result = client.analyze_entity_sentiment(document, encoding)

    for entity in result.entities:
        print('Mentions: ')
        print(u'Name: "{}"'.format(entity.name))
        for mention in entity.mentions:
            entity_type = enums.Entity.Type(entity.type)
            print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
            print(u'  Content : {}'.format(mention.text.content))
            print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
            print(u'  Sentiment : {}'.format(mention.sentiment.score))
            print(u'  Type : {}'.format(entity_type.name))
        print(u'Salience: {}'.format(entity.salience))
        print(u'Sentiment: {}\n'.format(entity.sentiment))