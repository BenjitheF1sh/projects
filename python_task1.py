def rishoni( first, last):
    for element in range(first, last):
        flag = True
        if element in (0,1):
            flag =False
        else:
            for num in range(2, element):
                if(element%num==0):
                    flag = False
        if(flag):
            print(element)

def polindrom(sentence):
    temp = sentence[::-1]
    for element in sentence:
        if(sentence.find(element)!=temp.find(element)):
            return False
    return True

def longestPhrase(sentence):
    max = 0
    longest = " "
    word_list = sentence.split()
    for word in word_list:
        if len(word) > max:
            longest = word
            max = len(word)

    return longest

def main():
    rishoni(0,100)
    sentence = input("Enter a phrase")
    print(sentence[::-1])
    sentence2 = input("Enter a phrase to check if its a polindrom!")
    print(polindrom(sentence2))
    print(longestPhrase(sentence))

main()
