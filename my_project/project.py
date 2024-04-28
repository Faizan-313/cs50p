from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import getpass


# deal with the alerts when login to the account
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)

s = Service("...chromedriver address.../chromedriver.exe")
driver = webdriver.Chrome(service = s,options=options)

driver.get("https://www.facebook.com/")

#csv file for post related data
filename = "facebook_post_data.csv"
header = ['Likes', 'Comments','Post Text']

#csv file for frind list
filename_1 = "facebook_frind_list.csv"
header_1 = ['Friends','Profile Link']


def main():
    login()
    html_content = profile()

    No_of_likes_and_comments(html_content)
    post_text(html_content)

    friend_list()
    print('Done!')
    driver.quit()


def login():
    #login to the account by getting the users eamil and password
    email = driver.find_element(By.XPATH,'''//*[@id="email"]''')
    user_email = input("Enter your email: ")
    email.send_keys(user_email)

    password = driver.find_element(By.XPATH,'''//*[@id="pass"]''')
    user_password = getpass.getpass("Enter your password: ")
    password.send_keys(user_password)

    # wait till the login button is fully loaded and then click on it
    login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))).click()
    time.sleep(2)


def profile():
    # go to the profile page after the login
    driver.get("https://m.facebook.com/profile")
    time.sleep(10)

    # get the html content of the profile page
    page_content = driver.page_source
    return BeautifulSoup(page_content,'html.parser')


def No_of_likes_and_comments(soup):
    # make and open a csv file and the data
    with open(filename,'w',newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(header)

        impresions = soup.find_all('div',class_='x6s0dn4 xi81zsa x78zum5 x6prxxf x13a6bvl xvq8zen xdj266r xktsk01 xat24cr x1d52u69 x889kno x4uap5 x1a8lsjc xkhd6sd xdppsyt')
        for imp in impresions:
            comment = imp.find('span',class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xi81zsa')
            try:
                new_comment = comment.text
            except:
                new_comment = "0"

            like = imp.find('span',class_='xt0b8zv x2bj2ny xrbpyxo xl423tq').span.span
            try:
                new_like = like.text
            except:
                new_like = "0"

            writer.writerow([new_like,new_comment])


def post_text(soup):
    # Define the values for the new column
    post_text = []
    text_elements = soup.find_all('div', class_='xu06os2 x1ok221b')
    for t in text_elements:
        txt = t.find('span', class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h')
        new_txt = txt.text if txt else '#'
        post_text.append(new_txt)


    post_text = [text for text in post_text if text != '#']

    # open the file again in reading mode and then add the column for post text in it
    with open(filename, 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Add the new column values to the remaining rows of the data
    for i in range(1, min(len(data), len(post_text) + 1)):
        data[i].append(post_text[i - 1] if i - 1 < len(post_text) else "")


    # Write the updated data back to the CSV file
    with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def friend_list():
    driver.get("https://www.facebook.com/peer.faizan.35762/friends")
    time.sleep(10)

    scroll_pause_time = 3
    scroll_height = 0

    while True:
        # Get current scroll height
        prev_scroll_height = scroll_height
        scroll_height = driver.execute_script("return document.body.scrollHeight")

        # Scroll down the page
        driver.execute_script(f"window.scrollTo(0, {scroll_height});")

        # Wait for a brief moment to allow new listings to load
        time.sleep(scroll_pause_time)

        # If no more new listings are loaded, break the loop
        if scroll_height == prev_scroll_height:
            break

    # get the html content of the friend's list page
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')

    with open(filename_1,'w',newline='', encoding='utf-8-sig')as file:
        writer = csv.writer(file)
        writer.writerow(header_1)

        friend_names = soup.find_all('div',class_="x1iyjqo2 x1pi30zi")
        for friend in friend_names:
            frnd = friend.find('span',class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u').text
            # frnd_link = friend.find('div',class_='xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs').a
            frnd_link = friend.find('a')['href'] if friend.find('a') else '*'

            writer.writerow([frnd,frnd_link])


if __name__ == "__main__":
    main()

