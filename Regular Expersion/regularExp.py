#patternmatching


string="ababababaabbbbabbbbabbbbab"
#count number of ab in given string
#step 1 improt re

import re
pattern="ab"
matcher=re.finditer(pattern,string)
count=0
for match in matcher:
    count+=1
    print(match.start()) #it will retrun postion of ab
    print(match.group()) #it will retrun object of ab
#print(count)