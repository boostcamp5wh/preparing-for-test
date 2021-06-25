import sys
time_price = []
for _ in range(int(sys.stdin.readline())):
    time, price = map(int, sys.stdin.readline().split())
    time_price.append({'time':time, 'price':price})
max_benefit = [0]*20
for i in range(len(time_price)):
    if max_benefit[i]>max_benefit[i+1]:
        max_benefit[i+1] = max_benefit[i]
    if max_benefit[i+time_price[i]['time']] < (max_benefit[i]+time_price[i]['price']):
        max_benefit[i+time_price[i]['time']] = max_benefit[i]+time_price[i]['price']
print(max_benefit[len(time_price)])
