from resources.lib.soupObj import soupObject
import xbmc
import xbmcgui
from resources.lib.impfunctions import build_url, addon_handle
from resources.lib.urlResolver import resolve_url
import xbmcplugin
import re
import concurrent.futures
import os


urlmain = "https://www.yodesitv.info/"
channelList = ["Star Plus", "Sony TV", "Star Bharat", "Zee TV"]

tvshow_cache = {}


def get_channel():
    xbmc.log(f"Fetching channels from URL: {urlmain}", xbmc.LOGDEBUG)
    soup = soupObject(urlmain, '.secondary-navigation')
    channels = soup.find_all('li', attrs={'class': 'menu-item-type-post_type'})
    for channel in channels:
        if channel.text.strip() in channelList:
            li = xbmcgui.ListItem(channel.text.strip())
            url = build_url({'mode': 'get_shows', 'url': channel.find('a').get('href')})
            xbmc.log(f"Adding channel to directory: {channel.text.strip()} with URL: {url}", xbmc.LOGDEBUG)
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
    li = xbmcgui.ListItem("Airing Today")
    url = build_url({'mode': 'airing_shows', 'url': channel.find('a').get('href')})
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)


def get_shows(showurl):
    xbmc.log(f"Fetching shows from URL: {showurl}", xbmc.LOGDEBUG)
    shows = soupObject(showurl, '#tab-0-title-1')
    showLists = shows.find_all('div', attrs={'class': re.compile('^one_')})
    local_img = 'special://home/addons/plugin.video.hometheater/resources/Images/'
    # local_img_abs_path = xbmc.translatePath(local_img)
    for showList in showLists:
        li = xbmcgui.ListItem(showList.text)
        icon = showList.select_one('div>a>img')['src']
        fanart = icon.replace('-370x208','') if "-370x208" in icon else icon

        fileExist = os.path.dirname(__file__)
        fileimgbd = ("-".join(showList.text.lower().split(" ")) + "_" + "backdrop.webp").replace("---", "").replace(":", "").strip()
        fileimgposter = ("-".join(showList.text.lower().split(" ")) + "_" + "poster.webp").replace("---", "").replace(":", "").strip()
        poster = os.path.join(os.path.dirname(fileExist), "Images", fileimgposter)
        backdrop = os.path.join(os.path.dirname(fileExist), "Images", fileimgbd)

        # if "no-thumbnail" not in icon:
        li.setArt({
            'thumb' : poster if os.path.exists(poster) else icon,
            'icon' : poster if os.path.exists(poster) else icon,
            'fanart' : backdrop if os.path.exists(backdrop) else fanart
        })
        showurl = build_url({'mode': 'get_Episodes', 'url': showList.find('a').get('href')})
        xbmc.log(f"Adding show to directory: {showList.text} with URL: {showurl}", xbmc.LOGDEBUG)
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=showurl, listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)


# def get_shows(showurl):
#     xbmc.log(f"Fetching shows from URL: {showurl}", xbmc.LOGDEBUG)
#     shows = soupObject(showurl, re.compile('^one_'))
#     showLists = shows.find_all('div', attrs={'class': re.compile('^one_')})
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         something = [executor.submit(get_show_title, showList) for showList in showLists]
        
            
#     for future in concurrent.futures.as_completed(futures):
#         li, url = future.result()
#         xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)
#     xbmcplugin.endOfDirectory(addon_handle)

# def get_show_title(showList):
#     showTitle = showList.select_one('p a').text


def get_Episodes(episodeUrl):
    xbmc.log(f"Fetching episodes from URL: {episodeUrl}", xbmc.LOGDEBUG)
    episodeSoup = soupObject(episodeUrl, '#content_box')
    episodes = episodeSoup.select('h2.front-view-title')
    for episode in episodes:
        li = xbmcgui.ListItem(episode.text)
        li.setProperty('IsPlayable', 'true')
        vidurl = build_url({'mode': 'play_video', 'url': episode.find('a').get('href')})
        xbmc.log(f"Adding episode to directory: {episode.text} with URL: {vidurl}", xbmc.LOGDEBUG)
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=vidurl, listitem=li, isFolder=False)
        xbmcplugin.setContent(addon_handle, 'videos')
    xbmcplugin.endOfDirectory(addon_handle)

def play_video(video_url):
    if video_url in tvshow_cache:
        stream_Link = tvshow_cache[video_url]
    else:
        stream_Link = get_VideoLink(video_url)
        # stream_Link = test_link.get('url')
        tvshow_cache[video_url] = stream_Link
    li = xbmcgui.ListItem(offscreen = True)
    # li.setProperty('IsPlayable', 'true')
    li.setPath(stream_Link)
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=li)

def get_VideoLink(vidurl):
    videoLinkSoup = soupObject(vidurl, '.thecontent')
    def workingLink(search_text):
        # links = videoLinkSoup.find(get_tag).parent.find_next_sibling('p').select_one('a')['href']
        links = videoLinkSoup.find(lambda tag: get_tag(tag, search_text)).parent.find_next_sibling('p').select_one('a')['href']
        linkSoup = soupObject(links, '#content')
        iframe = linkSoup.select_one('iframe').get('src')
        stream_Url = resolve_url(iframe, subs=True)
        stream_Url = stream_Url.get('url')
        xbmc.log(f"Stream url is: {stream_Url}", xbmc.LOGDEBUG)
        return stream_Url
    if x := workingLink('TVlogy'):
        return x
    elif x := workingLink('Netflix'):
        return x
    # links = videoLinkSoup.find(lambda tag: get_tag(tag, 'Netflix')).parent.find_next_sibling('p').select_one('a')['href']
    # linkSoup = soupObject(links, '#content')
    # iframe = linkSoup.select_one('iframe').get('src')
    # stream_Url = resolve_url(iframe, subs=True)
    # xbmc.log(f"Stream url is: {stream_Url}", xbmc.LOGDEBUG)
    # if stream_Url:
    #     return stream_Url
    

def get_tag(tag, search_text):
    # return tag.name == 'span' and 'Netflix' in tag.text
    return tag.name == 'span' and search_text in tag.text