
a = input()
z = input()
x, y = 0, len(z)
counter = 0
values = []
while True:
    if counter == (len(a)):
        break
    if counter == 0:
        
        values.append([a[x:y], (x, y-1)])
    else:
        x+=1
        y+=1
        values.append([a[x:y], (x, y-1)])
        
    counter += 1
final_values = []
for _ in values:
    if _[0]==z:
        final_values.append(_[1])
if len(final_values) == 0:
    print((-1, -1))
else:
    for _ in final_values:
        print(_)