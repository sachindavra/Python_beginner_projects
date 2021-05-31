from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from getpass import getpass

chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get("https://www.instagram.com/")
sleep(10)

username = input("Enter Username: ")
enter_username = chrome.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
enter_username.send_keys(username)

passwd = getpass(prompt='Passwd: ')
enter_pass = chrome.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
enter_pass.send_keys(passwd)

login_button = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
login_button.click()
sleep(10)


find_user = chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
find_user.send_keys(input("User to find: "))
sleep(3)
find_user.send_keys(Keys.ENTER)
find_user.send_keys(Keys.ENTER)

open_post = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div/div[2]')
open_post.click()
sleep(3)

like = chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
like.click()

first_post_next_button = chrome.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a')
first_post_next_button.click()
sleep(3)

first_comment = chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
first_comment.send_keys("Good Pic!")
first_comment.send_keys(Keys.ENTER)




while True:
    try:
        like_next_post = chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        like_next_post.click()
        open_next_post = chrome.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]')
        open_next_post.click()
        sleep(3)
    except:
        close_button = chrome.find_element_by_xpath('/html/body/div[5]/div[3]/button')
        close_button.click()
        break




