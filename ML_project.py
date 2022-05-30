# Machine Learning - project 19.05.2022
# Analysis of the emotional marking of comments (sentiment of statement)
# Training data: http://ai.stanford.edu/~amaas/data/sentiment/
# Test data: user testing

FOLDER_POS = r'M03\data\aclImdb\train\pos\*.txt'
FOLDER_NEG = r'M03\data\aclImdb\train\neg\*.txt'

import glob

files_positive = glob.glob(FOLDER_POS)
files_negative = glob.glob(FOLDER_NEG)

positive = []
negative = []

special_char = '?.,!>~#*@()'

def reviews(files_type, list):
    for file in files_type:
        with open(file,  encoding='utf8') as stream:
            comment = stream.read()
    
        comment = comment.replace('<br />', ' ') 

        comment_new = ''
        for char in comment:  
            if char in special_char:
                comment_new += char.replace(char,' ')
            else:
                comment_new += char
    
        comment = comment_new.lower()
        comment = comment.split(' ')
        list.append(comment)

reviews(files_positive, positive)
reviews(files_negative, negative)

# User statement:

user_review = input('Give a statement: ')

new_user_review = ''

for char in user_review:
    if char in special_char:
        new_user_review += char.replace(char, '')
    else:
        new_user_review += char

user_review = new_user_review.lower()
user_review = user_review.split(' ')

# Sentiment:

sum_pos = 0
sum_neg = 0
sum_sentiment = 0

for word in user_review:
    for statement in positive:
        if word in statement:
            sum_pos += 1

    for statement in negative:
        if word in statement:
            sum_neg += 1
    
    all_ = sum_pos + sum_neg

    if all_ != 0:
        word_sentiment = (sum_pos - sum_neg)/all_
    else: 
        word_sentiment = 0.0
    
    print(word, word_sentiment)
    sum_sentiment += word_sentiment
    sum_pos = 0
    sum_neg = 0


average_sentiment = sum_sentiment/len(user_review)

print('The sentiment of this statement is', average_sentiment)

if average_sentiment > 0:
    print('This statement is positive.')
elif average_sentiment < 0:
    print('This statement is negative.')
else:
    print('This statement is neutral.')
