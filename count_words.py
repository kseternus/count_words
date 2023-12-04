import re


def countWords(string):
    string_list = re.split(r'[' ' \n`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?0123456789]', string)
    string_list = [i for i in string_list if i !='']
    count = {}
    for i in string_list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


txt_file = open('file.txt', 'r')
data = str(txt_file.read())
print(countWords(data))
