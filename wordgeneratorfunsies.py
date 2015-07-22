# Zachary Lee, Lab 2

from goody import read_file_values
from goody import safe_open
import prompt
from collections import defaultdict
import random

def read_corpus(n: int, file) -> dict:
    file_iterator = read_file_values(file)
    
    preread_list = []
    corpus = defaultdict(list)
    
    for i in range(n):
        preread_list.append(file_iterator.__next__())
    
    for word in file_iterator:
        if word not in corpus[tuple(preread_list)]:
            corpus[tuple(preread_list)].append(word) 
        preread_list.remove(preread_list[0])
        preread_list.append(word)
        
    return corpus


def print_corpus(d: dict) -> None:
    print('Corpus')
    
    for key, value in sorted(d.items(), key = (lambda x: x[0])):
        print('  {} can be followed by any of {}'.format(key, value))
        
    values_sorted_by_length = sorted(d.values(), key = (lambda x: len(x)))
    print('min/max = {}/{}'.format(len(values_sorted_by_length[0]), len(values_sorted_by_length[-1])))


def produce_text(d: dict, starting_words: list, generate_count: int) -> list:
    current = starting_words[:]
    generated = starting_words[:]
    
    for i in range(generate_count):
        try:
            new = random.choice(d[tuple(current)])
            generated.append(new)
            current.pop(0)
            current.append(new)
        except IndexError:
            generated.append(None)
            break
        
    return generated
    




order_statistic = prompt.for_int('Enter order statistic', is_legal = lambda x: x>0)

file = open('thisisawesome.txt', 'r', encoding = 'utf-8')

corpus = read_corpus(order_statistic, file)

# print_corpus(corpus)

print('Enter {} words to start with'.format(order_statistic))

starting_words = []
for i in range(order_statistic):
    starting_words.append(prompt.for_string('Enter word {}'.format(i+1)))
    
words_to_generate = prompt.for_int('Enter # of words to generate', is_legal = (lambda x: x > 0))
    
generated_text = produce_text(corpus, starting_words, words_to_generate)

for i in range(int(len(generated_text)/10)):
    print(' '.join(generated_text[10*i:10*(i+1)]))

file.seek(0)
