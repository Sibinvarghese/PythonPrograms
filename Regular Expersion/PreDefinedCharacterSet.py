#PreDefined Character Set
import re

#x="[abc]" #it will check for either a,b or c is present in target string
#x="[a-z]" #it will check for lowercase a to z alphabets
#x="[0-9]" #it will check for 0 to 9 digits
#x="[A-Z]" #it will check for Uppercase A to Z alphabets
#x="[a-zA-Z]" #it will check for lowercase and uppercase a to z alphabets
#x="[a-zA-Z0-9]"  #it will check for all words
#x="[^a-zA-Z0-9]" # '^' symbol it will accept All characters without lower and uppercase a-z and 0-9 digits
#x="[^0-9]" #'^' symbol it will accept All characters without 0-9
#PreDefined Character
#====================
#x="\s" #it will check for space
#x="\d" #it will check for digit ("\d" == "[0-9]" equallent )
#x="\D" #it will accept all character without digits  ("\D"=="[^0-9]")
#x="\w" #it will check for all character without spcl character ("\w"=="[a-zA-Z0-9]")
x="\W" #it will accept al Special Character withou alphabets and digits  ("\W"=="[^a-zA-Z0-9]"
matcher=re.finditer(x,"ab7 c@KZ")
for match in matcher:
    print(match.start())
    print(match.group())