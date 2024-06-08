from bs4 import BeautifulSoup
import requests

print("============ output =============")


# with open('htmlEx.html') as html_file:
#     soup = BeautifulSoup(html_file,'lxml')


# match = soup.h2
# match = soup.find('div', class_='post')

# posts = soup.find_all('div', class_='post')

# for post in posts:
#     print(post.h2.text)
#     print(post.p.text)


# ========== parse a real website ============

source = requests.get('https://www.nytimes.com/international/').text

soup = BeautifulSoup(source,'lxml')

news = soup.find_all('section', class_='story-wrapper')


for new in news:
    print(new.a.text)

