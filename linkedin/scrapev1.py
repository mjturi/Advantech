from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
import schedule
from subprocess import Popen

# Function definition for entire bot process
def bot():
    # set paths for webdriver + initialize
    options = Options()
    options.add_argument('--incognito')
    options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
    driver_path = "C:/Users/Matt Turi/Downloads/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(options=options, executable_path=driver_path)

    driver.maximize_window()

    driver.get('https://www.linkedin.com/')
    time.sleep(1)

    # find + click signin
    driver.find_element_by_xpath('/html/body/nav/div/a[2]').click()
    time.sleep(1)

    # enter login info
    user = driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[1]/input')
    user.send_keys('EMAIL')
    pswd = driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[2]/input')
    pswd.send_keys('PASSWORD')

    # submit form, try catch because it was having issues finding the button by a single absolute path
    try:
        driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[4]').click()
    except Exception:
        try:
            driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[3]/button').click()
        except Exception:
            driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[4]/button').click()
            try:
                driver.find_element_by_link_text('Sign in').click()
            except Exception:
                quit()

    time.sleep(1)
    # try catch for mobile authentication, seems unnecessary as of now
    try:
        driver.find_element_by_xpath('/html/body/div/div[1]/section/div[2]/div/article/footer/div/div/button').click()
    except Exception:
        print('No auth needed')

    page_tracker = 1
    page_stop = 11
    link_stop = 10

    # boolean li query, must first search in google then copy search address
    site = 'https://www.google.com/search?q=site:www.linkedin.com+intitle:linkedin+%22vice+president+-+booz+allen%22+-intitle:answers+-intitle:updated+-intitle:blog+-intitle:directory+-inurl:jobs+-inurl:megite.com&ei=yEt7X_v0N-H99AO3tqoQ&start=230&sa=N&ved=2ahUKEwj7-InJ8Z3sAhXhPn0KHTebCgI43AEQ8NMDegQIDBBB&biw=1920&bih=969'
    driver.get(site)

    # main loop for handling bot
    while True:
        main_window = driver.current_window_handle
        link_counter = 0
        ua = UserAgent()
        userAgent = ua.random
        print(userAgent)

        time.sleep(1)

        data = driver.find_elements_by_partial_link_text('linkedin.com')

        for data[link_counter] in data:
            # if link_counter > link_stop and page_tracker == page_stop:
            #     break
            data = driver.find_elements_by_partial_link_text('linkedin.com')
            data[link_counter].send_keys(Keys.CONTROL + Keys.RETURN)

            driver.switch_to.window(driver.window_handles[1])

            time.sleep(2)

            # LOCATIONS WERE CHANGING DUE TO VPN...as of now it is not necessary to use a vpn unless office traffic is high
            # '/html/body/div[7?]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]'

            # Block to figure out their name: if both attempts fail, go to essentially end of task loop and resume
            # process or move on to next page
            try:
                con_name = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]')
            except Exception:
                try:
                    con_name = driver.find_element_by_xpath(
                        '/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]')
                except Exception:
                    ua = UserAgent()
                    userAgent = ua.random
                    print(userAgent)
                    driver.close()
                    driver.switch_to.window(main_window)
                    link_counter += 1
                    time.sleep(1)
                    continue
                    # if page_tracker < 30:
                    #     time.sleep(2.5 * 60)
                    #     driver.find_element_by_xpath(
                    #         '/html/body/div[8]/div[2]/div[10]/div[1]/div[2]/div/div[5]/div[2]/span[1]/div/table/tbody/tr/td[12]/a/span[2]').click()
                    #     page_tracker += 1
                    #     time.sleep(1)
                    #     main_window = driver.current_window_handle
                    #     continue
                    # else:
                    #     driver.quit()
                    #     break

            # block for splicing connection name, obtaining first name only
            con_name = str(con_name.text)
            if ',' in con_name:
                con_name = con_name.split(', ')
                con_name = con_name[0]
            elif '-' in con_name:
                con_name = con_name.split('-')
                con_name = con_name[0]

            if ' ' in con_name:
                con_name = con_name.split(' ')
                con_name = con_name[0]

            print(con_name)

            if len(con_name) < 16:
                # Try catch for different linkedin headers
                try:
                    driver.find_element_by_xpath(
                        '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button').click()
                except Exception:
                    try:
                        driver.find_element_by_xpath(
                            '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button/span').click()
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/div/div/ul/li[4]/div/div/span[1]').click()
                    except Exception:
                        # If a connect button either is not there or is unclickable, just move on
                        ua = UserAgent()
                        userAgent = ua.random
                        print(userAgent)
                        driver.close()
                        driver.switch_to.window(main_window)
                        link_counter += 1
                        time.sleep(1)
                        # block to continue to next page on google search
                        if page_tracker < 190:
                            driver.find_element_by_xpath(
                                '/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[5]/div[2]/span[1]/div/table/tbody/tr/td[' + str(
                                    page_tracker) + ']/a').click()
                            page_tracker += 1
                            time.sleep(1)
                            main_window = driver.current_window_handle
                            continue
                        else:
                            driver.quit()
                            break

                # block for sending a personalized note with connection
                time.sleep(1)
                try:
                    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]/span').click()
                    tbox = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/textarea')
                    time.sleep(1)
                    tbox.send_keys('Hi ' + con_name + '- We have common contacts and I thought we might also connect. Advantech has teamed with BAH for 13+ years as the prof services HUBZone: www.advantech-gs.com. We\'re nationwide, and happy to support/provide any info to help you stay ahead of market needs.\nJack 858.705.3069')
                    time.sleep(1)

                    # This the send connection line
                    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
                    time.sleep(1)

                except Exception:
                    print('Already Connected')

            ua = UserAgent()
            userAgent = ua.random
            print(userAgent)
            driver.close()
            driver.switch_to.window(main_window)
            link_counter += 1
            time.sleep(1)

        # block to continue to next page on google search, <num pages to go through. Default cap is 25, change here if less is desired
        if page_tracker < 190: #page_stop: # 30:
            time.sleep(2.5 * 60)
            driver.find_element_by_xpath(
                '/html/body/div[8]/div[2]/div[10]/div[1]/div[2]/div/div[5]/div[2]/span[1]/div/table/tbody/tr/td[12]/a/span[2]').click()
            page_tracker += 1
            time.sleep(1)
            main_window = driver.current_window_handle
        else:
            driver.quit()
            break
bot()

# schedule.every().day.at("04:00").do(bot)
# failed = False
# while True:
#     try:
#         schedule.run_pending()
#     except Exception:
#         Popen('taskkill /F /IM chrome.exe', shell=True)
#         print('failed')
#         failed = True
#         time.sleep(10)
#         while failed:
#             try:
#                 schedule.run_all()
#                 failed = False
#             except Exception:
#                 Popen('taskkill /F /IM chrome.exe', shell=True)
#                 print('failed')
#                 time.sleep(10)
#     time.sleep(60)
