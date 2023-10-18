# Machine Learning - project 19.05.2022
# Analysis of the emotional marking of comments (sentiment of statement)
# Training data: http://ai.stanford.edu/~amaas/data/sentiment/
# Test data: user testing
# New main branch: 30.05.2022

import glob
from string import punctuation
from typing import Dict, List

POS_FILE = r'pos/*.txt'
NEG_FILE = r'neg/*.txt'

def remove_punctation(text: str) -> str:
    """
    Removing special characters from the given text.
    """

    comment = text.replace('<br />', ' ')
    comment_new = ''

    for char in comment:  
        if char in punctuation:
            comment_new += char.replace(char,' ')
        else:
            comment_new += char
    
    return comment_new


def load_files(files: str) -> Dict[str, int]:
    """ 
    Load files. Use glob module. Counting how many files the word is in.
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


def count_sentiment(dictonary: Dict[str, int], word: str) -> int:
    """ 
    Get the numbers of individual words.
    """

    if word in dictonary:
        resonance = dictonary[word]
    else:
        resonance = 0
    
    return resonance


def new_review() -> List[str]:
    """
    Add new review.
    """

    text = input('Enter a review: ')
    sentence = remove_punctation(text)
    words = sentence.lower().split()

    return words


def final_raport(sentence_sentiment: float) -> None:
    """
    Print final raport.
    """

    if sentence_sentiment > 0:
       label = 'positive'
    else:
        label = 'negative'
    print('---')
    print('This sentence is', label + ':', 'sentiment =', sentence_sentiment)

def main() -> None:
    pos_reviews = load_files(POS_FILE)
    neg_reviews = load_files(NEG_FILE)

    words = new_review()
    sentence_sentiment = 0
    for word in words:
        positive = count_sentiment(pos_reviews, word)
        negative = count_sentiment(neg_reviews, word)

        all_ = positive + negative

        try:
            word_sentiment = (positive - negative) / all_
        except ZeroDivisionError:
            word_sentiment = 0.0

        print(word, word_sentiment)

        sentence_sentiment += word_sentiment

    sentence_sentiment /= len(words)
    final_raport(sentence_sentiment)


if __name__ == '__main__':
    main()
