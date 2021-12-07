import random

moves = "^v><"

route = ""

for i in range(random.randint(1,30)):
    route += moves[random.randint(0,3)]

walked = {
  "0,0": 1
}

current = [0, 0]

def save(now):
    now = str(now[0]) + ',' + str(now[1])
    if now in walked:
        walked[now] += 1
    else:
        walked[now] = 1

for direction in route:
    if direction == '^': 
        current[1] += 1
        save(current)
    elif direction == 'v': 
        current[1] -= 1
        save(current)
    elif direction == '>': 
        current[0] += 1
        save(current)
    elif direction == '<': 
        current[0] -= 1
        save(current)

maxv = max(walked.values())
print(maxv)