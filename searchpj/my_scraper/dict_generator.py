#!/usr/lib/python3
# -*- encoding: utf-8 -*-

import re
from collections import Counter
import random


def word_list(source_text):
    source_words = re.findall(r"[,\.-:;\?!]|\w+\b", source_text)
    counting_elements = Counter(source_words)
    string_of_elements = (" ".join(counting_elements))
    list_of_elements = re.findall(r"[,\.-:;\?!]|\w+\b", string_of_elements)
    return list_of_elements, source_words

def dictionary(list_of_elements, source_words):
    dictionary_of_repeats = {}
    for j, el in enumerate(list_of_elements):
        next_elements = []
        for i in range(len(source_words) - 1):
            if source_words[i] == list_of_elements[j]:
                next_elements.append(source_words[i + 1])
        key = list_of_elements[j]
        all_repeats = Counter(next_elements)
        frequent_repeats = dict(all_repeats.most_common(5))
        dictionary_of_repeats[key] = tuple(frequent_repeats)
    return dictionary_of_repeats

def text_generation(first_word, dictionary_of_repeats, text_len_lim):
    text_new = first_word
    start_txt = text_new
    step = 0
    while step < text_len_lim:
        for key, value in dictionary_of_repeats.items():
            if start_txt == key and len(value) > 0:
                value_num =  len(value)-1
                rand_value = random.randint(0, value_num)
                if not re.findall(r"[,\.-:;\?!]", value[rand_value]):
                    text_new += ' '
                text_new += value[rand_value]
                start_txt = value[rand_value]
        step += 1
    return text_new


if __name__ == '__main__':
    f = open('initial_text.txt', 'r', encoding='utf-8')
    source_text = f.read()
    f.close()
    list_of_elements, source_words = word_list(source_text)
    dictionary_of_repeats = dictionary(list_of_elements, source_words)
    first_elements = ('Она', 'Он', 'Только', 'Дом')
    first_word = random.choice(first_elements)
    text_len_lim = 35 # text length limit
    text_new = text_generation(first_word, dictionary_of_repeats, text_len_lim)
    print('dictionary_of_repeats ======', dictionary_of_repeats)
    #print('source_words ======', source_words)
    print("text_new: \n", text_new)


# Генератор учитывает после каких слов встречаются знаки препинания
# и вставляет их после соответствующих слов.
# Защита от зацикливания реализована в случайном выборе одного из
# 5 возможных наиболее частых следующих слов.
