# 프로그래머스 2단계 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [] #큐
    for i in range(len(truck_weights)):
        while True: # truck_weights[i] 가 다리에 올라올 때까지 반복
            answer += 1 #시간 증가
            
            if len(bridge) == bridge_length: 
                bridge.pop(0) #다리가 다 찼으면 가장 먼저 들어온 트럭을 pop
                
            if (sum(bridge) + truck_weights[i]) <= weight: 
                bridge.append(truck_weights[i]) 
                break #다리에 트럭을 더 올릴 수 있으면 올리고 break
            else:
                bridge.append(0) #더 올릴 수 없으면 다리에 0을 올리고 반복문 계속 돌림
    return answer + bridge_length
