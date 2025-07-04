import main_parser as MP

class JobLab_Parser(MP.Main_Parser):
    __secret_phone_xpath = None
    __enable_phone_xpath = None
    __secret_email_xpath = None
    __enable_email_xpath = None
    
    def __init__(self):
        super().__init__()
        self.__url = "https://www.joblab.ru"
        self.__vacancy_field = ("xpath", "//input[@name='srprofecy']")
        self.__search_button = ("xpath", "//input[@type='submit']")
        self.__vacancy = "developer"                                  #input vacancy here
        self.__vacancy_xpath = ("xpath", "//p[@class='prof']")        
        self.__secret_phone_xpath = ("xpath", "//a[text()='Показать телефон']")
        self.__secret_email_xpath = ("xpath", "//a[contains(text(), 'э')]")
        self.__enable_phone_xpath = ("xpath", "//a[contains(text(), '8')]")
        self.__driver = self._Main_Parser__driver
        self.__driver.get(self.__url)
        self._Main_Parser__load_cookies()
        self.__driver.refresh()
      

    def __enter_keyword(self):
        self._Main_Parser__wait.until(MP.EC.element_to_be_clickable(self.__vacancy_field)).send_keys(self.__vacancy)
        self.__driver.find_element(*(self.__search_button)).click()
        self.__browser_pages = self.__driver.window_handles

    def __viewing(self):
        self.__vacancies_links = self.__driver.find_elements(*(self.__vacancy_xpath))
        for tmp in self.__vacancies_links:
            tmp.click()
            self._Main_Parser__browser_pages = self.__driver.window_handles
            self.__driver.switch_to.window(self._Main_Parser__browser_pages[1])
            self._Main_Parser__wait.until(MP.EC.element_to_be_clickable(self.__secret_phone_xpath)).click()
            self.__driver.find_element(*(self.__secret_email_xpath)).click()
            MP.time.sleep(3)

    def Vacancy_Searching(self):
        self.__enter_keyword()
        self.__viewing()
        