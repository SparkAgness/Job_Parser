from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium .webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pickle
import os
import time
from abc import ABC, abstractmethod


class Main_Parser():
    __chrome_options = None
    __service = None
    __driver = None   
    __wait = None
    
    __url = None
    __browser_pages = None
    __vacancy = None
    __vacancy_field = None
    __search_button = None
    __cookies_path = None
    __additional_buttons = None
    __vacancies_list = None
    __vacancies_links = None #find_elements after searching
    __vacancy_xpath = None

    def __init__(self):
        self.__chrome_options = webdriver.ChromeOptions()
        self.__chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.__chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
        self.__service = Service(ChromeDriverManager().install())
        self.__driver = webdriver.Chrome(service=self.__service, options=self.__chrome_options)
        self.__wait = WebDriverWait(self.__driver, 10, poll_frequency=1)
        self.__cookies_path = f"{os.getcwd()}/cookies.pkl"
        
    @abstractmethod
    def __viewing(self): pass
    
    @abstractmethod
    def __enter_keyword(self): pass

    @abstractmethod
    def Vacancy_Searching(self): pass

    def __load_cookies(self):
        cookies = pickle.load(open(self.__cookies_path, "rb"))
        for cookie in cookies:
            self.__driver.add_cookie(cookie)

    def __del__(self):
        self.__driver.close()


