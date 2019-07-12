#from names_dataset import NameDataset
import string
import csv

#m = NameDataset()

first_names_array = []
last_names_array = []
word_list = set()
word_list_with_frequencies = set()

with open('census_names/yob1991.txt', 'r') as words:
    r = csv.reader(words, delimiter=',', quotechar='|')
    for row in r:
        #word_list.append(row[0])
        #word_list.add(row[0].lower())
        tup = ( row[0].lower(), int(row[2]) ) 
        word_list_with_frequencies.add( tup )

def init_array(arr):
    for i in range(26):
        arr.append([])
        for j in range(26):
            arr[i].append(0)
    return arr

first_names_array = init_array(first_names_array)
#last_names_array = init_array(last_names_array)

#for ind, name in enumerate(m.first_names):
# for ind, name in enumerate(word_list):
for ind, tup in enumerate(word_list_with_frequencies):

    if ind > 5000:
        break
    #print(name)
    #for i in range(len(name)-1):
    for i in range(len(tup[0])-1):
        #print(name[i] + name[i+1])
        try:
            #first_names_array[string.ascii_lowercase.index(name[i])][string.ascii_lowercase.index(name[i+1])] += tup[1]
            first_names_array[string.ascii_lowercase.index(tup[0][i])][string.ascii_lowercase.index(tup[0][i+1])] += tup[1]
        except ValueError:
            break

print(first_names_array)

with open('words.csv', 'w', newline='') as csvfile:
    w = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(first_names_array)):
        row = first_names_array[i]
        w.writerow(row)

print('done')
