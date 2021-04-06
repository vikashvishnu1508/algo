# def power_of_three(num):
#     while num > 0:
#         if num % 3 == 0:
#             return True
#         else:
#             num = num // 3
#     return False

def power_of_three2(num):
    if num <= 0:
        return False
    if num % 3 == 0:
        return True
    else:
        power_of_three2(num // 3)

print(power_of_three2(847288609443))

