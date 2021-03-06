from selenium import webdriver
from pathlib import Path
import time
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

def func_view_more(page_link):
    project_dir = str(Path(__file__).resolve().parents[2])
    PATH = project_dir + "/references/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(page_link)

    view_more_btn_selector = '#generic-content > div > div > div > div > div > div.newsCentreList.section > div.card > div > a'

    while True:
        try:
            view_more_button = driver.find_element_by_css_selector(view_more_btn_selector)
            time.sleep(5)
            view_more_button.click()
            time.sleep(7)
            print("Expanded")
        except Exception as e:
            break

    print("Complete")
    html = driver.page_source
    time.sleep(3)
    driver.quit()

    return html

#func_view_more("https://www.et.undp.org/content/ethiopia/en/home/blog.html")

# https://www.sz.undp.org/content/eswatini/en/home/blog.html view more link     #view more count 1
# https://www.et.undp.org/content/ethiopia/en/home/blog.html    #view more count 2 working