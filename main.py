def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(words(file_contents))
    print(chars(file_contents))


def words(text):
    words = len(text.split())
    return(words)

def chars(text):
    letters = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0
    }
    lowered_string = text.lower()
    for char in lowered_string:
        if char == letters[char]:
            n = letters[char:n+1]
            letters[char:n]
        else:
            print("not in the list")
    return(letters)

main()
