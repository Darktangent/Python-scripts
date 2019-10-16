import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.find_all('a'))
# print(soup.find(id="score_21254166"))
links = soup.select('.storylink')
subtext = soup.select('.subtext')
# print(votes[0])
# print(votes[0].get('id'))
# print(links)
# print(votes)


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):

        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(" points", ''))
            if (points > 99):
                # print(points)
                hn.append({'title': title, 'link': href, "votes": points})

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))
