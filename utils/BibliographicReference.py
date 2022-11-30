from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json


# class BibliographicReference:
#     def __init__(self):
#         self.youtube_title: str = None
#         self.youtube_chanel_name: str = None
#         self.youtube_date: str = None
#
#
# def get_html(url: str):
#     """Формирует и возвращает объект bs4 из html страницы, полученной по указанному url."""
#     html = requests.get(url).content
#     soup = BeautifulSoup(html, 'html.parser')
#     return soup


if __name__ == '__main__':
    """
https://youtu.be/r_Wf532f5X4
прсомотрено 25.10.2022
    """
    youtube_url = 'https://youtu.be/r_Wf532f5X4'
    response = requests.request("GET", youtube_url)
    soup = BeautifulSoup(response.text, "html.parser")
    body = soup.find_all("body")[0]
    scripts = body.find_all("script")

    result = json.loads(scripts[0].string[30:-1])

    print(result['videoDetails']['title'])
    print(result['annotations'][0]['playerAnnotationsExpandedRenderer']['featuredChannel']['channelName'])
    print(result['microformat']['playerMicroformatRenderer']['publishDate'])
    print(result['microformat']['playerMicroformatRenderer']['uploadDate'])

    date_str = result['microformat']['playerMicroformatRenderer']['publishDate']
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')

    channel = result['annotations'][0]['playerAnnotationsExpandedRenderer']['featuredChannel']['channelName']
    year = date_obj.year
    title = result['videoDetails']['title']
    day = date_obj.day
    month = date_obj.month
    viewed = '25.10.2022'  # заполнить вручную

    print(f'*{channel}*. ({year}) {title} \[ПОЯСНЕНИЕ ЗАПОЛНИТЬ] // YouTube. {day} {month} ({youtube_url}). Просмотрено: {viewed}')
