import requests
from bs4 import BeautifulSoup
import pandas as pd
from project_dir_helper import project_dir
import urllib.parse


df_link_COs = pd.read_excel(project_dir + "/data/interim/output_links.xlsx", index_col=0)  # getting all generated links
df_link_COs = df_link_COs.loc[df_link_COs['status'] == 200].reset_index()  # keeping only working links


def get_h4_tag(link_page):
    h4_link_list = []
    h4_text_list = []
    parent_link_list = []
    count_print = 0
    for h4 in soup.select("h4"):
        h4_href_link = h4.a["href"]  # getting href links in h4 tags
        h4_link = urllib.parse.urljoin(link_page, h4_href_link)
        h4_link_list.append(h4_link)  # appending obtained href links to list
        h4_text = h4.get_text(strip=True)  # getting h4 tag text
        h4_text_list.append(h4_text)  # appending obtained h4 text to list
        parent_link_list.append(link_page)
        count_print = count_print+1
        print(count_print)
    return parent_link_list, h4_link_list, h4_text_list  # retuning list of links and text as 2 lists


list_all_parent_link = []
list_all_h4_link = []
list_all_h4_text = []
for link_article_parent_page in df_link_COs["link"]:
    page = requests.get(link_article_parent_page)
    soup = BeautifulSoup(page.content, 'html.parser')
    temp_list_parent, temp_list_h4_link, temp_list_h4_text = get_h4_tag(link_article_parent_page)
    list_all_parent_link.extend(temp_list_parent)
    list_all_h4_link.extend(temp_list_h4_link)
    list_all_h4_text.extend(temp_list_h4_text)

df_link_articles = pd.DataFrame(
    {'parent_link': list_all_parent_link, 'link_type': list_all_h4_link, 'article_title': list_all_h4_text})

df_link_articles.to_excel(project_dir+"/data/interim/output_article_links.xlsx")

print("OK")
