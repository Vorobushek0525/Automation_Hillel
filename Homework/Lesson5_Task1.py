import re

text = 'aba accca azzza wwwwa'
pattern = "a[b-z]*a"

print(re.sub(pattern, '!', text))



#or

# text = 'aba accca azzza wwwwa'
#
# print(re.sub(r"a[b-z]*a", '!', text))