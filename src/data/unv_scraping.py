import requests
from bs4 import BeautifulSoup

print("working")

# list_path_article = []  # stands for relative path of document
# list_prps_article = []  # stands for list of paragraphs in document
# list_label_article = []  # stands for list of labels in document


def get_article_data(article_link):
    page = requests.get(article_link)  # requesting and parsing with bs4
    soup = BeautifulSoup(page.content, 'html.parser')

    post_date = soup.find('p', class_='subheader').string  # document post date of page
    doc_title = soup.h1.get_text()  # document title in page

    label_content = soup.find('div', class_='pageSDGicons section')
    list_label_content = []  # list for SDG labels
    for item in label_content.findAll("img"):
        list_label_content.append(item.get('alt'))

    doc_paragraphs_parent_set = soup.find_all('div', class_='parbase section text')
    list_doc_paragraphs = []  # list for paragraphs in document / each paragraph is one list element
    for doc_paragraphs_parent in doc_paragraphs_parent_set:
        for item in doc_paragraphs_parent.findAll("p"):
            list_doc_paragraphs.append(item.get_text())

    keywords_doc_parent = soup.find("meta", {"name": "keywords"})  # key word text
    keywords_doc = keywords_doc_parent['content']  # stored as str with "," between keywords

    # list for title page path
    path_doc = soup.find("ul", {'class': "breadcrumbs"})
    list_path_doc = []
    for item in path_doc.findAll('span', {'property': 'name'}):
        list_path_doc.append(item.string)

    return list_path_doc, post_date, doc_title, list_doc_paragraphs, list_label_content, keywords_doc


list_path_article, post_date, doc_title, list_prps_article, list_label_article, keywords_doc = get_article_data(
    "https://www.gw.undp.org/content/guinea_bissau/en/home/blog/design-thinking-as-a-powerful-tool-to-improve-public-service-del.html")

print(list_path_article)

#"https://www.gm.undp.org/content/gambia/en/home/blog/2020/undp-support-to-the-establishment-of-the-virtual-courts-in-respo.html" working link