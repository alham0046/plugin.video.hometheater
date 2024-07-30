from bs4 import BeautifulSoup
import requests
# from resources.lib.soupObj import soupObject

# show_data = {
#     1: [{'title': 'Episode 1'}, {'title': 'Episode 2'}],
#     2: [{'title': 'Episode 1'}, {'title': 'Episode 2'}],
#     3: [{'title': 'Episode 1'}, {'title': 'Episode 2'}]
# }

# print(show_data)
# for season, episode in show_data.items():
#     print(episode[0]["title"])

# a = {}
# a['url'] = {'a' : "google.com"}
# a['url1'] = {'a' : "google1.com"}
# a['url2'] = {'a' : "google2.com"}
# for i,j in a.items():
#     print(i, j['a'])

# a = ['alham', 'faishal', 'vipul']
# for i,j in enumerate(a):
#     print(i, j)

# {
#     '1': [{'Episode 1': 'https:xyz.mkv'}],
#     '3': [{'Episode 2': 'https:xyz2.mkv'}, {'Episode 1': 'https:xyz3.mkv'}],
#     '2': [{'Episode 5': 'https://abc.mkv'}, {'Episode 3': 'https://def.mkv'}]
# }

html = """
<div class="entry-content">
    <h5 style="text-align: center;"><strong><span style="color:#fff;">Season 5 Netflix <span style="color: #FFA500;">[Hindi DD5.1]</span> 720p WEB-DL x264 [400MB/E]</span> </strong></h5>
    <hr>
    <h5 style="text-align: center;"><strong><span style="color:#fff;">Season 3 Netflix <span style="color: #FFA500;">[Hindi DD5.1]</span> 720p WEB-DL x264 [400MB/E]</span> </strong></h5>
    <p style="text-align: center;"><a href="https://example.com/season3/720p" rel="nofollow noopener noreferrer" target="_blank"><button class="dwd-button">Download Now</button></a></p>
    <h5 style="text-align: center;"><strong><span style="color:#fff;">Season 3 Netflix <span style="color: #FFA500;">[Hindi DD5.1]</span> 1080p WEB-DL x264 [1GB/E]</span> </strong></h5>
    <p style="text-align: center;"><a href="https://example.com/season3/1080p" rel="nofollow noopener noreferrer" target="_blank"><button class="dwd-button">Download Now</button></a></p>
</div>
"""
# soup = BeautifulSoup(html, 'html.parser')
# hrtags = soup.hr.find_next_siblings()
# reqtag = next(x for x in hrtags if "1080" in x.text)
# print(reqtag)

# url = "https://gamerxyt.com/hubcloud.php?host=vcloud&id=qus12krjb0vjbj8&token=TWRjekV4bmtCemxDcys5Yk4wNGNqWTZCeXdLMktHb2xQS2lUSFczUGtSMD0="
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
# mp4Url = soup.select_one('a[href*="pixeldra"]')['href']
# print(mp4Url)

a = {'a':"alham", 'v':"vipul", 's':"sumit"}
print(len(a))
