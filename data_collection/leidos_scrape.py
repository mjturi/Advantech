from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Function definition for entire bot process
def bot():
    names = []
    abouts = []
    expers = []
    locs = []
    titles = []
    # set paths for webdriver + initialize
    options = Options()
    options.add_argument('--incognito')
    options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
    driver_path = "C:/Users/Matt Turi/Downloads/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    
    driver.maximize_window()
    
    driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    time.sleep(1)
    
    # # find + click signin
    # driver.find_element_by_xpath('/html/body/nav/div/a[2]').click()
    # time.sleep(1)
    
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
    site = 'https://www.google.com/search?sxsrf=ALeKk00dGJFvOsL0RkLfj1hJl5o2MHBhaQ%3A1604693531019&ei=G66lX8ZKzf36BNDrj6AF&q=site%3Awww.linkedin.com+intitle%3Alinkedin+%22dynetics%22+AND+%28usaf+OR+air%29+-intitle%3Aanswers+-intitle%3Aupdated+-intitle%3Ablog+-intitle%3Adirectory+-inurl%3Ajobs+-inurl%3Amegite.com&oq=site%3Awww.linkedin.com+intitle%3Alinkedin+%22dynetics%22+AND+%28usaf+OR+air%29+-intitle%3Aanswers+-intitle%3Aupdated+-intitle%3Ablog+-intitle%3Adirectory+-inurl%3Ajobs+-inurl%3Amegite.com&gs_lcp=CgZwc3ktYWIQDFDbG1iFMWDlWGgAcAB4AIABAIgBAJIBAJgBDaABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwiGxI6f3e7sAhXNvp4KHdD1A1QQ4dUDCA0'
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
    
            try:
                location = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[2]/li[1]').text
            except:
                location = ""
    
            try:
                head = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/header/h2')
            except Exception:
                # driver.execute_script("window.scrollTo(0, 400)")
                try:
                    head = driver.find_element_by_xpath(
                        '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[6]/span/div/section/div[1]/section/header/h2')
                except Exception:
                    ua = UserAgent()
                    userAgent = ua.random
                    print(userAgent)
                    driver.close()
                    driver.switch_to.window(main_window)
                    link_counter += 1
                    time.sleep(1)
                    break
    
            try:
                driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[3]/section/p/span[3]/span/a').click()
            except Exception:
                print('about expanded')
            try:
                about = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[3]/section/p/span[1]')
                about = str(about.text)
            except Exception:
                about = "EMPTY"
    
            actions = ActionChains(driver)
            actions.move_to_element(head).perform()
    
            try:
                title = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3')
                title = title.text
            except Exception:
                try:
                    title = driver.find_element_by_xpath(
                        '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[6]/span/div/section/div[1]/section/ul/li[1]/section/ul/li[1]/div/div/div/div/div/div/h3/span[2]')
                    title = title.text
                except Exception:
                    print('Now what...')
    
            try:
                driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/div/p/span/button').click()
            except Exception:
                print('No see more button')
            try:
                experience = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/div/p')
                experience = experience.text
            except Exception:
                print('No experience for this chum')
                experience = ""
    
            # try:
            #     experience = driver.find_element_by_xpath(
            #         '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/div/p')
            #     experience = str(experience.text)
            # except Exception:
            #     try:
            #         experience = driver.find_element_by_xpath(
            #             '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3')
            #         experience = str(experience.text)
            #     except Exception:
            #         try:
            #             experience = driver.find_element_by_xpath(
            #                 '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/ul')
            #             experience = str(experience.text)
            #         except Exception:
            #             try:
            #                 driver.find_element_by_xpath(
            #                     '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[6]/span/div/section/div[1]/section/ul/li[1]/section/div/div/div/p')
            #                 experience = str(experience.text)
            #             except Exception:
            #                 experience = "EMPTY"
    
            con_name = str(con_name.text)
    
    
            print(con_name)
            print(location)
            print(title)
            print(about)
            print(experience)
    
            expers.append(experience)
            abouts.append(about)
            names.append(con_name)
            locs.append(location)
            titles.append(title)
    
            ua = UserAgent()
            userAgent = ua.random
            print(userAgent)
            driver.close()
            driver.switch_to.window(main_window)
            link_counter += 1
            time.sleep(1)
    
        # block to continue to next page on google search, <num pages to go through. Default cap is 25, change here if less is desired
        if page_tracker < 25:  # page_stop: # 30:
            time.sleep(.75 * 60)
            driver.find_element_by_xpath(
                '/html/body/div[8]/div[2]/div[10]/div[1]/div[2]/div/div[5]/div[2]/span[1]/div/table/tbody/tr/td[12]/a/span[2]').click()
            page_tracker += 1
            time.sleep(1)
            main_window = driver.current_window_handle
        else:
            driver.quit()
            break
    
    names_ser = pd.Series(names)
    exp_ser = pd.Series(expers)
    about_ser = pd.Series(abouts)
    locs_ser = pd.Series(locs)
    titles_ser = pd.Series(titles)
    
    frame = {'Name': names_ser, 'Description/Bio': about_ser, 'Location': locs_ser, 'Title': titles_ser, 'Expertise (subj matter)': exp_ser}
    final = pd.DataFrame(frame)
    final.to_csv('DYNETICS_LI_AIR.csv')
    
    time.sleep(10)
    
    names = []
    abouts = []
    expers = []
    locs = []
    titles = []
    # set paths for webdriver + initialize
    options = Options()
    options.add_argument('--incognito')
    options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
    driver_path = "C:/Users/Matt Turi/Downloads/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    
    driver.maximize_window()
    
    driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    time.sleep(1)
    
    # # find + click signin
    # driver.find_element_by_xpath('/html/body/nav/div/a[2]').click()
    # time.sleep(1)
    
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
    site = 'https://www.google.com/search?sxsrf=ALeKk002NZELzf9Vqz1GpH6gRzDN59W_SA%3A1604693597409&ei=Xa6lX8HJGMrk-gSinZEQ&q=site%3Awww.linkedin.com+intitle%3Alinkedin+%22dynetics%22+AND+%28navy+OR+navsea+OR+navwar+OR+spawar%29+-intitle%3Aanswers+-intitle%3Aupdated+-intitle%3Ablog+-intitle%3Adirectory+-inurl%3Ajobs+-inurl%3Amegite.com&oq=site%3Awww.linkedin.com+intitle%3Alinkedin+%22dynetics%22+AND+%28navy+OR+navsea+OR+navwar+OR+spawar%29+-intitle%3Aanswers+-intitle%3Aupdated+-intitle%3Ablog+-intitle%3Adirectory+-inurl%3Ajobs+-inurl%3Amegite.com&gs_lcp=CgZwc3ktYWIQA1DzIViaM2CbOWgAcAB4AIABAIgBAJIBAJgBBqABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwiB7OK-3e7sAhVKsp4KHaJOBAIQ4dUDCA0&uact=5'
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
    
            try:
                location = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[2]/li[1]').text
            except:
                location = ""
    
            try:
                head = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/header/h2')
            except Exception:
                # driver.execute_script("window.scrollTo(0, 400)")
                try:
                    head = driver.find_element_by_xpath(
                        '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[6]/span/div/section/div[1]/section/header/h2')
                except Exception:
                    ua = UserAgent()
                    userAgent = ua.random
                    print(userAgent)
                    driver.close()
                    driver.switch_to.window(main_window)
                    link_counter += 1
                    time.sleep(1)
                    break
    
            try:
                driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[3]/section/p/span[3]/span/a').click()
            except Exception:
                print('about expanded')
            try:
                about = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[3]/section/p/span[1]')
                about = str(about.text)
            except Exception:
                about = "EMPTY"
    
            actions = ActionChains(driver)
            actions.move_to_element(head).perform()
    
            try:
                title = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3')
                title = title.text
            except Exception:
                try:
                    title = driver.find_element_by_xpath(
                        '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[6]/span/div/section/div[1]/section/ul/li[1]/section/ul/li[1]/div/div/div/div/div/div/h3/span[2]')
                    title = title.text
                except Exception:
                    print('Now what...')
    
            try:
                driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/div/p/span/button').click()
            except Exception:
                print('No see more button')
            try:
                experience = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/div/p')
                experience = experience.text
            except Exception:
                print('No experience for this chum')
                experience = ""
    
            # try:
            #     experience = driver.find_element_by_xpath(
            #         '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/div/p')
            #     experience = str(experience.text)
            # except Exception:
            #     try:
            #         experience = driver.find_element_by_xpath(
            #             '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3')
            #         experience = str(experience.text)
            #     except Exception:
            #         try:
            #             experience = driver.find_element_by_xpath(
            #                 '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/ul')
            #             experience = str(experience.text)
            #         except Exception:
            #             try:
            #                 driver.find_element_by_xpath(
            #                     '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[6]/span/div/section/div[1]/section/ul/li[1]/section/div/div/div/p')
            #                 experience = str(experience.text)
            #             except Exception:
            #                 experience = "EMPTY"
    
            con_name = str(con_name.text)
    
            print(experience)
            print(about)
            print(con_name)
    
            expers.append(experience)
            abouts.append(about)
            names.append(con_name)
            locs.append(location)
            titles.append(title)
    
            ua = UserAgent()
            userAgent = ua.random
            print(userAgent)
            driver.close()
            driver.switch_to.window(main_window)
            link_counter += 1
            time.sleep(1)
    
        # block to continue to next page on google search, <num pages to go through. Default cap is 25, change here if less is desired
        if page_tracker < 25:  # page_stop: # 30:
            time.sleep(.75 * 60)
            driver.find_element_by_xpath(
                '/html/body/div[8]/div[2]/div[10]/div[1]/div[2]/div/div[5]/div[2]/span[1]/div/table/tbody/tr/td[12]/a/span[2]').click()
            page_tracker += 1
            time.sleep(1)
            main_window = driver.current_window_handle
        else:
            driver.quit()
            break
    
    names_ser = pd.Series(names)
    exp_ser = pd.Series(expers)
    about_ser = pd.Series(abouts)
    locs_ser = pd.Series(locs)
    titles_ser = pd.Series(titles)
    
    frame = {'Name': names_ser, 'Description/Bio': about_ser, 'Location': locs_ser, 'Title': titles_ser, 'Expertise (subj matter)': exp_ser}
    final = pd.DataFrame(frame)
    final.to_csv('DYNETICS_LI_NAVY.csv')
    
    time.sleep(10)

    names = []
    abouts = []
    expers = []
    locs = []
    titles = []
    # set paths for webdriver + initialize
    options = Options()
    options.add_argument('--incognito')
    options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
    driver_path = "C:/Users/Matt Turi/Downloads/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(options=options, executable_path=driver_path)

    driver.maximize_window()

    driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    time.sleep(1)

    # # find + click signin
    # driver.find_element_by_xpath('/html/body/nav/div/a[2]').click()
    # time.sleep(1)

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
    site = 'https://www.google.com/search?sxsrf=ALeKk03JCaJE-d8duObwMDIiidaTB637eg%3A1604693543222&ei=J66lX8qEDY3k-gS8xKvYAg&q=site%3Awww.linkedin.com+intitle%3Alinkedin+%22dynetics%22+AND+%28Army+OR+usasoc+OR+forscom+OR+arcyber+OR+inscom+OR+netcom+OR+ATEC+or+centcom+OR+cascom%29+-intitle%3Aanswers+-intitle%3Aupdated+-intitle%3Ablog+-intitle%3Adirectory+-inurl%3Ajobs+-inurl%3Amegite.com&oq=site%3Awww.linkedin.com+intitle%3Alinkedin+%22dynetics%22+AND+%28Army+OR+usasoc+OR+forscom+OR+arcyber+OR+inscom+OR+netcom+OR+ATEC+or+centcom+OR+cascom%29+-intitle%3Aanswers+-intitle%3Aupdated+-intitle%3Ablog+-intitle%3Adirectory+-inurl%3Ajobs+-inurl%3Amegite.com&gs_lcp=CgZwc3ktYWIQDFCyow1YsqMNYLzEDWgAcAB4AIABAIgBAJIBAJgBA6ABAqABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwiKtPek3e7sAhUNsp4KHTziCisQ4dUDCA0'
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

            try:
                location = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[2]/li[1]').text
            except:
                location = ""

            try:
                head = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/header/h2')
            except Exception:
                # driver.execute_script("window.scrollTo(0, 400)")
                try:
                    head = driver.find_element_by_xpath(
                        '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[6]/span/div/section/div[1]/section/header/h2')
                except Exception:
                    ua = UserAgent()
                    userAgent = ua.random
                    print(userAgent)
                    driver.close()
                    driver.switch_to.window(main_window)
                    link_counter += 1
                    time.sleep(1)
                    break

            try:
                driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[3]/section/p/span[3]/span/a').click()
            except Exception:
                print('about expanded')
            try:
                about = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[3]/section/p/span[1]')
                about = str(about.text)
            except Exception:
                about = "EMPTY"

            actions = ActionChains(driver)
            actions.move_to_element(head).perform()

            try:
                title = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3')
                title = title.text
            except Exception:
                try:
                    title = driver.find_element_by_xpath(
                        '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[6]/span/div/section/div[1]/section/ul/li[1]/section/ul/li[1]/div/div/div/div/div/div/h3/span[2]')
                    title = title.text
                except Exception:
                    print('Now what...')

            try:
                driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/div/p/span/button').click()
            except Exception:
                print('No see more button')
            try:
                experience = driver.find_element_by_xpath(
                    '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/div/p')
                experience = experience.text
            except Exception:
                print('No experience for this chum')
                experience = ""

            # try:
            #     experience = driver.find_element_by_xpath(
            #         '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/div/p')
            #     experience = str(experience.text)
            # except Exception:
            #     try:
            #         experience = driver.find_element_by_xpath(
            #             '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3')
            #         experience = str(experience.text)
            #     except Exception:
            #         try:
            #             experience = driver.find_element_by_xpath(
            #                 '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/ul')
            #             experience = str(experience.text)
            #         except Exception:
            #             try:
            #                 driver.find_element_by_xpath(
            #                     '/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[6]/span/div/section/div[1]/section/ul/li[1]/section/div/div/div/p')
            #                 experience = str(experience.text)
            #             except Exception:
            #                 experience = "EMPTY"

            con_name = str(con_name.text)

            print(experience)
            print(about)
            print(con_name)

            expers.append(experience)
            abouts.append(about)
            names.append(con_name)
            locs.append(location)
            titles.append(title)

            ua = UserAgent()
            userAgent = ua.random
            print(userAgent)
            driver.close()
            driver.switch_to.window(main_window)
            link_counter += 1
            time.sleep(1)

        # block to continue to next page on google search, <num pages to go through. Default cap is 25, change here if less is desired
        if page_tracker < 3:  # page_stop: # 30:
            time.sleep(.75 * 60)
            driver.find_element_by_xpath(
                '/html/body/div[8]/div[2]/div[10]/div[1]/div[2]/div/div[5]/div[2]/span[1]/div/table/tbody/tr/td[5]/a/span[2]').click()
            page_tracker += 1
            time.sleep(1)
            main_window = driver.current_window_handle
        else:
            driver.quit()
            break

    names_ser = pd.Series(names)
    exp_ser = pd.Series(expers)
    about_ser = pd.Series(abouts)
    locs_ser = pd.Series(locs)
    titles_ser = pd.Series(titles)

    frame = {'Name': names_ser, 'Description/Bio': about_ser, 'Location': locs_ser, 'Title': titles_ser,
             'Expertise (subj matter)': exp_ser}
    final = pd.DataFrame(frame)
    final.to_csv('DYNETICS_LI_ARMY.csv')

bot()
