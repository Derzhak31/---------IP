import requests
from pyfiglet import Figlet
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Провайдер]': response.get('isp'),
            '[Организация]': response.get('org'),
            '[Страна]': response.get('country'),
            '[Регион]': response.get('regionName'),
            '[Город]': response.get('city'),
            '[Индекс]': response.get('zip'),
            '[Широта]': response.get('lat'),
            '[Долгота]': response.get('lon')
        }

        for k, v in data.items():
            print(f'{k} : {v}')
            
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP Info'))
    ip = input('Please enter a target IP: ')

    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
