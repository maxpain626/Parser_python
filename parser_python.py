import urllib.request as urllib2
import re
import zlib
import os.path
import hashlib


# сайт
url = "https://www.wildberries.ru/catalog/109361831/detail.aspx"


# функция чтобы зайти на сайт
def query_web(url):
    response = urllib2.urlopen(url)
    return print(response.read())

# создание хеша и сохранение в файл
def cash(url):
    hash = hashlib.md5(url.encode('utf-8')).hexdigest()
    fname = "cache/" + hash
    if not os.path.isfile(fname):
        content = query_web(url)
        f = open(fname, "wb")
        f.write(content)
        f.close()
    else:
        f = open(fname, "rb")
        content = f.read()
    return content
    


cash(url)


'''
urllib.request.urlopen(): Отправить HTTP-запрос и получить ответ от сервера.
urllib.request.urlretrieve(): Скачать файл по указанному URL.
urllib.request.Request(): Создать объект запроса с дополнительными параметрами, такими как заголовки.
urllib.parse.urlencode(): Преобразовать словарь параметров в строку запроса.
urllib.error.URLError: Исключение в случае ошибки при выполнении запроса.
urllib.robotparser.RobotFileParser(): Парсить robots.txt файлы для проверки доступа к ресурсам.
'''

'''
Методы, которые предоставляет функция urllib.request.urlopen(), включают следующие:

read(size=None): Чтение данных из ответа. Если аргумент size указан, читает и возвращает указанное количество байтов данных, иначе возвращает все данные.
readline(size=-1): Чтение строки из ответа. Если указан аргумент size, читает и возвращает строку указанной длины (или меньше), иначе возвращает строку до конца строки.
readlines(hint=-1): Чтение всех строк из ответа и возвращает их в виде списка. Можно указать максимальное количество байтов для чтения (hint).
getcode(): Получение HTTP-кода состояния ответа (например, 200 - успешный запрос).
geturl(): Получение исходного URL, к которому был выполнен запрос (могут быть перенаправления).
info(): Получение объекта, содержащего заголовки ответа.
'''

'''
Example usage:
    
    import urllib.request
    
    # set up authentication info
    authinfo = urllib.request.HTTPBasicAuthHandler()
    authinfo.add_password(realm='PDQ Application',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='geheim$parole')
    
    proxy_support = urllib.request.ProxyHandler({"http" : "http://ahad-haam:3128"})
    
    # build a new opener that adds authentication and caching FTP handlers
    opener = urllib.request.build_opener(proxy_support, authinfo,
                                         urllib.request.CacheFTPHandler)
    
    # install it
    urllib.request.install_opener(opener)
    
    f = urllib.request.urlopen('https://www.python.org/')
'''
