from telegraph import Telegraph
import requests
from bs4 import BeautifulSoup
import cssutils
import html_content as doc


if __name__ == '__main__':
    telegraph = Telegraph()
    telegraph.create_account(short_name='1337')

    url = 'https://aeon.co/essays/tools-and-voyages-suggest-that-homo-erectus-invented-language'

    # 1) Загрузить статью в файл
    r = requests.get(url)
    with open('article.html', 'w', encoding="utf-8") as output_file:
        output_file.write(r.text)

    # 2) Открыть файл на чтение
    with open("article.html", "r", encoding="utf-8") as f:
        source_content = f.read()

    # 3) Извлечь название статьи
    article_title = doc.get_article_name(source_content)

    # 5) Извлечь html контент
    html_doc = doc.get_fixed_html_content(str(source_content))

    response = telegraph.create_page(
        article_title,
        html_content=html_doc
    )

    print('https://telegra.ph/{}'.format(response['path']))
