from urllib import request


url = "https://www.example.com"
response = request.urlopen(url)
html = response.read()

soup = BeautifulSoup(html, "html.parser")

# Находим заголовок страницы
title = soup.title.string
print("Title of the page:", title)

# Находим все ссылки на странице
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

# Находим текстовое содержимое тега <p>
paragraphs = soup.find_all("p")
for paragraph in paragraphs:
    print(paragraph.text)
    