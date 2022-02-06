import re

text = "*+ *q+ *qq+ *qqq+ *qqq qqq+"
pattern = "\*q{1,3}\+"

print(re.findall(pattern, text))