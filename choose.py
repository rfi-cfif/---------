from random import *


def changing():
    nums = [choice(j) for j in num]
    id_num = [(j, choice(ID[j])) for j in nums]
    return id_num


with open('numbers.txt') as f:
    num = [[int(i) for i in f.readline().split(', ')] for _ in range(3)]

with open('ID_answers.txt') as f:
    ID = {}
    for b in f.readlines():
        n, id, ans = [int(i) if i.isdigit() else i for i in b.split()]
        ID[n] = ID.get(n, []) + [(id, ans)]

n = 17
a = {i + 1: 0 for i in range(n)}
for i in range(n):
    a[i + 1] = changing()

with open('23.01.24.txt', 'w') as f:
    for k, v in a.items():
        f.write(f'Variant  {str(k)}\n')
        for i in v:
            f.write(f'{i[0]}  {i[1][0]}\n')
        f.write('\n')
    
with open('23.01.24_ans.txt', 'w') as f:
    for k, v in a.items():
        f.write(f'Variant  {str(k)}\n')
        for i in v:
            f.write(f'{i[1][1]}\n')
        f.write('\n')
