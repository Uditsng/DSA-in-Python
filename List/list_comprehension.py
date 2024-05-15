#syntax: new_list = ['new_item' for 'item' in 'list']
prevList = [1,2,3,4]
newList = [newItem*2 for newItem in prevList]
print(newList)
print(prevList)

language = "Python"
newList = [letter for letter in language]
print(newList)

#instead of list, range is given
newMyList = [i*2 for i in range(0,5)]
print(newMyList)

for i in range(0,5):
    print(i*2)


'''Conditional list comprehension'''
#syntax: new_list = ['new_item' for 'item' in 'list' if 'condition']

'''1'''
main_list = [-10,-9,-8,-7,-6,1,2,3,4,5,6]
newList2 = [ newItem for newItem in main_list if newItem > 0]#printing only positive number
print(newList2)

'''2'''
newList3 = [ i**2 for i in main_list if i <               0]#taking sqr of negative number
print(newList3)

'''3'''
sentence = " My name is udit"

def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)