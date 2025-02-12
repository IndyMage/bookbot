def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
   #print(file_contents)
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
        ";" : 0
        
       
    }
    lowered_string = text.lower()
    for char in lowered_string:
        if char == 'a':
            letters['a'] += 1
        elif char == 'b':
            letters['b'] += 1
        elif char == 'c':
            letters['c'] += 1        
        elif char == 'd':
            letters['d'] += 1        
        elif char == 'e':
            letters['e'] += 1        
        elif char == 'f':
            letters['f'] += 1        
        elif char == 'g':
            letters['g'] += 1        
        elif char == 'h':
            letters['h'] += 1       
        elif char == 'i':
            letters['i'] += 1       
        elif char == 'j':
            letters['j'] += 1        
        elif char == 'k':
            letters['k'] += 1        
        elif char == 'l':
            letters['l'] += 1        
        elif char == 'm':
            letters['m'] += 1        
        elif char == 'n':
            letters['n'] += 1        
        elif char == 'o':
            letters['o'] += 1        
        elif char == 'p':
            letters['p'] += 1        
        elif char == 'q':
            letters['q'] += 1       
        elif char == 'r':
            letters['r'] += 1
        elif char == 's':
            letters['s'] += 1
        elif char == 't':
            letters['t'] += 1
        elif char == 'u':
            letters['u'] += 1
        elif char == 'v':
            letters['v'] += 1
        elif char == 'w':
            letters['w'] += 1
        elif char == 'x':
            letters['x'] += 1
        elif char == 'y':
            letters['y'] += 1
        elif char == 'z':
            letters['z'] += 1
        elif char == " ":
            letters[" "] += 1
        elif char == ".":
            letters["."] += 1
        elif char == ",":
            letters[","] += 1
        elif char == "!":
            letters["!"] += 1
        elif char == "?":
            letters["?"] += 1
        elif char == "1":
            letters["1"] += 1
        elif char == "2":
            letters["2"] += 1
        elif char == "3":
            letters["3"] += 1
        elif char == "4":
            letters["4"] += 1
        elif char == "5":
            letters["5"] += 1
        elif char == "6":
            letters["6"] += 1
        elif char == "7":
            letters["7"] += 1
        elif char == "8":
            letters["8"] += 1
        elif char == "9":
            letters["9"] += 1
        elif char == "0":
            letters["0"] += 1
        elif char == "(":
            letters["("] += 1
        elif char == ")":
            letters[")"] += 1
        elif char == "@":
            letters["@"] += 1
        elif char == "$":
            letters["$"] += 1
        elif char == "-":
            letters["-"] += 1
        elif char == "/":
            letters["/"] += 1
        elif char == ":":
            letters[":"] += 1
        elif char == "'":
            letters["'"] += 1
        elif char == '"':
            letters['"'] += 1
        elif char == "*":
            letters["*"] += 1
        elif char == ";":
            letters[";"] += 1
        elif char == "%":
            letters["%"] += 1       
    return(letters)

main()
