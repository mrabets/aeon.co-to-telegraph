from telegraph import Telegraph
import requests
from bs4 import BeautifulSoup
import cssutils


def read_file(filename):
    with open(filename, encoding="utf-8") as input_file:
        text = input_file.read()
    return text


def get_html_content(url):
    temp_str = '<img src="https://epsilon.aeon.co/images/3958ed96-fadb-4678-9636-716c1efd4372/header_essay-anti' \
               '-slavery-picnic-at-weymouth-landing_-massachusetts-eb16da06-fb8c-b1c5-fcce-1582c1a5d30a.jpg" ' \
               'alt="" title="" ' \
               'class="ld-image-block">' \
               '<p>Detail of <em>Anti-Slavery Picnic at Weymouth Landing, Massachusetts</em> (<em>c</em>1845) ' \
               'by Susan Torrey Merritt. <a ' \
               'href="https://www.artic.edu/artworks/73987/anti-slavery-picnic-at-weymouth-landing' \
               '-massachusetts" target="_blank" rel="noreferrer noopener"><em>Courtesy the Art Institute of ' \
               'Chicago</em></a></p> ' \
               '<p>The United States, people around the world say, was founded by Puritans. The Puritan ' \
               'colonists were inspired by ‘the magnificence of leading an exodus of saints to found a <em>city ' \
               'on a hill</em> [my emphasis], for the eyes of all the world to behold.' \
               'Those are the words of Perry Miller, the 20th century ' \
               'pre-eminent scholar on the subject, interpreting John Winthrop, the first governor of ' \
               'Massachusetts, and author of this undying metaphor. Miller believed that Winthrop was ' \
               '‘preternaturally sensing … the promise of America’. Politicians from Jack Kennedy to Ronald ' \
               'Reagan have exploited Winthrop’s image for their own visions of the promise of America, ' \
               'as have countless op-ed columnists and historians. It’s difficult to find an American history ' \
               'textbook today that does <em>not</em> claim that Winthrop spoke these words in a shipboard ' \
               'sermon to his fellow colonists crossing the Atlantic in 1630. But it’s not true.’</p>' \
               '<blockquote>Boston built itself as a quasi-autonomous city-state with an expansive ' \
               'regional hinterland</blockquote>' \
               '<figure><img src="https://d2e1bqvws99ptg.cloudfront.net/user_image_upload/1530/insert-harbour' \
               '-commonwealth_cn69ms76r_productionMaster.jpg" alt="" title="" ' \
               'class="ld-image-block"><figcaption class="ld-image-caption"><em>View of the Long Warf &amp; ' \
               'port of the harbour of Boston in New England, America</em> by R Byron circa 1754. <em>Courtesy ' \
               'Digital Commonwealth/Massachusetts Collections online</em></figcaption></figure> '

    # background = html.fromstring()

    return temp_str

# def get_main_html_content(article_url):
#     r = requests.get(article_url)
#     with open('test.html', 'w', encoding="utf-8") as output_file:
#         output_file.write(r.text)
#
#     with open("test.html", "r", encoding="utf-8") as f:
#         contents = f.read()
#
#     soup = BeautifulSoup(contents, 'html.parser')
#
#     article_title = soup.find("h1", class_="article-card__title")


if __name__ == '__main__':
    telegraph = Telegraph()
    telegraph.create_account(short_name='1337')

    url = 'https://aeon.co/essays/new-england-kept-slavery-but-not-its-profits-at-a-distance'

    # 1) Загрузить статью в файл
    r = requests.get(url)
    with open('article.html', 'w', encoding="utf-8") as output_file:
        output_file.write(r.text)

    # 2) Открыть файл на чтение
    with open("article.html", "r", encoding="utf-8") as f:
        source_content = f.read()

    # 3) Извлечь название статьи
    soup = BeautifulSoup(source_content, 'html.parser')
    article_title = soup.find("h1", class_="article-card__title")

    # 4) Извлечь фон статьи
    background_image = soup.find('figure')['style']
    style = cssutils.parseStyle(background_image)
    url = style['background-image']
    url = url.replace('url(', '').replace(')', '')

    # 5) Извлечь html контент
    article_content = soup.find("div", class_="has-dropcap")

    soup = BeautifulSoup(str(article_content), "html.parser")

    # 1. find the <span> tag to replace:
    span = soup.find("span", class_="ld-nowrap")

    # 2. create new <em> tag with the same contents as <span>
    em = soup.new_tag("em")
    # em.contents = span.contents
    for i in span.children:
        print(i)
    # 3. replace the tag inside the tree
    # span.replace_with(em)
    # print(soup)

    #em_tag = '<em>{0}</em>'.format(span_content)
    #tag = span_content
    #tag.name = "em"

    # for x in soup.find_all('span', class_='ld-nowrap'):
    #     print('<em>' + x.text + '</em>')

    #del tag['class']

   # print(span_content)

    # tag = soup.h1
    #
    # tag.name = "h3"
    # del tag['class']

    # response = telegraph.create_page(
    #     article_title.text,
    #     html_content='<img src="{0}" alt="альтернативный текст">'.format(url) + str(article_content)
    # )
    #
    # print('https://telegra.ph/{}'.format(response['path']))
