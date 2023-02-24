# from bs4 import BeautifulSoup
#
# with open('xml_file.xml', encoding='UTF-8') as xml_file:
#     src = xml_file.read()
#     soup = BeautifulSoup(src, 'xml')
#
# networkCode = soup.select('networkCode')
# applicationName = soup.select('applicationName')
# query = soup.select('query')
#
# print(networkCode[0].text)
# print(applicationName[0].text)
# print(query[0].text)

import re

request = '''
      <filterStatement>
        <query>WHERE parentId IS NULL LIMIT 500</query>
      </filterStatement>
      '''

t = re.search(r"<query>(.+?)</query>", request).group(1)
print(t)