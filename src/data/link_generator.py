import pandas as pd
import requests
from project_dir_helper import project_dir




# getting necessary data for creating links
df_country_codes = pd.read_csv(project_dir+"/data/raw/codes_countries_COs.csv", index_col=0)
df_link_templates = pd.read_excel(project_dir+"/data/raw/link_templates.xlsx")
list_link = []  # storing links
list_type_link = []  # storing types of link pages
list_link_status = []
step_counter = 0

for index_link, row_link in df_link_templates.iterrows():  # iteration to create COs' page links
    for index_country, row_country in df_country_codes.iterrows():
        temp_link = row_link["first part"] + row_country["code"] + \
                    row_link["second part"] + str(row_country["country"]) + \
                    row_link["third part"]  # NOTE: empty country codes might cause // link generation. Should be resolved
        list_link.append(temp_link)  # adding temporary links to link_list
        list_type_link.append(row_link['type'])  # adding type of pages to list_type_link


# list_link = list_link[0:10] # for reducing data size
# list_type_link = list_type_link[0:10]


def get_url_status(url):  # checks status for each url in list urls
    try:
        r = requests.get(url)
        temp_status = str(r.status_code)
    except Exception as e:
        temp_status = "Failed to connect"
    return temp_status


for link in list_link:
    status_check = get_url_status(link)
    list_link_status.append(status_check)
    step_counter = step_counter + 1
    print(step_counter)  # step counter stand just for not get bored while compiling

df_link_COs = pd.DataFrame(
    {'link': list_link, 'link_type': list_type_link, 'status': list_link_status})  # storing links and page type of COs
df_link_COs.to_excel(project_dir+"/data/interim/output_links.xlsx")



print("OK")

