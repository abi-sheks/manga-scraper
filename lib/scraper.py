import requests
from bs4 import BeautifulSoup
from slugify import slugify
import os 

LATEST_CHAPTER_INDEX = 3

def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def get_manga_list(mname : str):
    manga_title = slugify(mname)
    url = str(os.getenv("SEARCH_LINK")) + manga_title
    soup = get_soup(url)
    manga_lists = soup.find_all("div", class_="panel-list-story")
    if len(manga_lists) != 1:
        print("Not possible")
        raise Exception("Website response is invalid")
    mangas = manga_lists[0].find_all("div", class_="list-story-item")
    return mangas

def display_manga_choices(manga_list):
    index = 0
    for item in manga_list:
        print(f"{index} > {item.div.h3.a.attrs['title']}")
        index += 1

def get_manga_info(manga):
    # expects the manga dom object
    mtitle = manga.div.h3.a.attrs['title']
    mlink = manga.div.h3.a.attrs['href']
    return mtitle, mlink

def get_latest_chapter(manga_link):
    manga_page = get_soup(manga_link)
    manga_details = manga_page.find_all("div", class_="story-info-right-extent")
    if len(manga_details) != 1:
        raise Exception("Website response is invalid")
    #second span of updated div contains latest chapter info
    latest_chapter = manga_details[0].find_all("p")[LATEST_CHAPTER_INDEX].find_all('span')[1].text
    return latest_chapter


    

        

