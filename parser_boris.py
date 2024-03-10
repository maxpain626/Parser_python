import urllib.request as urllib2
import re
import zlib
import os.path
import hashlib
import json


# функция чтобы зайти на сайт
def query_web(_url: str, use_unzip: bool):
    req = urllib2.Request(_url)
    response = urllib2.urlopen(_url)
    if use_unzip:
        return unzip(response.read())
    return response.read()


# создание хеша и сохранение в файл
def query_with_cache(_url: str, use_unzip: bool):
    filename = hashlib.md5(_url.encode('utf-8')).hexdigest()
    filepath = "cache/" + filename
    if not os.path.isfile(filepath):
        _content = query_web(_url, use_unzip)
        f = open(filepath, "wb")
        f.write(_content)
        f.close()
    else:
        f = open(filepath, "rb")
        _content = f.read()
    return _content


def unzip(stream):
    dec = zlib.decompressobj(32 + zlib.MAX_WBITS)  # offset 32 to skip the header
    return dec.decompress(stream)


def parse_wb(_url):
    # парсим номер продукта на ВБ из урла
    match = re.search(r'/([^/]*?)/detail.aspx', str(_url))
    # проверяем что урл получилось распарсить, если нет - выходим из фукции
    if match is None:
        print('Wrong url format. Can not parse product id')
        return
    # формируем урл для запроса к api ВБ, в качестве параметра нужно указать номер продукта
    product_id = match[1]
    price_url = f'https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={product_id}'
    # print(price_url)
    # делаем запрос (кеш используется только для отладки),
    # апи не архивирует ответ, поэтому второй параметр False (см. query_with_cache и query_web)
    # ответ сразу парсим в словарь(?) json
    price_data = json.loads(query_with_cache(price_url, False))
    # выводим название продукта, цену без скидки и цену со скидкой
    p = price_data["data"]["products"][0]
    print("-------------")
    print(f'{p["name"]}  #{p["id"]}')
    print(p["priceU"] / 100)
    print(p["salePriceU"] / 100)
    print(p)


# тестовый список продуктов
urls = [
    "https://www.wildberries.ru/catalog/109361831/detail.aspx",
    "https://www.wildberries.ru/catalog/177899105/detail.aspx",
    "https://www.wildberries.ru/catalog/167972025/detail.aspx",
    "https://www.wildberries.ru/catalog/119082472/detail.aspx",
    "https://www.wildberries.ru/catalog/45392768/detail.aspx?targetUrl=SG"
]

for url in urls:
    parse_wb(url)

# WB
# https://www.wildberries.ru/catalog/109361831/detail.aspx
# https://basket-07.wbbasket.ru/vol1093/part109361/109361831/info/ru/card.json -> data[colors]
# https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm=$color[0];$color[1];...

# https://www.wildberries.ru/catalog/177899105/detail.aspx

# cache(url)


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