import requests
from bs4 import BeautifulSoup

print("working")

page = requests.get(
    "https://www.gm.undp.org/content/gambia/en/home/blog/2020/undp-support-to-the-establishment-of-the-virtual-courts-in-respo.html")
soup = BeautifulSoup(page.content, 'html.parser')

post_date = soup.find('p', class_='subheader').string  # document post date of page
doc_title = soup.h1.get_text()  # document title in page

label_content = soup.find('div', class_='pageSDGicons section')
list_label_content = []  # list for SDG labels
for item in label_content.findAll("img"):
    list_label_content.append(item.get('alt'))

doc_paragraphs_parent = soup.find('div', class_='parbase section text')
list_doc_paragraphs = []  # list for paragraphs in document
for item in doc_paragraphs_parent.findAll("p"):
    list_doc_paragraphs.append(item.string)

keywords_doc_parent = soup.find("meta", {"name": "keywords"})  # key word text
keywords_doc = keywords_doc_parent['content']

# list for title page path
path_doc = soup.find("ul", {'class': "breadcrumbs"})
list_path_doc = []
for item in path_doc.findAll('span', {'property': 'name'}):
    list_path_doc.append(item.string)

print(list_doc_paragraphs)
print("hello")

