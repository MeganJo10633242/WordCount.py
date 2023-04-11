def word_count(filename):
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    return len(words)

filename = input("Enter filename to count words: ")
print("Word count:", word_count(filename))
