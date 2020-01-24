'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count = 0):    
    if len(word) == 0:
        return count
    elif len(word) > 0:
        if word[0:2] == 'th':
            count += 1           
        return count_th(word[1:], count) 



    
#print(count_th('THtHThth'))    

sum = 0
n = 20

for i in range(n):
    j = 1
    while j < n:
        j *= 2
        sum += 1

print(sum)        