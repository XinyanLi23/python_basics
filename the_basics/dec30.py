# a = '125*400'
# b = '15+385'

# # find nums
# # def get_nums(s):
# #     new_str = [int(item) for item in s if str.isdigit(item) is True] 
# #     return new_str

# # print(get_nums(b))



# find operator
def get_operator(number):
   new_operator = [item for item in number if str.isdigit(item) is False] 
   return new_operator[0]



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

question = input("Enter your question: ")
#b = '15*385'
operator = get_operator(question)
# print(operator)
idx = question.index(operator)
# print(idx)
left = int(question[:idx])
# print(left)
right = int(question[idx+1:])
# print(right)
answer = (operation(left, operator, right))

answer = print(answer) 