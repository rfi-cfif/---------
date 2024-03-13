from random import *


def changing(ans):
    ANS = {}
    for i in range(0, len(ans), 2):
        k = int(ans[i])
        ANS[k] = ANS.get(k, []) + [ans[i + 1]]
    num_was = list(ANS.keys())
    num_peop = []
    for i in num:
        i = [g for g in i if g not in num_was]
        num_peop.append(i)
    # print(num_was)
    # print(num)
    # print(num_peop)
    nums = [choice(j) for j in num_peop]
    id_num = [(j, choice(ID[j])) for j in nums]
    return id_num

# def changing(ans):
#     nums = [choice(j) for j in num]
#     id_num = [(j, choice(ID[j])) for j in nums]
#     return id_num

with open('numbers_d.txt') as f:
    num = [[int(i) for i in f.readline().split(', ')] for _ in range(3)]

with open('ID_answers.txt') as f:
    ID = {}
    for b in f.readlines():
        n, id, ans = [int(i) if i.isdigit() else i for i in b.split()]
        ID[n] = ID.get(n, []) + [(id, ans)]

with open('people_d.txt', encoding='utf-8') as f:
    people = []
    peop_ans = {}
    for p in f.readlines():
        p = p.split()
        people.append(p[0])
        peop_ans[p[0]] = p[1:]

n = 21
a = {people[i]: 0 for i in range(n)}
for i in range(n):
    k, v = people[i], peop_ans[people[i]]
    a[k] = changing(v)

with open('people_d.txt', 'w', encoding='utf-8') as f:
    for k, v in a.items():
        f.write(f'{str(k)} ')
        for i in v:
            f.write(f'{i[0]} {i[1][0]} ')
        for i in range(0, len(peop_ans[k]), 2):
            f.write(f'{peop_ans[k][i]} {peop_ans[k][i + 1]} ')
        f.write('\n')

with open('14.03.24.txt', 'w', encoding='utf-8') as f:
    for k, v in a.items():
        f.write(f'{str(k)}\n')
        for i in v:
            f.write(f'{i[0]}  {i[1][0]}\n')
        f.write('\n')

with open('14.03.24_ans.txt', 'w', encoding='utf-8') as f:
    for k, v in a.items():
        f.write(f'{str(k)}\n')
        for i in v:
            f.write(f'{i[1][1]}\n')
        f.write('\n')
