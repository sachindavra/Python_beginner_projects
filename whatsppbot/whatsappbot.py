from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get("https://web.whatsapp.com")
sleep(10)

emojis = [":-)", ":-P", ":-(", ":-D", "<3"]

search_box = chrome.find_element_by_class_name("_2_1wd")
search_box.send_keys("Test")
search_box.send_keys(Keys.ENTER)

for i in range(0, 5):
    message_box = chrome.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
    message_box.send_keys(f"Testing whatsapp bot. {emojis[i]}")
    message_box.send_keys(Keys.ENTER)
    sleep(2)
