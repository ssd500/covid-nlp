import re
import nltk
from nltk.corpus import stopwords 
nltk.download('stopwords')

def tolowercase(words):#converting to lowercase
    for i in range(len(words)):
        words[i]= words[i].lower()
    return words
        
def emoji(words):#removing emojis
    emo = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    for w in range(len(words)):
        words[w]=emo.sub(r'', words[w])
    return words
        
def removechar(words):#removing special characters
    specialchar = ["!",'"',"#","%","&","'","(",")",
              "*","+",",","-",".","/",":",";","<",
              "=",">","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–"]
    
    for c in specialchar:
        for w in range(len(words)):
            words[w] = words[w].replace(c, '')
    return words

def removelinks(words):#removing hyperlinks
    for i in range(len(words)):
        words[i] = re.sub(r'http\S+','',words[i])
    return words

def removecommon(words):#removing stopwords
    stop_words = list(stopwords.words('english'))
    for i in range(len(words)):
        for d in range(len(stop_words)):
            if(words[i]==stop_words[d]):
                words[i] = words[i].replace(stop_words[d],'')
    return words

def removeempty(words):#removing '' and ' '
    newwords = []
    for i in range(len(words)):
        if(words[i]!='' and words[i]!=' '):
            newwords.append(words[i])
    return newwords