import requests
import bs4

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Begin')
    result = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
    # print(result.text)
    soup = bs4.BeautifulSoup(result.text, "lxml")

    image1 = soup.select('.infobox .image img')
    image1_url = 'https:' + image1[0].attrs['src']

    image2 = soup.select('.thumb.tright .thumbimage')
    image2_url = 'https:' + image2[0].attrs['src']
    print(image1_url)
    r1 = requests.get(image1_url)
    with open('image1.jpg', 'wb') as i1:
        i1.write(r1.content)

    r2 = requests.get(image2_url)
    with open('image2.jpg', 'wb') as i2:
        i2.write(r2.content)
