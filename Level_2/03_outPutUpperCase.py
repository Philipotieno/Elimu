lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break

for sentense in lines:
    print(sentense)