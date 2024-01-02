from db.models import *
from slugify import slugify
from lib.scraper import get_manga_info, get_latest_chapter, get_manga_list
import os


# all web-manga related ops in scraper.py, this only contains db logic
def get_subbed_mangas(uname : str):
    try:
        database.connect(reuse_if_open=True)
        user = Profile.get(Profile.username==uname)
    except Exception as e:
        raise Exception(f"The required profile could not be found : {str(e)}")
    user_mangas = user.mangas.order_by(Manga.name)
    database.close()
    return user_mangas

# the manga parameter is a parsed DOM object from bs4 here
def subscribe_to_manga(manga, sub_name):
    try:
        database.connect(reuse_if_open=True)
        mtitle, mlink = get_manga_info(manga)
        latest_chap = get_latest_chapter(mlink)
        manga, created = Manga.get_or_create(name = mtitle)
        manga.latest_chapter = latest_chap
        sub = Profile.get(Profile.username == sub_name)
        manga.subscribers.add(sub)
        manga.save()
        database.close()
    except Exception as e:
        database.close()
        raise Exception(str(e))

#the manga parameter is a database object here
def is_chapter_released(manga):
    try:
        database.connect(reuse_if_open=True)
        title = manga.name
        chap_in_db = manga.latest_chapter
        mlist = get_manga_list(title)
        # will give most accurate response as it is direct keyword search, can confidently use mlist[0]
        _, mlink = get_manga_info(mlist[0])
        latest_chap = get_latest_chapter(mlink)
        rel_manga = Manga.get(name=title)
        rel_manga.chap_in_db = latest_chap
        rel_manga.save()
        database.close()
        return latest_chap != chap_in_db, latest_chap
    except Exception as e:
        database.close()
        raise e




