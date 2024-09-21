def count_characters(string):
    return len(string)



string = "Hello, World!"

sokitu = count_characters(string)

print("so ki tu trong chuoi la: ",sokitu)

# count words in string

def count_words(string):
    return len(string.split())

string = "Hello, World!"

sokitu = count_words(string)

print("so tu trong chuoi la: ",sokitu)
