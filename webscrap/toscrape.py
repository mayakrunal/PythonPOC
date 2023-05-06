import requests
import bs4

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    books: list[str] = []
    for i in range(1, 51):
        result = requests.get(f'http://books.toscrape.com/catalogue/page-{i}.html')
        # print(result.text)
        soup = bs4.BeautifulSoup(result.text, "lxml")
        products = soup.select('.product_pod')
        for item in products:
            if len(item.select('.star-rating.Two')) != 0:
                # image = article.select('a')[0]['href']
                book = item.select('a')[1]['title']
                # book = item.find_parent(attrs={'class': 'product_pod'})
                # .select('h3 a')[0].getText()
                books.append(book)

    print(books)
