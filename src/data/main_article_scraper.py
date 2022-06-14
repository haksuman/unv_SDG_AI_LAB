import pandas as pd
from unv_scraping import get_article_data
from project_dir_helper import project_dir
import requests
from src.features.project_functions import get_url_status

df_article_scrape = pd.read_excel(project_dir + "/data/interim/output_article_links.xlsx",
                                  index_col=0)  # getting all generated article links

# df_article_scrape = df_article_scrape.head(10)  # in order to reduce number of rows in df

list_main_path_article = []
list_main_post_date = []
list_main_doc_title = []
list_main_prps_article = []
list_main_label_article = []
list_main_keywords_article = []


step_counter = 0
# for index_status_check, row_status_check in df_article_scrape.iterrows():
#     status_check = get_url_status(row_status_check["link_article"])
#     if not str(status_check) == 200:
#         df_article_scrape.drop(index_status_check,inplace=True)
#     step_counter = step_counter + 1
#     print(step_counter)

count = 1
for index_article, row_article in df_article_scrape.iterrows():
    status_check = get_url_status(row_article["link_article"])
    if not str(status_check) == "200":
        df_article_scrape.drop(index_article, inplace=True)
        continue

    list_path_article, post_date, doc_title, str_prps_article, list_label_article, keywords_article = get_article_data(
        row_article["link_article"])
    # storing web scraping outputs in main_lists
    list_main_path_article.append(list_path_article)
    list_main_post_date.append(post_date)
    list_main_doc_title.append(doc_title)
    list_main_prps_article.append(str_prps_article)
    list_main_label_article.append(list_label_article)
    list_main_keywords_article.append(keywords_article)
    print(count)
    count = count + 1

df_article_scrape["path_article"] = list_main_path_article
df_article_scrape["post_date"] = list_main_post_date
df_article_scrape["article_title"] = list_main_doc_title
df_article_scrape["article_text"] = list_main_prps_article
df_article_scrape["article_label"] = list_main_label_article
df_article_scrape["article_keywords"] = list_main_keywords_article

df_article_scrape.to_csv(project_dir + "/data/processed/article_scrape_data.csv")
print("Completed!")
a = 5


