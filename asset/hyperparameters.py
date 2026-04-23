params = {
    'headers': {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9"
    },
    'sources': ['bdnews24', 'dailystar', 'dhakatribune',
                'observerbd', 'businessstandard', 'thebangladeshtoday',
                'daily-sun', 'dhakapost', 'timeofbangladesh'],
    # 'sources': ['timeofbangladesh'],
    'output_url_path': 'data',
    'output_article_path': 'data/articles',
    'source_selectors': 
    {
        'bdnews24': {
            'src_name': 'bdnews24',
            'root_url': 'https://bdnews24.com',
            'url_collection_name': 'bdnews24_urls',
            'art_collection_name': 'bdnews24_article',
            'menu_selector' : ["div.main-menu nav li a"],
            'article_url_selector':
            [
                {
                    'card': 'div.readMore-wrapper div#data-wrapper div.col-md-3',
                    'title': 'h5',
                    'href': 'a',
                    'ignore_menu': []
                }
            ],
            'article_selector': 
            {
                'title': 'div.details-title h1',
                'author': 'div.author-name-wrap',
                'article': 'div.details-brief p'
            }
        },

        'dailystar': {
            'src_name': 'dailystar',
            'root_url': 'https://www.thedailystar.net',
            'url_collection_name': 'dailystar_urls',
            'art_collection_name': 'dailystar_article',
            'menu_selector': ['div.mega-menu-wrapper li.has-submenu li a'],
            'article_url_selector':
            [
                {
                    'card': '.grid .relative .card-content',
                    'title': 'a',
                    'href': 'a',
                    'ignore_menu': []
                }
            ],
            'article_selector': 
            {
                'title': 'div.block-field-blocknodenewstitle h1',
                'author': 'div.block-author-info-block span.font-medium',
                'time': 'div.block-article-meta-block span.text-gray-600',
                'article': 'div.block-field-blocknodenewsbody p'
            }
        },

        'dhakatribune': {
            'src_name': 'dhakatribune',
            'root_url': 'https://www.dhakatribune.com',
            'url_collection_name': 'dhakatribune_urls',
            'art_collection_name': 'dhakatribune_article',
            'menu_selector': ['div.main_menu ul li a'],
            'article_url_selector':
            [
                {
                    'card': 'div.summery_view h2.title',
                    'title': 'a',
                    'href': 'a',
                    'ignore_menu': []
                }
            ],
            'article_selector': 
            {
                'title': 'div.content_detail_small_width1 div.col_in h1.title',
                'author': 'div.additional_info_container  div.each_author a.name span',
                'time': 'div.additional_info_container_inner div.time span.tts_time',
                'article': 'article.jw_detail_content_holder p'
            }
        },

        'observerbd' : {
            'src_name': 'observerbd',
            'root_url': 'https://www.observerbd.com/',
            'url_collection_name': 'observerbd_urls',
            'art_collection_name': 'observerbd_article',
            'menu_selector': ['li.m_none a'],
            'article_url_selector':
            [
                {
                    'card': 'div.container div.col-lg-8 div.title_inner',
                    'title': 'a',
                    'href': 'a',
                    'ignore_menu': []
                }
            ],
            'article_selector': 
            {
                'title': 'div#toPrint h1.color',
                'author': 'div#toPrint div.credit span',
                'time': 'div#toPrint div.pub span',
                'article': 'div#toPrint div#f',
                
            }
        },

        'businessstandard': {
            'src_name': 'businessstandard',
            'root_url': 'https://www.tbsnews.net',
            'url_collection_name': 'businessstandard_urls',
            'art_collection_name': 'businessstandard_article',
            'menu_selector': ['div.top-bar-right ul#main-menu li a'],
            'article_url_selector':
            [
                {
                    'card': 'div.pane-content div.view-content .card-title ',
                    'title': 'a',
                    'href': 'a',
                    'ignore_menu': []
                }
            ],
            'article_selector': 
            {
                'title': 'header h1',
                'author': 'div.author-section div.author-name',
                'time': 'div.author-section div.date',
                'article': 'p.rtejustify'
            }
        },

        'thebangladeshtoday': {
            'src_name': 'thebangladeshtoday',
            'root_url': 'https://thebangladeshtoday.com',
            'url_collection_name': 'thebangladeshtoday_urls',
            'art_collection_name': 'thebangladeshtoday_article',
            'menu_selector': ['div.menu-main-menu-container a'],
            'article_url_selector':
            [
                {
                    'card': 'div.oxy-dynamic-list div.ct-div-block ',
                    'title': 'div',
                    'href': 'a',
                    'ignore_menu': ['Bangla Edition']
                }
            ],
            'article_selector': 
            {
                'title': 'h1#headline-7-24729 span#span-8-24729',
                'author': 'none',
                'time': 'span#span-211-24729',
                'article': 'div#text_block-22-24729 p'
            }
        },

        'daily-sun': {
            'src_name': 'daily-sun',
            'root_url': 'https://www.daily-sun.com',
            'url_collection_name': 'daily-sun_urls',
            'art_collection_name': 'daily-sun_article',
            'menu_selector': ['div.headerMenu li a',
                              'div.desktopSubCategoryDiv h2 a'],
            'article_url_selector':
            [
                {
                    'card': 'div.desktopSectionListMedia div.media',
                    'title': 'h2',
                    'href': 'a',
                    'ignore_menu': []
                },
                {
                    'card': 'div.col-md-9 div.desktopSectionLead',
                    'title': 'h2',
                    'href': 'a',
                    'ignore_menu': []
                }
            ],
            'article_selector': 
            {
                'title': 'div.col-sm-10 h1.detailHeadline',
                'author': 'none',
                'time': 'div.displayInlineBlock span.publishedTime',
                'article': 'div.col-md-7 div.desktopDetailBody p'
            }
        },

        'dhakapost':{
            'src_name': 'dhakapost',
            'root_url': 'https://en.dhakapost.com',
            'url_collection_name': 'dhakapost_urls',
            'art_collection_name': 'dhakapost_article',
            'menu_selector': ['div.navbar-collapse li.nav-item a'],
            'article_url_selector':
            [
                {
                    'card': 'div.cat-lead-container div.lead-news',
                    'title': 'h2',
                    'href': 'a',
                    'ignore_menu': ['Prayer Time']
                },
                {
                    'card': 'div.cat-lead-container div.col-12',
                    'title': 'h2',
                    'href': 'a',
                    'ignore_menu': ['Prayer Time']
                },
                {
                    'card': 'div.more-contents div.col-sm-4',
                    'title': 'h2',
                    'href': 'a',
                    'ignore_menu': ['Prayer Time']
                }
            ],
            'article_selector': 
            {
                'title': 'h1.news-title',
                'author': 'p.author',
                'time': 'div.d-flex p.news-time',
                'article': 'div.news-details p'
            }
        },

        'timeofbangladesh' : {
            'src_name': 'timeofbangladesh',
            'root_url': 'https://tob.news',
            'url_collection_name': 'timeofbangladesh_urls',
            'art_collection_name': 'timeofbangladesh_article',
            'menu_selector': ['nav.navigation li.menu-item a'],
            'article_url_selector':
            [
                {
                    'card': 'div.block-content div.loop div.post-meta h2',
                    'title': 'a',
                    'href': 'a',
                    'ignore_menu': []
                },
                {
                    'card': 'div.block-content div.post-meta h3',
                    'title': 'a',
                    'href': 'a',
                    'ignore_menu': []
                }
                
            ],
            'article_selector': 
            {
                'title': 'div.the-post-header h1.is-title',
                'author': 'div.featured div.wp-caption-text',
                'time': 'div.the-post-header time.post-date',
                'article': 'div.post-content-wrap div.post-content p'
            }
        }

    }  
}