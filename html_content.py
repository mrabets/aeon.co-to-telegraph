import requests
from bs4 import BeautifulSoup
import cssutils


def get_fixed_html_content(content):
    background_image = get_background_image(content)
    temp_soup = BeautifulSoup(content, 'html.parser')
    doc = str(temp_soup.find("div", class_="has-dropcap"))
    doc = change_tag(doc, "span", "ld-nowrap", "em")
    doc = change_tag(doc, "span", "ld-dropcap", "em")
    doc = change_tag(doc, "p", "pullquote", "blockquote")
    doc = change_tag(doc, "sub", "ld-subscript", "em")
    doc = unwrap_tag(doc, "div", "has-dropcap")
    doc = extract_tag(doc, "div", "newsletter-signup newsletter-signup--wide")
    return background_image + doc


def get_article_name(content):
    temp_soup = BeautifulSoup(content, 'html.parser')
    article_title = temp_soup.find("h1", class_="article-card__title")
    return article_title.text

def get_background_image(content):
    temp_soup = BeautifulSoup(content, 'html.parser')
    background_image = temp_soup.find('figure')['style']
    style = cssutils.parseStyle(background_image)
    url = style['background-image']
    url = url.replace('url(', '').replace(')', '')
    return '<img src="{0}">'.format(url)

def change_tag(content, current_tag_name, class_name, new_tag_name):
    temp_soup = BeautifulSoup(content, "html.parser")

    for current in temp_soup.find_all(current_tag_name, class_=class_name):
        new = temp_soup.new_tag(new_tag_name)
        new.contents = current.contents
        current.replace_with(new)

    return str(temp_soup)


def unwrap_tag(content, tag_name, class_name):
    temp_soup = BeautifulSoup(content, "html.parser")

    tag = temp_soup.find(tag_name, class_=class_name)
    tag.unwrap()

    return str(temp_soup)


def extract_tag(content, tag_name, class_name):
    temp_soup = BeautifulSoup(content, "html.parser")

    tag = temp_soup.find(tag_name, class_=class_name)
    tag.extract()

    return str(temp_soup)