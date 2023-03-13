#coding:utf-8
import re
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import urllib

"""
下载煎蛋妹子到本地，通过selenium、正则表达式、phantomjs、Beautifulsoup实现
"""

url2 = 'http://jandan.net/ooxx'
url1 = 'http://w2.aqu1024.rocks/pw/thread.php?'
#解决谷歌浏览器正受到自动测试软件的控制
#options = webdriver.ChromeOptions()
#options.add_argument('disable-infobars')
#driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.PhantomJS('C:\Program Files\phantomjs\bin\phantomjs.exe')

driver = webdriver.PhantomJS()
wait = WebDriverWait(driver, 30)

#下载的煎蛋妹子保存的文件夹
img_save_file = 'images'

#获取总页数。打开煎蛋网-妹子图默认页面可以获取到总页数
def get_default_page_num():
    try:
        driver.get(url)
        page_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.current-comment-page')))
        return page_element.text
    except TimeoutException:
        get_default_page_num()

#获取图片的url
def get_img_url(page_number):
    img_url_list = []
    url = url2 + r'?fid=' + str(page_number)
    print(url)
    html = driver.get(url)
    try:
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#footer')))
    except TimeoutException:
        print("打开页面失败，重新加载该页面")
        get_img_url(page_number)

    #获取页面html元素
    html = driver.page_source
    #通过BeautifulSoup解析
    soup = BeautifulSoup(html, 'html.parser')
    #找出所有为img的标签
    imgs = soup.find_all('img')
    #gif图片需要获取ora_src属性，才是完整的gif图片。has_attr 判断是否有某个属性，attrs可以获取属性值
    for img in imgs:
        if img.has_attr('org_src'):
            img_url = img.attrs['org_src']
        else:
            img_url = img.attrs['src']
        img_url_list.append(img_url)
    return img_url_list

def get_img_url2(page_number):
    img_url_list = []
    url = r'http://jandan.net/ooxx/page-' + str(page_number) + r'#comments'
    print(url)
    # url = 'http://www.baidu.com'
    html = driver.get(url)
    try:
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#comments > ol img')))
    except TimeoutException:
        print("打开页面失败，重新加载该页面")
        get_img_url(page_number)

    #获取页面html元素
    html = driver.page_source
    #通过BeautifulSoup解析
    soup = BeautifulSoup(html, 'html.parser')
    #找出所有为img的标签
    imgs = soup.find_all('img')
    #gif图片需要获取ora_src属性，才是完整的gif图片。has_attr 判断是否有某个属性，attrs可以获取属性值
    for img in imgs:
        if img.has_attr('org_src'):
            img_url = img.attrs['org_src']
        else:
            img_url = img.attrs['src']
        img_url_list.append(img_url)
    return img_url_list
#下载图片，通过urllib的urlretrieve实现
def download_img(img_url):
    try:
        img_name = img_url.split('/')[-1]
        img_save_path = img_save_file + '/' + img_name
        urllib.request.urlretrieve(img_url, img_save_file + '/' + img_name)
    except TimeoutException:
        print("获取图片超时")

#创建图片存储所在的文件夹
def add_img_save_file(img_save_file):
    if os.path.exists(img_save_file):
        pass
    else:
        os.makedirs(img_save_file)

def main():
    add_img_save_file(img_save_file)
    #通过正则表达式提取当前的页数
    partner = re.compile(r'(\d+)')
    #content = get_default_page_num()
    #total_pages = partner.search(content).group()
    total_pages = 81
    #for i in range(69, int(total_pages) + 1):
    for i in range(1, int(total_pages) + 1):
        img_url_list = get_img_url(str(i))
       
        for img_url in img_url_list:
            print("正在下载第" + str(i) + '的图片，url为：',img_url)
            download_img(img_url)

if __name__ == '__main__':
    main()