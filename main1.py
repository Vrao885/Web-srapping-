from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

import json

option = Options()
option.headless = False

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(5)
baseUrl = "https://youtube.com/"
keyword = "Programming"

def getChannelUrl():
    driver.get(f"{baseUrl}/search?q={keyword}")
    time.sleep(3)
    allChannelList= driver.find_elements_by_css_selector("#text.style-scope.ytd-channel-name a.yt-simple-endpoint.style-scope.yt-formatted-string")
    links = list(dict.fromkeys(map(lambda a: a.get_attribute("href"),allChannelList)))
    return links

def getChannelDetails(urls):
    details = []
    for url in urls:
        driver.get(f"{url}/about")
        cname = driver.find_element_by_css_selector("#text.style-scope.ytd-channel-name").text 
        cDess = driver.find_element_by_css_selector("#description-container.ytd-channel-about-metadata-renderer").text
        cSubs = driver.find_element_by_css_selector("#subscriber-count.meta-item.ytd-c4-tabbed-header-renderer").text
        clink = url
        otherLinkObj = driver.find_elements_by_css_selector("#link-list-container.style-scope.ytd-channel-about-metadata-renderer a.yt-simple-endpoint.style-scope.ytd-channel-about-metadata-renderer")
        otherLinks = list(dict.fromkeys(map(lambda a: a.get_attribute("href"),otherLinkObj)))
        
        obj = {
            "Channelname" : cname,
            "chanalurl"  : clink,
            "channelDescription" : cDess,
            "channelsubscribers" : cSubs,
            "otherLinks" : otherLinks
        }
        details.append(obj)
    return details
if __name__ == "__main__":
    allChannelUrls = getChannelUrl()
    allChannelDetails = getChannelDetails(allChannelUrls)
    print(json.dumps(allChannelDetails, indent=5))