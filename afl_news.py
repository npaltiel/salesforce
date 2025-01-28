from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='d2d5786ec49f430d8308f18a76a40b14')

# /v2/everything
all_articles = newsapi.get_everything(q='afl', from_param='2024-10-26',
                                      to='2024-11-25', language='en', domains='abc.net.au')


# Function to extract source, title, and date
def parse_articles(data):
    if 'articles' in data:
        parsed_data = [
            {
                "source": article['source']['name'],
                "title": article['title'],
                "publishedAt": article['publishedAt']
            }
            for article in data['articles']
        ]
        return parsed_data
    return []


# Parse the articles
parsed_articles = parse_articles(all_articles)
