from collections import Counter

input_state = True
data = {
    'nshoes':0,
    'shoe_sizes':[],
    'nclients': 0,
    'ssizes_and_prices': [],
    'counter': 1,
}
while input_state:
    _input =input()
    if _input == '' or  _input ==  ' ' or _input ==  '\t':
        input_state= False
    else:
        if data['counter'] == 1:
            data['nshoes'] = _input if _input.isdigit() else int(_input)
        elif data['counter'] == 2:
            data['shoe_sizes'] = _input.split()
        elif data['counter'] == 3:
            data['nclients'] = _input if _input.isdigit() else int(_input)
        else:
            data['ssizes_and_prices'].append(_input.split())
            
        data['counter'] += 1

data['shoe_sizes'] = data['shoe_sizes'][:int(data['nshoes'])]
data['ssizes_and_prices'] = data['ssizes_and_prices'][:int(data['nclients'])]

print(Counter(data['shoe_sizes']))

'''
10
2 4 1 2 3 4 5 7 9 0 
6
4 55
2 12
7 25
8 10
4 99
3 88
'''
total = 0
datas = list(set(data['shoe_sizes']))
print(datas)

for x in data['ssizes_and_prices']:
    if x[0] in datas:
        total+=int(x[1])
        

print(total)