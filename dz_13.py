'''2'''

# def plus_two(number):
#     try:
#         result = number + 2
#         print(result)
#     except TypeError:
#         print('Ожидаемый тип данных — число!')
# plus_two(3)
# plus_two('3')

'''3'''

try:
    my_list = [1, 2, 3]
    index = 2 
    '''Ерканат напишите сверху свой индекс'''
    print("Element at index", index, ":", my_list[index])
except IndexError:
    print("Index is out of range!")