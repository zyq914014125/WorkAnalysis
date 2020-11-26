from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from Sprider import pageinputId, workinputId, pageButton

browser = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')

class selenium_:
#查找对应工作,形参:URL,job
    def __init__(self,url):
        self.url=url
    def browser_input(self,job):
        browser.get(self.url)
        browser.find_element_by_id(workinputId).send_keys(job)
        sleep(5)
        #用户点击
        # browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/button").click()
        #用户敲击Enter
        browser.find_element_by_id(workinputId).send_keys(Keys.ENTER)
        sleep(5)
        #返回网页
        self.url=browser.current_url
        return browser.page_source
    #翻页（因为原url，又臭又长https://search.51job.com/list/090200,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
    def browser_nextPage(self,page):
        browser.get(self.url)
        # 清空原有页数
        browser.find_element_by_id(pageinputId).clear()
        browser.find_element_by_id(pageinputId).send_keys(page)
        sleep(3)
        #点击翻页
        browser.find_element_by_xpath(pageButton).click()
        sleep(3)
        # 返回网页
        return browser.page_source
    def browser_exit(self):
        browser.__exit__()
    # browser_nextPage(browser_input("https://www.51job.com/","java"),3)