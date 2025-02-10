def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(words(file_contents))

def words(text):
    words = len(text.split())
    return(words)


main()
