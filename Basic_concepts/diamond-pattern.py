n = 13

for x in range(1,n+1,2):
    pattern =  (('*'+ ' ') * x).center(n*2)
    print(pattern)
for y in reversed(range(1,n+1,2)):
    reversepattern = (('*'+ ' ') * y).center(n*2)
    print(reversepattern)