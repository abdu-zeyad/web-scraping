import requests
from bs4 import BeautifulSoup

domain = 'https://en.wikipedia.org/wiki/History_of_Mexico'
response = requests.get(domain)


def get_citations_needed_count(domain):
    get_soup = BeautifulSoup(response.text, 'html.parser')
    result = get_soup.find_all('sup', class_='Inline-Template')
    return (len(result))


def get_citations_needed_report(domain):

    get_soup = BeautifulSoup(response.text, 'html.parser')
    result = get_soup.find_all('sup', class_='Inline-Template')
    paragraph_contain_citation = []

    for p in result:
        paragraph_contain_citation.append(p.parent.text.strip())
    return '\n'.join(paragraph_contain_citation)


count = get_citations_needed_count(domain)
report = get_citations_needed_report(domain)
print(count)
print(report)
