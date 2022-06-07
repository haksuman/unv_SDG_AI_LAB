import requests
from bs4 import BeautifulSoup
import unicodedata

print("working")


def get_article_data(article_link):
    page = requests.get(article_link)  # requesting and parsing with bs4
    soup = BeautifulSoup(page.content, 'html.parser')
    post_date = None
    keywords_doc = None
    doc_title = None
    if not soup.find('p', class_='subheader') is None:
        post_date = soup.find('p', class_='subheader').string  # document post date of page
    if not soup.h1 is None:
        doc_title = soup.h1.get_text()  # document title in page

    label_content = soup.find('div', class_='pageSDGicons section')
    list_label_content = []  # list for SDG labels
    if not label_content is None:
        for item in label_content.findAll("img"):
            list_label_content.append(item.get('alt'))

    doc_paragraphs_parent_set = soup.find_all('div', class_='parbase section text')
    list_doc_paragraphs = []  # list for paragraphs in document / each paragraph is one list element
    for doc_paragraphs_parent in doc_paragraphs_parent_set:
        for item in doc_paragraphs_parent.findAll("p"):
            item_text = unicodedata.normalize("NFKD", item.get_text())
            list_doc_paragraphs.append(item_text)
    doc_paragraphs = "-".join(list_doc_paragraphs)  # paragraphs of pages connected with "-" to one string variable

    keywords_doc_parent = soup.find("meta", {"name": "keywords"})  # key word text
    if not keywords_doc_parent is None:
        keywords_doc = keywords_doc_parent['content']  # stored as str with "," between keywords

    # list for title page path
    path_doc = soup.find("ul", {'class': "breadcrumbs"})
    list_path_doc = []
    if not path_doc is None:
        for item in path_doc.findAll('span', {'property': 'name'}):
            list_path_doc.append(item.string)

    return list_path_doc, post_date, doc_title, doc_paragraphs, list_label_content, keywords_doc
    # list_path_doc = list, post_date = str, doc_title =str, doc_paragraphs=str, list_label_content=list, keywords=str


list_path_article, post_date, doc_title, str_prps_article, list_label_article, keywords_doc = get_article_data(
    "https://www.bw.undp.org/content/botswana/en/home/presscenter/articles/2019/undp-playing-its-integrator-role-as-part-of-accelerating-sdgs-im.html")

a = 5
print("OK")
# "https://www.gm.undp.org/content/gambia/en/home/blog/2020/undp-support-to-the-establishment-of-the-virtual-courts-in-respo.html" working link
