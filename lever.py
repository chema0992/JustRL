import random

def Try(choice):
    if random.random() < true_probs[choice]: # 성공
        reward = 1
        counts[choice] += 1
        Q[choice] = Q[choice] + (reward - Q[choice]) / counts[choice]
        return 0
    else: # 실패
        reward = 0
        counts[choice] += 1
        Q[choice] = Q[choice] + (reward - Q[choice]) / counts[choice]
        return 0

lever_num: int = 3 # 레버 개수
true_probs = [0.2, 0.5, 0.8] # 실제 확률
Q = [0] * lever_num # Q 초기화
counts = [0] * lever_num # 몇번 당겼는지 기록하는 리스트 초기화
epsilon: int = 0.2 # 탐험 확률
num: int = 0
choice: int = 0

loop = int(input("몇번 반복?: "))

for i in range(loop):
    num = random.random()
    if num <= epsilon: # 탐험
        choice = random.randint(0, 2)
        Try(choice)
    else: # Q에 따라서
        choice = Q.index(max(Q))
        Try(choice)

print(f"{loop}번 반복 결과:\n 실제 확률: {true_probs}\n Q: {Q}\n counts: {counts}\n")