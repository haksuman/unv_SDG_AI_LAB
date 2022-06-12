import requests
from bs4 import BeautifulSoup
import pandas as pd
from project_dir_helper import project_dir
import urllib.parse
from src.features.view_more_automation import func_view_more


df_link_COs = pd.read_excel(project_dir + "/data/interim/output_links.xlsx", index_col=0)  # getting all generated links
df_link_COs = df_link_COs.loc[df_link_COs['status'] == "200"].reset_index()  # keeping only working links

def get_url_status(url):  # checks status for each url in list urls
    try:
        r = requests.get(url)
        temp_status = str(r.status_code)
    except Exception as e:
        temp_status = "Failed to connect"
    return temp_status

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
        count_print = count_print + 1
        print(count_print)
    return parent_link_list, h4_link_list, h4_text_list  # retuning list of links and text as 2 lists


list_all_parent_link = []
list_all_h4_link = []
list_all_h4_text = []
for link_article_parent_page in df_link_COs["link"]:
    html_src = func_view_more(link_article_parent_page)
    #page = requests.get(link_article_parent_page)
    soup = BeautifulSoup(html_src)
    temp_list_parent, temp_list_h4_link, temp_list_h4_text = get_h4_tag(link_article_parent_page)
    list_all_parent_link.extend(temp_list_parent)
    list_all_h4_link.extend(temp_list_h4_link)
    list_all_h4_text.extend(temp_list_h4_text)

df_link_articles = pd.DataFrame(
    {'parent_link': list_all_parent_link, 'link_article': list_all_h4_link, 'article_title': list_all_h4_text})

for index_article, row_article in df_link_articles.iterrows():  # this for loop is stands for solving a bug that generate blog link as article link
    if row_article["parent_link"] == row_article["link_article"]:
        df_link_articles.drop(index_article, axis=0, inplace=True)

step_counter2 = 0
list_article_link_status = []
for index_article_1, row_article_1 in df_link_articles.iterrows():
    status_check = get_url_status(row_article_1["link_article"])
    list_article_link_status.append(status_check)
    step_counter2 = step_counter2 + 1
    print(step_counter2)

df_link_articles["article_link_status"] = list_article_link_status
df_link_articles = df_link_articles.loc[df_link_articles['article_link_status'] == "200"].reset_index()  # keeping only working links



df_link_articles.to_excel(project_dir + "/data/interim/output_article_links.xlsx")

print("OK")
