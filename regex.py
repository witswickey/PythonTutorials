import re

st = 'jfhsf#$dmcdsns@$dsmfskmffsdkfm'

regext = re.compile(r'\w')
foo = ""
print(regext.findall(st))
for ch in regext.findall(st):
    foo += ch
print(foo)
