# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as f:
       content = f.read()
    return  content

def count_words():
    import re
    text = read_file_content("./story.txt")
    text = text.lower()
    text = re.sub(r'[^\w]', ' ', text)
    text = re.sub(' +', ' ', text)
    words = text.split(" ")
    dicWords = {}
    for word in words:
        if word in dicWords:
            dicWords[word] += 1
            print(dicWords)
        elif word == "":
            pass
        else:
            dicWords[word] = 1
    return dicWords

count_words()