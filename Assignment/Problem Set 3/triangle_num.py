t_num = 0

# for n in range(1,151): # [1, 150]

#     t_num  = t_num + n

#     if t_num >= 150:
#         break
    
#     if t_num % 2 == 0:
#         print(t_num)
#     elif t_num % 5 == 0:
#         print(t_num)
        
n = 1
while t_num <= 150:

    t_num  = t_num + n
    n = n + 1

    if t_num % 2 == 0:
        print(t_num)
    elif t_num % 5 == 0:
        print(t_num)
