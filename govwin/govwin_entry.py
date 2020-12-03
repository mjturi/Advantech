from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import schedule
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def bot():
    options = Options()
    options.add_argument('--incognito')
    options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.maximize_window()

    # initialize into govwin
    driver.get('https://iq.govwin.com/cas/login?service=https://iq.govwin.com/neo/myGovwin')
    time.sleep(1)

    # login
    email = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/form/div/div/input')
    email.send_keys('USERNAME')

    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/form/div/span/input[1]').click()
    time.sleep(1)

    pswd = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/form/div/div[2]/input')
    pswd.send_keys('PASSWORD')

    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/form/div/span/input[1]').click()
    time.sleep(2)

    try:
        driver.find_element_by_xpath('/html/body/div[12]/div/button').click()
    except Exception:
        print('No welcome message')

    # can be incumbent, NAICS code, primary requirement, etc
    NAICS = ['541330','541519','541611','236220','334511','334516','335999','517311','518210','541210','541219','541511','541512','541513','541612','541614','541620','541690','541710','541712','541715','541820','541990','561110','561210','562111','562910','611430','611710','621111','621511','811219']

    for code in NAICS:
        search = driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[2]/div[2]/form/div/input')
        search.send_keys(code + Keys.ENTER)
        link_count = 2
        main_window = driver.current_window_handle

        while True:
            cur = driver.find_element_by_xpath(
                '/html/body/div[4]/div[3]/div[1]/div/div[5]/div[5]/div/div[' + str(link_count) + ']/h3/a')
            cur.send_keys(Keys.CONTROL + Keys.RETURN)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)

            date = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/table/tbody/tr[2]/td').text
            date = str(date).split('/')[1]
            date = str(date).split(' (')[0]
            date = int(date)

            if date > 2019:
                driver.find_element_by_xpath('/html/body/div[4]/div[4]/div/div[1]/ul/li[7]/a').click()
                time.sleep(2)
                driver.find_element_by_xpath(
                    '/html/body/div[4]/div[4]/div/div[9]/div/div/div[3]/div/div/div[2]/div[1]/div/a[1]').click()
                time.sleep(1)
                tagline = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/form/table/tbody/tr[2]/td/input')
                fname = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/form/table/tbody/tr[3]/td/input')
                lname = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/form/table/tbody/tr[4]/td/input')
                title = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/form/table/tbody/tr[5]/td/input')
                phone = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/form/table/tbody/tr[6]/td/input')
                email = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/form/table/tbody/tr[7]/td/input')
                website = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/form/table/tbody/tr[8]/td/input')
                position = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/form/table/tbody/tr[9]/td/select')
                capabilities = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/form/table/tbody/tr[10]/td/textarea')

                # Keys.BACK_SPACE (0,6,4,17,10,23,19,-,0)
                tagline.send_keys('HUBZone specializing in engineering, technical, and professional services')

                # fname.clear()
                # fname.send_keys('test')
                #
                # lname.clear()
                # lname.send_keys('test')

                title.clear()
                title.send_keys('Talent Acquisition & Development Manager')

                phone.clear()
                # phone.send_keys('')

                # email.clear()
                # email.send_keys('test')

                website.clear()
                website.send_keys('http://advantech-gs.com/')

                position.click()
                driver.find_element_by_xpath(
                    '/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/form/table/tbody/tr[9]/td/select/option[3]').click()

                capabilities.send_keys('HUBZone specializing in engineering, technical, and professional services \nIT/Cybersecurity: Advantech cybersecurity and intelligence experts provide organizations with timely access to high-quality actionable data from disparate sources to accelerate analysis, response and situational awareness. \nProgram/Business Management: Advantech delivers a variety of program and business management services to support customers in meeting their requirements, managing and sustaining their programs within budget, and accomplishing their missions. \nEngineering: Advantech delivers a variety of program and business management services to support customers in meeting their requirements, managing and sustaining their programs within budget, and accomplishing their missions.')

                driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/form/div[1]/input').click()
            else:
                driver.close()
                driver.switch_to(main_window)
                link_count = 2
                break

            driver.close()
            driver.switch_to(main_window)
            link_count += 1


bot()
