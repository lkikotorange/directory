import requests
from bs4 import BeautifulSoup

app_id = 12345
s = requests.Session()
s.headers.update ({
    'Referer': 'https://www.twitch.tv',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'
  })


def load_user (app_id, page, session):
    url = 'https://www.twitch.tv/directory' % (app_id, page)
    request = session.get(url)
    return request.text


def name(text):
    soup = BeautifulSoup(text)
    twitch_list = soup.find('div', {'class': 'directory-container'})
    return twitch_list is not None


def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    return text


def parse_User_defalile_bs (filiname):
    results = []
    text = read_file(filename)

    soup = BeautifulSoup(text)
    twitch_list = twitch_list = soup.find('div', {'class': 'directory-container'})
    items = twitch_list.find_all('div', {'class': ['item', 'item even']})
    for item in items:

        categ_link = item.find('div', {'class': 'tw-card-title'}).find('h3').get('class')
        categ_desk = item.find('div', {'class': 'tw-card-title'}).find('h3').text
        categ_id = re.findall('\d+', categ_link)[0]
        print (item)

        results.append({
            'categ_id': categ_id,
            'categ_desk': categ_desk
        })
    return results


page = 1
while True:
    data = load_user(app_id, page, s)
    if name(data):
        with open ('./page.html'%(page), 'w', encoding='utf-8') as f:
            f.write(r.data)
            page+=1
    else:
        break
