from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os

def bot():
    # This is Scotty + Isabel's POC list
    IDS = ['heffernan_tobias@bah.com', 'shearer_jennifer@bah.com', '"Tammy Paight"', 'munoz_frank@bah.com', 'noppenberger_derek@bah.com', '"Kim Lynch"', 'carmelite_betsy@bah.com', '"Lara Chiaurro"', '"Christopher Enriquez"', '"Carrie Ross"', '"Cliff Weber"', '"Catherine Breeze"', '"Steven Moore"', 'dave_docherty@bah.com', 'yao_felix@bah.com', 'gotherman_jeff@bah.com', '"Patrick Ward"', 'williams_anthony2@bah.com', 'newcomb_robert@bah.com', '"Elizabeth Nathaniel"', '"Eric Raffett"', '"Dan Breithenbach"', '"Elizabeth Warner"', 'riolo_joseph@bah.com', 'pastore_dennis@bah.com', '"Cameron Mayer"', '"Chris Bogdan"', '"Travis Bird"'] # need a list of criteria to start searching through
    # This is Tatsu + Jac's List
    # IDS = ['tiffany_frye@bah.com',
    # 'david_donovan@bah.com',
    # 'ron_berry@bah.com',
    # 'dave_geerdes@bah.com',
    # 'geoff_haney@bah.com',
    # 'eric_oitzman@bah.com',
    # 'holly_stowell@bah.com',
    # 'charles_wilson@bah.com']
    # This is my list
    for op in IDS:
        directory = op.replace('"', '')
        parent_dir = 'C:/Users/Matt Turi/Desktop/'


        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        path = path.replace('/', '\\')
        print(path)


        # DRIVER WITH SET DOWNLOAD LOCATION
        options = Options()
        # options.add_argument('--incognito')
        options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        driver_path = "C:/Users/Matt Turi/Downloads/chromedriver_win32/chromedriver.exe"
        prefs = {"plugins.always_open_pdf_externally": True, 'download.default_directory': str(path)}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        actions = ActionChains(driver)

        driver.maximize_window()

        main_window = driver.current_window_handle

        new_op = op + " filetype:pdf"
        driver.get("https://www.google.com/")

        search = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        search.send_keys(new_op + Keys.ENTER)

        time.sleep(1)

        results = driver.find_elements_by_xpath('//*[@id="rso"]/div/div/div/a/div')
        links = driver.find_elements_by_xpath('//*[@id="rso"]/div/div/div/a')
        link_count = 0
        for r in results:
            print(r.text)
            if "jar2" in str(r.text):
                links.pop(0)
                continue
            else:
                actions.key_down(Keys.CONTROL).click(links[link_count]).perform()
                links.pop(0)
                time.sleep(2)
        driver.close()




bot()