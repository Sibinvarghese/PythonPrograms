from re import *


pattern="aaaaabaaabbbbaaabbaaaaa"

#x="a+" #it will single a and sequences of a not check b position
#x="a*" #it will check for all character includeing b postion

#x="a?" #it will check for a all postion

#x="^a" # is the given pattern staring with a

# x="a$" #is the given pattern ending with a

#x="a{2}" #it will check for 2 number of a

# x="a{3}" #it will check for 3 number of a

# x="a{2,3}" #minimum 2 a and and maximum 3 a




matcher=finditer(x,pattern)
for match in matcher:
    print(match.start())
    print(match.group())