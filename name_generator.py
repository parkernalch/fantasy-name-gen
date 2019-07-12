import csv
import string
from random import randint, random

def init_array(arr):
    for i in range(26):
        arr.append([])
        for j in range(26):
            arr[i].append(0)
    return arr

freq_array_firstname = init_array([])


with open('words.csv', newline='') as csvfile:
    r = csv.reader(csvfile, delimiter=',', quotechar='|')
    for i, row in enumerate(r):
        for j, num in enumerate(row):
            freq_array_firstname[i][j] = num

def Normalize(array):
    for i, row in enumerate(array):
        total = 0
        for j, element in enumerate(row):
            total += float(element)

        for j, element in enumerate(row):
            array[i][j] = round(float(element) / total, 4)
    return array

working_array = Normalize(freq_array_firstname)

with open('words.csv', 'w', newline='') as normfile:
    w = csv.writer(normfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(working_array)):
        row = working_array[i]
        w.writerow(row)

class Letter:
    def __init__(self, glyph, isVowel, isConsonant):
        self.glyph = glyph.lower()
        self.isVowel = isVowel
        self.isConsonant = isConsonant
        self.num = string.ascii_lowercase.index(self.glyph)

global alphabet
alphabet = [
    Letter('a', True, False),
    Letter('b', False, True),
    Letter('c', False, True),
    Letter('d', False, True),
    Letter('e', True, False),
    Letter('f', False, True),
    Letter('g', False, True),
    Letter('h', False, True),
    Letter('i', True, False),
    Letter('j', False, True),
    Letter('k', False, True),
    Letter('l', False, True),
    Letter('m', False, True),
    Letter('n', False, True),
    Letter('o', True, False),
    Letter('p', False, True),
    Letter('q', False, True),
    Letter('r', False, True),
    Letter('s', False, True),
    Letter('t', False, True),
    Letter('u', True, False),
    Letter('v', False, True),
    Letter('w', False, True),
    Letter('x', False, True),
    Letter('y', True, True),
    Letter('z', False, True),
]

def Map_Name(name):
    map = []
    for i in range(len(name)):
        global alphabet
        ind = string.ascii_lowercase.index(name[i])
        letter = alphabet[ind]

        if letter.isVowel and letter.isConsonant:
            map.append('b')
        elif letter.isVowel:
            map.append('v')
        else:
            map.append('c')
    return map

def Generate_Name(seed=''):
    name = seed
    name_length_min = 4
    name_length_max = 9
    name_length_rand = randint(name_length_min, name_length_max)
    map = Map_Name(name)
    global alphabet

    for i in range(name_length_rand - len(name)):
        #print(name, map)
        if i==0 and len(name)==0:
            l = alphabet[randint(0, 25)]
        else:
            l = Pick_Next(name, map)

        name += l.glyph

        if l.isVowel and l.isConsonant:
            map.append('b')
        elif l.isVowel:
            map.append('v')
        else:
            map.append('c')

    return name

def Pick_Next(name, map):
    #print('GO for Pick_Next')
    next_is_constant = False
    next_is_vowel = False
    if map[-2:] in [['v','v'], ['b','v'], ['v','b']]:
        next_is_constant = True
    elif map[-2:] in [['c','c']]:
        next_is_vowel = True
    elif len(name)==1 and map in [['v'], ['b']]:
        next_is_constant = True
    elif len(name)==1 and map in [['c'], ['b']]:
        next_is_vowel = True

    prev_letter_index = string.ascii_lowercase.index(name[-1:])

    while True:
        rand_letter = random()
        letter = ''
        total = 0
        for j in range(0, 25):
            total += working_array[prev_letter_index][j]
            if total >= rand_letter:
                global alphabet
                letter = alphabet[j]
                break
        #print(letter, type(letter))
        if letter != '':
            if letter.isVowel and not next_is_constant:
                break
            if letter.isConsonant and not next_is_vowel:
                break
    return letter

i = input()
while i != '0':
    split = i.replace(' ','').split(',')
    if len(split) > 1:
        for n in range(int(split[1])):
            print(Generate_Name(split[0]))
    else:
        print(Generate_Name(split[0]))
    i = input()

# i = input()
# while i!='0':
#     split = i.replace(' ','').split(',')
#     if len(split) > 1:
#         desired_name = split[1]
#         seed = split[0]
#     count = 0
#     while True:
#         if Generate_Name(seed) == desired_name:
#             print('Number of iterations: {}'.format(count))
#             break
#         else:
#             count += 1
#     i = input()
