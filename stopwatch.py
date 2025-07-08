# num_list = (input().split(' '))
# for i in range(len(num_list)):
#     num_list[i] = int(num_list[i])
# print(sum(num_list))


import time


minute = 0
second = 0

while True:
    time.sleep(1)
    second+=1
    if second == 60:
        minute+=1
        second=0
    if len(str(second)) == 1 and len(str(minute)) == 1:
        print(f'0{minute}:0{second}')
    elif len(str(second)) == 1 and len(str(minute)) != 1:
        print(f'{minute}:0{second}')
    elif len(str(second)) != 1 and len(str(minute)) == 1:
        print(f'0{minute}:{second}')
    elif len(str(second)) != 1 and len(str(minute)) != 1:
        print(f'{minute}:{second}')
     
