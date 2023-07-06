import re

email = input("What's your email: ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|gov|net|com)$", email, re.IGNORECASE):  # re.search(search_string or patterns, main_string)
    print("Valid")
    #  here, r-> raw string, [^@]-> any character except '@' sign
    # [a-zA-Z0-9_] -> \w
else:
    print("Invalid")

'''
. -> any character except a newline
* -> 0 or more repetitions
+ -> 1 or more repetitions
? -> 0 or 1 repetition
{m} -> m repetitions
{m,n} -> m–n repetitions

 ^ -> matches the start of the string
$ -> matches the end of the string or just before the newline at the end of the string

 [] -> set of characters
[^] -> complementing the set

\d -> decimal digit
\D -> not a decimal digit
\s -> whitespace characters
\S -> not a whitespace character
\w -> word character … as well as numbers and the underscore -> [a-zA-Z0-9_]
\W -> not a word character

 A|B -> either A or B
(...) -> a group
(?:...) -> non-capturing version

'''