from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import time
import pandas as pd

header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

def scrape_articles(start, COOLDOWN):
    articles = []
   
    for i in range (start,COOLDOWN):
        try:
            url = f'https://www.wired.com/most-recent/?page={i}'
            result_text = requests.get(url).text   
            soup = BeautifulSoup(result_text, 'lxml')
            news_articles = soup.find_all('div', class_ ='SummaryItemWrapper-gcQMOo eJhumH summary-item summary-item--has-margin-spacing summary-item--has-border summary-item--article summary-item--no-icon summary-item--text-align-left summary-item--layout-placement-side-by-side-desktop-only summary-item--layout-position-image-left summary-item--layout-proportions-33-66 summary-item--side-by-side-align-top summary-item--side-by-side-image-right-mobile-true summary-item--standard SummaryItemWrapper-bGtGFH klkoMz summary-list__item')


            for news_article in news_articles:
                news_article_headline = news_article.find('h3',class_='SummaryItemHedBase-dZZTtv fCrIUA summary-item__hed').text             
                url2 = "https://www.wired.com"
                article_link = news_article.div.a['href']
                article_links = urljoin(url2,article_link)
                articles.append([news_article_headline, article_links])

            # for link in article_links:
            #     r = requests.get(link, headers = header)
            #     soup = BeautifulSoup(link.content,'lxml')
            #     date = soup.find('time', class_='BaseWrap-sc-UrHlS BaseText-fFrHpW ContentHeaderTitleBlockPublishDate-khXePI boMZdO eWfDvD gqmbtB').text.strip()
            #     print("Debugging")
            #     print(date)

        except: 
            time.sleep(5)
            continue 

    file = open('articles.html', 'w')
    df = pd.DataFrame(articles, columns=['Title', 'Link'])
    df.to_html(file)
    print(df)
    file.close()
    

if __name__ == "__main__":
    COOLDOWN = 35
    scrape_articles(1, COOLDOWN)
    


    
