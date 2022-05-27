def pal(word):
    if word == word[::-1]:
        print('palindrom')
    else:
        print(':(')

wrd = input('Enter word: ')
print(pal(wrd))