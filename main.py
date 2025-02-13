def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    word_count = words(file_contents)
    char_dict = chars(file_contents)
    report(word_count, char_dict)
    #print(word_count, char_dict)
   

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
        "z" : 0,
        " " : 0,
        "." : 0,
        "," : 0,
        "!" : 0,
        "?" : 0,
        "*" : 0,
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0,
        "5" : 0,
        "6" : 0,
        "7" : 0,
        "8" : 0,
        "9" : 0,
        "0" : 0,
        "(" : 0,
        ")" : 0,
        "-" : 0,
        "@" : 0,
        ":" : 0,
        "/" : 0,
        "$" : 0,
        "'" : 0,
        '"' : 0,
        '%' : 0,
        ";" : 0,
        "[" : 0,
        "]" : 0,
        '\n': 0,
        '#' : 0,
        '_' : 0 
    }
    lowered_string = text.lower()
    for char in lowered_string:
        letters[char] += 1        
    return(letters)

def report(word_count, char_dict):
    
    alpha_list = []
    for char in char_dict:
        if char.isalpha():
            char_info = {"char": char, "num": char_dict[char]}
            alpha_list.append(char_info)
    alpha_by_values = sorted(alpha_list, key=lambda item: item["num"], reverse=True)
        
        
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for alpha in alpha_by_values:
        print(f"The '{alpha["char"]}' character was found {alpha["num"]} times")

    



main()