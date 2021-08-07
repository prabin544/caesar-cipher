import nltk

# nltk.download('words', quiet=True)
# nltk.download('names', quiet=True)

# from nltk.corpus import words, names

# word_list = words.words()
# name_list = names.words()

# string = 'ok'
# word_count = 0
# if string in word_list or string in name_list:
#     word_count =+ 1
# else:
#     print('I am here')

string = "I am here"

def encrypt(string):
    print('Original String: ', string)
    list1 = list(string)
    num = []
    new_list = []
    str1 = ""
    for x in list1:
        num.append(ord(x)+3)
    # print(list1)
    # print(num)
    for x in num:
        new_list.append(chr(x))
    for ele in new_list:
        str1 += ele
    # print(new_list)
    print('Coverted String: ', str1.replace('#', ' '))


# def decrypt():
#     pass

encrypt(string)


