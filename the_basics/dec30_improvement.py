# a = '125*400'
# b = '15+385'

# # find nums
# # def get_nums(s):
# #     new_str = [int(item) for item in s if str.isdigit(item)] 
# #     return new_str

# # print(get_nums(b))



# find operator
def get_operator(number):
   new_operator = [item for item in number if not str.isdigit(item)] 
   return new_operator[0]

# def get_operator_index(s):
#     i = 0
#     while True:
#         ch = s[i]
#         if not str.isdigit(ch):
#             return i
#         i += 1

# def get_operator_index(s):

#     print(len(s))
#     print(list(range(len(s))))
#     for i in range(len(s)):
#         print(i)
#         if not str.isdigit(s[i]):
#             return i

def get_operator_index(s):
    for i, ch in enumerate(s):
        print(i, ch)
        if not str.isdigit(ch):
            return i



def operation(left, operator, right):
    if operator == '+':
        return left + right 
    elif operator == '-':
        return left - right 
    elif operator == '*':
        return left * right 
    elif operator == '/':
        return left / right 
    else:
        return "cannot calculate"

# question = input("Enter your question: ")
question = '15*385'
# b = '15*385'
# operator = get_operator(question)
# print(operator)
idx = get_operator_index(question)
operator = question[idx]
# print(idx)
left = int(question[:idx])
# print(left)
right = int(question[idx+1:])
# print(right)
answer = (operation(left, operator, right))

answer = print(answer) 