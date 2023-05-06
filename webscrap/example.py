import requests
import bs4

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Begin')
    result = requests.get('http://www.example.com')
    # print(result.text)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    # print(soup)
    print(soup.select('title')[0].getText())
    print(soup.select('p'))
