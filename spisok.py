from random import randint
from random import randrange

'''
def make_spisok():
    list_a = [randint(int(input("Insert min of list: ")), int(input("Insert max of list"))) for i in range(input("Insert length of list: "))]
    return list_a
'''

#pricelist = [431, 523, 123, 7735, 8845, 24, 63, 6342, 735, 88945, 423, 5378]



def rand_params():
    length_list = int(input("Insert length of list: "))
    min_list = int(input("Insert min of list: "))
    max_list = int(input("Insert max of list: "))
    return length_list, min_list, max_list

length_list, min_list, max_list = rand_params()

def rand_list():
    len, mi, ma = rand_params()
    arr = []
    for _ in range(len):
        arr.append(randint(mi, ma))
    print(arr)
    return arr

# зацикливание программы
def looping():
    while True:
        user_input = input('Insert key to continue or "end" to stop": ') 
        rand_list() 
        if user_input.lower() == "end":
            break
        
looping()
