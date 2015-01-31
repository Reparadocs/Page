from bing_search_api import BingSearchAPI
import json

my_key = "8jhH8TwVCHdDiWxXYgC5KqyEmChYTKW0kkFngbVYnH8"
query_string = "Sony"
bing = BingSearchAPI(my_key)
params = {'$format': 'json',
          '$top': 10,
          '$skip': 0}
news = bing.search('news', query_string, params).json()
for i in range(10):
   print(news['d']['results'][0]['News'][i])
#news = json.loads(bing.search('news', query_string, params).json())
