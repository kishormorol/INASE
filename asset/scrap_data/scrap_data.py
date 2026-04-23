import re
from asset.core import GetHtmlSoup, CheckDuplicateUrls
from datetime import datetime, timedelta
class ScrapNews:

    def ScrapMenuList(self, params:dict, idx: int = 0, root_url = None) -> dict:

        src_name = params['src_name']
        root_url = root_url if root_url is not None else params['root_url']
        soup = GetHtmlSoup(root_url)
        menus = soup.select(params['menu_selector'][idx])
        # print(menus)
        # for m in menus:
        #     print(f'{m.text.strip()} --> {m.get("href")}')
        menu = {}
        for m in menus:
            name = m.text.strip()
            href = m.get('href')
            # print(f'{name} --> {href}')
            # if href is not None:
            #     if 'http' not in href:
            #         url = root_url + href
            #         menu[name]=url
            if href is None:
                continue
            if src_name == 'observerbd' or src_name == 'timeofbangladesh':
                if '#' in href or '.html' in href:
                    print(f'Ignoring menu {name} with href {href}')
                    continue
                menu[name]=href
            if 'http' not in href and src_name != 'observerbd':
                url = root_url + href
                menu[name]=url
            else:
                menu[name]=href
            
        return menu
    
    def ScrapArticleUrls(self, base_url, menu_name, 
                         params:dict):
        soup = GetHtmlSoup(url=base_url)
        root_url = params['root_url']
        src_name = params['src_name']
        url_info = []
        for idx in range(len(params['article_url_selector'])):
            ignore_menu = params['article_url_selector'][idx]['ignore_menu']
            if menu_name in ignore_menu:
                print(f'Ignoring menu {menu_name}')
                return []
            # print(params['article_url_selector'][idx])
            card_selector = params['article_url_selector'][idx]
            # print(card_selector)
            card = soup.select(card_selector['card'])
            # print(card)
            count = 0
            # print(f'Number of card: {len(card)}')
            for c in card:
                
                # if count == 0:
                #     print(c.prettify())
                #     count += 1
                data = {}
                href = c.select_one(card_selector['href'])

                if href is not None:
                    href = href.get('href')
                else:
                    href = 'No URL'
                    continue

                title = c.select_one(card_selector['title'])
                if title is not None:
                    title = title.text.strip()
                else:
                    title = 'No Title'
                
                
                
                # time = c.find('span', "").text.strip()
                # ignr = 'hour(s)'
                # if ignr in time:
                #     hour = int(re.findall(r'\d+.?\d*', time)[0])
                #     dt = datetime.now() 
                #     prob_time = dt - timedelta(hours=hour)
                #     time = prob_time
                accepted_src = ['bdnews24', 'observerbd', 
                                'thebangladeshtoday', 'daily-sun', 
                                'dhakapost', 'timeofbangladesh']
                #if src_name == 'bdnews24' or src_name == 'observerbd' or src_name == 'thebangladeshtoday' or src_name == 'daily-sun' or src_name == 'dhakapost' or src_name== 'timeofbangladesh':
                if src_name in accepted_src:
                    url = href
                else:
                    url = root_url + href
                data['titles'] = title
                data['url'] = url
                #data['scrap_at'] = str(time)
                data['source'] = src_name
                data['menu_name'] = menu_name
                url_info.append(data)
            # new_urls = CheckDuplicateUrls(url_info)
            # print(f'Extracted {len(url_info)} article urls from menu {menu_name}')
        return url_info


    def ScrapArticleData(self, url, params:dict):
        
        soup = GetHtmlSoup(url)
        data = {}
        data['source'] = params['src_name']
        
        # Scrap Title
        title = soup.select_one(params['article_selector']['title'])
        if title is not None:
            title = title.text.strip()
        
        #Scrap Author
        author = soup.select_one(params['article_selector']['author'])
        if author is not None:
            author = author.text.strip()
            author = author.split('Photo')[0].strip()

        #Scrap Article
        article_text = ''
        article = soup.select(params['article_selector']['article'])
        if article is not None:
            for a in article:
                article_text = article_text + a.text.strip()
        


        acceped_src = ['dailystar', 'businessstandard', 'observerbd',
                        'thebangladeshtoday', 'daily-sun', 
                        'dhakapost', 'timeofbangladesh']
        
        #Scrap Date
        if params['src_name'] == 'bdnews24':
            dates = soup.find('div', 'pub-up print-section d-lg-flex').find_all('p')
            #print(dates)
            for i, d in enumerate(dates):
                spacific = d.find_all('span')
                """print('*' * 80)
                print(spacific)
                print('*' * 80)"""
                tem = ''
                count = 0
                for s in spacific:
                    ti = s.text.strip()
                    """print('=' * 80)
                    print(ti)
                    print('=' * 80)"""
                    
                    if count == 0 and i ==0:
                        tem = 'published'
                    elif count == 1 and i ==0:
                        #data[tem] = ti
                        time = ti
                    if count == 0 and i == 1:
                        tem = s.text.strip()
                        up = tem.split(' : ')
                        #data[up[0].lower()] = up[1]
                    count +=1
        
          
        #elif params['src_name'] == 'dailystar' or params['src_name'] == 'businessstandard' or params['src_name'] == 'observerbd' or params['src_name'] == 'thebangladeshtoday' or params['src_name'] == 'daily-sun' or params['src_name'] == 'dhakapost' or params['src_name'] == 'timeofbangladesh':
        elif params['src_name'] in acceped_src:    
            time = soup.select_one(params['article_selector']['time'])
            if time is not None:
                time = time.text.strip()
                time = time.replace("Published : ", "")
                time = time.replace("Published: ", "")
                ignr = 'hour(s)'
                if ignr in time:
                    hour = int(re.findall(r'\d+.?\d*', time)[0])
                    dt = datetime.now() 
                    prob_time = dt - timedelta(hours=hour)
                    time = prob_time
                 
            time = str(time)
        
        elif params['src_name'] == 'dhakatribune':
            time = soup.select_one(params['article_selector']['time'])
            #print(time)
            if time is not None:
                time = time.get('content')
            else:
                time = str(None)
        else:
            time = str(None)

                

        data['url'] = url
        data['title'] = title
        data['time'] = time
        #data['desc'] = desc
        data['author'] = author
        data['scrap_at'] = str(datetime.now())
        data['full_article'] = article_text
        return data



        