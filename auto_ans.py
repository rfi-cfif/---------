with open('ID_answers.txt') as f:
    ID = {}
    for b in f.readlines():
        n, id, ans = b.split()
        ID[n] = ID.get(n, {}) | {id: ans}
# print(ID)

s = ''
with open('19.02.24.txt', encoding='utf-8') as f:
    for i in range(17):
        k = f.readline()
        s += k
        for j in range(3):
            a, b = f.readline().split()
            ans = ID[a][b]
            s += ans + '\n'
        s += '\n'
        f.readline()
print(s)

with open('19.02.24_ans.txt', 'w', encoding='utf-8') as f:
    f.write(s)
