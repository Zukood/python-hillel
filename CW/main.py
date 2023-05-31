import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def is_valid_url(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.ConnectionError:
        return False


def parse_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    return [link['href'] for link in links]


def save_valid_links(links):
    valid_links = []
    broken_links = []
    for link in links:
        absolute_link = urljoin(base_url, link)
        if is_valid_url(absolute_link):
            valid_links.append(absolute_link)
        else:
            broken_links.append(absolute_link)

    with open('valid_links.txt', 'w') as file:
        file.write('\n'.join(valid_links))

    with open('broken_links.txt', 'w') as file:
        file.write('\n'.join(broken_links))


def main():
    parser = argparse.ArgumentParser(description='HTML Page Parser')
    parser.add_argument('-url', type=str, help='URL of the HTML page')
    args = parser.parse_args()

    if not args.url:
        args.url = input('Enter the URL of the HTML page: ')

    global base_url
    base_url = args.url

    if not is_valid_url(base_url):
        print('Invalid URL')
        return

    links = parse_html(base_url)
    save_valid_links(links)

    print('Parsing complete.')


if __name__ == '__main__':
    main()
