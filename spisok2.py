from random import randint


# список случайных чисел
def rand_list(len:int, mi:int, ma:int):
    arr = []
    for _ in range(len):
        arr.append(randint(mi, ma))
    return arr

resul = rand_list(100, 1, 20)

print(resul)


slovar = {
    
}
