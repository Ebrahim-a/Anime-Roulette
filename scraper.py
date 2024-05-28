from requests_html import HTMLSession

class Scraper():
    def scrapedata(self, tag):
        url = f'https://www.livechart.me/spring-2024/tv{tag}'
        s=HTMLSession()
        r = s.get(url)
        print(r.status_code)

        qlist=[]

        anime = r.html.find('article.anime')

        for q in anime:
            try:
                
                item = {
                    'Anime': q.find('h3.main-title', first=True).text.strip(),
                    'Tag': ' '.join(q.find('ol.anime-tags', first=True).text.strip().split('\n'))

                }
                print(item)
                qlist.append(item)

            except UnicodeEncodeError:
                    pass
        return qlist
            

anime = Scraper()
anime.scrapedata('anime')