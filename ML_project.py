# Machine Learning - project 19.05.2022
# Analysis of the emotional marking of comments (sentiment of statement)
# Training data: http://ai.stanford.edu/~amaas/data/sentiment/
# Test data: user testing
# New main branch: 30.05.2022

import glob

POS_FILE = r'M03\data\aclImdb\train\pos\*.txt'
NEG_FILE = r'M03\data\aclImdb\train\neg\*.txt'

def remove_punctation(text):

    """
    Removing special characters from the given text.
    
    parametres:
        text;
    return:
        new text, without punctations.
    """

    SPECIAL_CHAR = '?.,!>~#*@()'

    comment = text.replace('<br />', ' ')
    comment_new = ''

    for char in comment:  
        if char in SPECIAL_CHAR:
            comment_new += char.replace(char,' ')
        else:
            comment_new += char
    
    return comment_new


def load_files(files):

    """ 
    Load files. Use glob module. Counting how many files the word is in.

    parameters: 
        files - indicate the path pattern that the function is to find using the glob module;
        dictonary - select an empty dictionary where the results will be saved;
    return: 
        dictonary
    """
    files = glob.glob(files)

    dictonary = {}
    for file in files:
        with open(file, encoding='utf8') as stream:
            content = stream.read()
            content_without_punctations = remove_punctation(content)
            words = content_without_punctations.lower().split()
            for word in set(words):
                dictonary[word] = dictonary.get(word, 0) + 1
    
    return dictonary


def count_sentiment(dictonary):

    """ 
    Counting the sentiment of individual words.
    
    parametres:
        dictonary - select a dictonary;
    return: 
        resonance of the word
    """

    if word in dictonary:
        resonance = dictonary[word]
    else:
        resonance = 0.0
    
    return resonance


def new_review(text):

    """
    Add new review.
    
    parametres:
        text - new review;
    return: 
        list of the words
    """

    sentence = remove_punctation(text)
    words = sentence.lower().split()

    return words


def final_raport(sentence_sentiment):

    """
    Print final raport.
    
    parametres:
        sentence_sentiment - total sentiment of the sentence
    print:
        information about sentiment of new review
    """

    if sentence_sentiment >0:
       label = 'positive'
    else:
        label = 'negative'
    print('---')
    print('This sentence is', label + ':', 'sentiment =', sentence_sentiment)


if __name__ == '__main__':
    
    pos_reviews = load_files(POS_FILE)
    neg_reviews = load_files(NEG_FILE)
    
    sentence = input('Podaj komentarz: ')
    words = new_review(sentence)

    sentence_sentiment = 0

    for word in words:
        positive = count_sentiment(pos_reviews)
        negative = count_sentiment(neg_reviews)

        all_ = positive + negative

        try:
            word_sentiment = (positive-negative)/all_
        except ZeroDivisionError:
            word_sentiment = 0.0

        print(word, word_sentiment)

        sentence_sentiment += word_sentiment

    sentence_sentiment /= len(words)

    final_raport(sentence_sentiment)
