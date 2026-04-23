import os
import ast
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from asset.hyperparameters import params
from config.db_manage import DBmanage
from config.crud_operation import DBManager


def GetHtmlSoup(url):
    # print(f'Getting html content from {url}')
    content = requests.get(url, headers=params['headers']).text
    soup = BeautifulSoup(content, 'html.parser')
    """with open('dailystyar.html', 'w', encoding='utf-8') as f:
        f.write(content)"""
    return soup


def CheckInternalDuplicateUrls(new_data:list[dict], prev_urls:list[str]) -> list:
    # print(prev_urls)
    url_data = []
    just_urls = []
    for idx, url in enumerate(prev_urls):
        if url not in just_urls:
            url_data.append(new_data[idx])
            just_urls.append(url)
    print('=' * 40)
    print(f'Internal Duplicate urls : {len(prev_urls) - len(just_urls)}')
    print(f'Unique urls             : {len(just_urls)}')
    print('=' * 40)
    return url_data, just_urls


"""def CheckDuplicateUrls(new_data:list, src_name:str, collection_name:str) -> list:


    date = str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

    root_path = f'{params["output_url_path"]}/urls'
    src_root_path = f'{root_path}/{src_name}'

    os.makedirs(root_path,exist_ok=True)
    os.makedirs(src_root_path,exist_ok=True)


    root_data_path = f'{root_path}/urls.json'
    src_root_data_path = f'{src_root_path}/urls.json'
    src_path = f'{src_root_path}/{date}_urld.json'

    print(src_root_data_path)
    if os.path.exists(src_path) == False:
        with open(src_path, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)

    if os.path.exists(src_root_data_path) == False:
        with open(src_root_data_path, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)


    if os.path.exists(root_data_path) == False:
        with open(root_data_path, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)

    with open(root_data_path, 'r', encoding='utf-8') as f:
        root_text = f.read()

    with open(src_root_data_path, 'r', encoding='utf-8') as f:
        text = f.read()


    prev_data = ast.literal_eval(text)
    print(f'Previous scrap urls : {len(prev_data)}')
    prev_root_data = ast.literal_eval(root_text)
    #print(prev_data)
    urls = []
    just_urls = []
    prev_urls = [data['url'] for data in prev_data]
    new_urls = [data['url'] for data in new_data]
    for idx, url in enumerate(new_urls):
        if url not in prev_urls:
            urls.append(new_data[idx])
            just_urls.append(url)
    print('-' * 60)
    print(f'Source Previous scrap urls    : {len(prev_data)}')
    print(f'Root Previous selected urls   : {len(prev_root_data)}')
    print(f'Source New selected urls      : {len(urls)}')

    urls, just_urls = CheckInternalDuplicateUrls(new_data=urls, prev_urls=just_urls)
    
    prev_data.extend(urls)

    prev_root_data.extend(urls)
    # print('*' * 60)
    # print(prev_data)
    # print('*' * 60)
    # print(prev_root_data)
    # print('*' * 60)

    with open(src_path, 'w', encoding='utf-8') as f:
        json.dump(urls, f, ensure_ascii=False, indent=4)


    with open(src_root_data_path, 'w', encoding='utf-8') as f:
        json.dump(prev_data, f, ensure_ascii=False, indent=4)

    
    with open(root_data_path, 'w', encoding='utf-8') as f:
        json.dump(prev_root_data, f, ensure_ascii=False, indent=4)
    
    #collection_name = f'{src_name}_urls'
    root_collection_name = f'urls'
    DBmanage(collection_name=collection_name, data=urls)
    DBmanage(collection_name=root_collection_name, data=urls)

    print(f'Source Total  urls            : {len(prev_data)}')
    print(f'Root Total  urls              : {len(prev_root_data)}')
    print('-' * 60)
    return just_urls"""


def CheckDuplicateUrls(new_data:list, src_name:str, collection_name:str) -> list:

    db = DBManager(collection_name=collection_name)
    root_db = DBManager(collection_name='urls')
    prev_data = db.FindAll()
  
    # prev_data = ast.literal_eval(text)
    # print(f'Previous scrap urls : {len(prev_data)}')

    prev_root_data = root_db.CountDocuments()

    # prev_root_data = ast.literal_eval(root_text)
    #print(prev_data)
    urls = []
    just_urls = []
    prev_urls = [data['url'] for data in prev_data]
    new_urls = [data['url'] for data in new_data]
    for idx, url in enumerate(new_urls):
        if url not in prev_urls:
            urls.append(new_data[idx])
            just_urls.append(url)
    print('-' * 60)
    print(f"Numbers of New urls           : {len(new_data)}")
    print(f'Source Previous scrap urls    : {len(prev_data)}')
    print(f'Root Previous selected urls   : {prev_root_data}')
    print(f'Source New selected urls      : {len(urls)}')

    urls, just_urls = CheckInternalDuplicateUrls(new_data=urls, prev_urls=just_urls)
    
    # print('*' * 60)
    # print(prev_data)
    # print('*' * 60)
    # print(prev_root_data)
    # print('*' * 60)

    
    #collection_name = f'{src_name}_urls'
    root_collection_name = f'urls'
    ids = DBManager(collection_name=collection_name).InsertMany(urls)
    print(f'Inserted data on {collection_name}: {len(ids)}')
    ids = root_db.InsertMany(urls)
    print(f'Inserted data on {root_collection_name}: {len(ids)}')
    # DBmanage(collection_name=collection_name, data=urls)
    # DBmanage(collection_name=root_collection_name, data=urls)

    print('-' * 60)
    return just_urls
