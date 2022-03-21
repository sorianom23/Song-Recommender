
def strip_hot_songs (url):
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import numpy as np
    
    titles = []
    artists = []
    
    for i in soup.select("li.o-chart-results-list__item > h3"):
        titles.append(i.get_text().strip())
    
    for i in soup.select("li.o-chart-results-list__item > span:nth-child(2)"):
        artists.append(i.get_text().strip())
    
    artists = [x for x in artists if x != "NEW"]
    titles = [x for x in titles if x != "RE-ENTRY"]
    
    hot100 = pd.DataFrame({
                        "title":titles,
                        "artist":artists
                      })
    hot100.to_csv("hot100.csv", index=False)

def strip_hot_songs (url):
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import numpy as np
    
    titles = []
    artists = []
    
    for i in soup.select("li > h3"):
        titles.append(i.get_text().strip())
    
    for i in soup.select("li > span:nth-child(2)"):
        artists.append(i.get_text().strip())
    
    artists = [x for x in artists if x != "NEW"]
    titles = [x for x in titles if x != "RE-ENTRY"]
    
    hot100 = pd.DataFrame({
                        "title":titles,
                        "artist":artists
                      })
    hot100.to_csv("hot100.csv", index=False)

def scrape_hot100 (url):
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import numpy as np
    
    titles = []
    artists = []
    
    for i in soup.select("li.o-chart-results-list__item > h3"):
        titles.append(i.get_text().strip())
    
    for i in soup.select("li.o-chart-results-list__item > span:nth-child(2)"):
        artists.append(i.get_text().strip())
    
    artists = [x for x in artists if x != "NEW"]
    titles = [x for x in titles if x != "RE-ENTRY"]
    
    hot100 = pd.DataFrame({
                        "title":titles,
                        "artist":artists
                      })
    hot100.to_csv("hot100.csv", index=False)

def scrape_hot100 (url):
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import numpy as np
    
    titles = []
    artists = []
    
    for i in soup.select("li.o-chart-results-list__item > h3"):
        titles.append(i.get_text().strip())
    
    for i in soup.select("li.o-chart-results-list__item > span:nth-child(2)"):
        artists.append(i.get_text().strip())
    
    artists = [x for x in artists if x != "NEW"]
    titles = [x for x in titles if x != "RE-ENTRY"]
    
    scrape_hot100 = pd.DataFrame({
                        "title":titles,
                        "artist":artists
                      })
    scrape_hot100.to_csv("scrape_hot100.csv", index=False)

def scrape_hot100 (url):
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import numpy as np
    
    titles = []
    artists = []
    
    for i in soup.select("li.o-chart-results-list__item > h3"):
        titles.append(i.get_text().strip())
    
    for i in soup.select("li.o-chart-results-list__item > span:nth-child(2)"):
        artists.append(i.get_text().strip())
    
    artists = [x for x in artists if x != "NEW"]
    titles = [x for x in titles if x != "RE-ENTRY"]
    
    scrape_hot100 = pd.DataFrame({
                        "title":titles,
                        "artist":artists
                      })
    scrape_hot100.to_csv("scrape_hot100.csv", index=False)

def scrape_hot100 (url):
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import numpy as np
    
    titles = []
    artists = []
    
    for i in soup.select("li.o-chart-results-list__item > h3"):
        titles.append(i.get_text().strip())
    
    for i in soup.select("li.o-chart-results-list__item > span:nth-child(2)"):
        artists.append(i.get_text().strip())
        artists = [x for x in artists if x != "NEW"]
        artists = [x for x in titles if x != "RE-ENTRY"]
    
    
    scraped_hot100 = pd.DataFrame({
                        "title":titles,
                        "artist":artists
                      })
    scraped_hot100.to_csv("hot100.csv", index=False)
