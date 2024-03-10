import hashlib


my_hash = input("Введите хэшируемые данные: ")

hash_object = hashlib.sha256(my_hash.encode())
print(hash_object.hexdigest())
