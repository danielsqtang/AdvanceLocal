import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Tesla&'
       'from=2019-01-25&'
       'sortBy=popularity&'
       'apiKey=5a8938f0855d47e19332e1f54747120b')
response = requests.get(url)
print(response.json())