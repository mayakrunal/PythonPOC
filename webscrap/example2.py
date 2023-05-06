import requests
import bs4

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Begin')
    result = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
    # print(result.text)
    soup = bs4.BeautifulSoup(result.text, "lxml")

    for div in soup.select('.vector-toc-text'):
        for child in div.children:
            if isinstance(child, bs4.NavigableString) and not child.getText().isspace():
                print(child.getText())

    # print(soup)
