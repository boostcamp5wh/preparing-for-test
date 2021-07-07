import sys
import math
sys.stdin.readline()                                    # 첫입력무시
mans_in_room = map(int, sys.stdin.readline().split())   # 두번째입력은 generator
main, sub = map(int, sys.stdin.readline().split())      # 세번째입력은 각 각 나눠줌
total = 0
for i in mans_in_room:                                  # 방마다 필요한 인원수 루핑
    if i>main:
        total += math.ceil((i-main) / sub)              # 주감독관역량보다 인원이 많으면 인원-주감독관역량 을 부감독관역량만큼 나누면 부감독관의 수가 나옴. 소수점은 +1명으로 올려버림.
    total += 1                                          # 어떤 방이든 1명은 필수니까 더해줌
print(total)                                            # 주감독관수 + 부감독관수(소수점은 +1)로 처리하면 전체 인원수 
