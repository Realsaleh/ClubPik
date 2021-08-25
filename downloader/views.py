import requests
import re
from bs4 import BeautifulSoup
from django.shortcuts import render


def Home(request):
    if 'username' in request.GET:
        try:
            username = request.GET.get('username')
            USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
            session = requests.Session()
            session.headers['User-Agent'] = USER_AGENT
            html_content = session.get(f'https://www.clubhouse.com/@{username}').text
            soup = BeautifulSoup(html_content, 'html.parser')
            get_tag = str(soup.find_all("div",class_='w-18 h-18 sm:w-20 sm:h-20 bg-gray-200 mx-auto bg-center bg-cover border border-gray-400 rounded-ch'))
            extract_url = re.findall(r'(https?://\S+)', get_tag)
            url = extract_url[0].replace("""_thumbnail_250x250')"></div>]""", "")
            return render(request, 'downloader/result.html', {'url': url})
        except IndexError:
            url = "Error...!"
            return render(request, 'downloader/error.html', {'url': url})
    else:
        return render(request, 'downloader/home.html')
