import os
import json
import copy
import time
from datetime import datetime
from asset.hyperparameters import params
from asset.core import CheckDuplicateUrls
from asset.scrap_data.scrap_data import ScrapNews
from config.db_manage import DBmanage

scraper = ScrapNews()
sources = params['sources']

url_counter = 0
article_counter = 0
start_time = time.time()
for i, src in enumerate(sources):
    #src = sources[0]

    
    par = params['source_selectors'][src]
    #print(par)
    print('='*80)
    print(' ' * 30, f'{i+ 1}. Scraping {src} ')
    print('='*80)
    menu_selector = par['menu_selector']
    for idx, menu in enumerate(menu_selector):
        if idx == 0:
            menu_list = scraper.ScrapMenuList(params=par, idx=idx)
            temp_menu_list = menu_list.copy()
        elif idx > 0:
            for k, v in temp_menu_list.items():
                menu_list.update(scraper.ScrapMenuList(params=par, idx=idx, root_url=v))
                
    # menu_list = scraper.ScrapMenuList(params=par)
    # print(menu_list)
    urls = []
    for menu_name, base_url in menu_list.items():
        article_urls = scraper.ScrapArticleUrls(base_url=base_url, menu_name=menu_name, params=par)
        urls.extend(article_urls)

    url_collection_name = par['url_collection_name']
    new_urls = CheckDuplicateUrls(urls, src_name=src,
                                  collection_name = url_collection_name)
    url_counter += len(new_urls)
    if len(new_urls) == 0:
        print('*' * 60)
        print(f'No new urls found for {src}. Skipping article scraping.')
        print('*' * 60)
        continue
    print('*' * 60)
    print(' ' * 20, 'Strart Article Scraping')
    print('*' * 60)

    articles = []
    for idx, url in enumerate(new_urls):
        if idx % 10 == 0:
            print(f'Scraping article {idx+1} out of {len(new_urls)}')
        data = scraper.ScrapArticleData(url=url, params=par)
        articles.append(data)
    #article = scraper.ScrapArticleData(url=new_urls, params=par)

    # articles_copy = copy.deepcopy(articles)

    article_counter += len(articles)
    #collection_name = f'{src}_article'
    collection_name = par['art_collection_name']
    DBmanage(collection_name=collection_name, data=articles)


    # root = params['output_url_path'] + '/articles/'+ src
    # os.makedirs(root, exist_ok = True)
    # path = f'{root}/{str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))}_articles.json'
    # #print(articles_copy)
    # with open(path, 'w', encoding='utf-8') as f:
    #     json.dump(articles_copy, f, ensure_ascii=False, indent=4)
    # #print(f'Extracted {len(urls)} article urls')"""

end_time = time.time()
total_time = end_time - start_time
minute = total_time // 60
second = total_time % 60
print('*' * 60 )
print(f'Total Scrap number of source  : {i + 1}' )
print(f'Total Scrap  number of urls   : {url_counter}' )
print(f'Total Scrap number of articles: {article_counter}' )
print('*' * 60 )

print('='*80)
print(' ' * 20, f'Total time taken: {minute:.0f} minutes and {second:.2f} seconds')
print('='*80)