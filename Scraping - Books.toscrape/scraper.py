# Data to extract:

# - Title
# - Price
# - Stock
# - Rate

# -------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import requests

URL = 'https://books.toscrape.com/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')

books = []

rating_map = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
}
    
books_content = soup.select('article.product_pod')

for book in books_content:
    title = book.select_one('h3 a')['title']

    book_price = book.select_one('p.price_color').text.strip()
    price = float(book_price.replace('Â£', ''))

    book_stock = book.select_one('p.instock').text.strip()
    stock = True if 'In stock' in book_stock else False

    book_rating = book.select_one('p.star-rating')['class'][1]
    rating = rating_map[book_rating]

    books.append({
        'title': title,
        'price': price,
        'stock': stock,
        'rating': rating,
    })

for book in books:

    print(book, '\n')
