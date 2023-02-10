import re
string="i like #real-Madrid and #Manchester-City so much"
pattern=r'\#(.*?)\ '
result=re.sub(pattern, r'<a href= #\1<\\<a>' , string)
print(result)