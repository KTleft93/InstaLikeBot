from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(browser):
        browser.get("https://www.instagram.com/?h1=en")
        time.sleep(5)
        username = browser.find_element_by_css_selector("[name='username']")
        password = browser.find_element_by_css_selector("[name='password']")
        login = browser.find_element_by_css_selector("button")

        username.send_keys("account_name")
        password.send_keys("password")
        login.click()
        time.sleep(5)

def visit_Tag(browser, url):
    browser.get(url)
    time.sleep(5)

    pictures = []
    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")
    some_pictures = pictures[9:12]
    sleep_time = 5
    image_count = 0

    for picture in some_pictures:

        picture.click()
        time.sleep(sleep_time)

        like_button = browser.find_element_by_css_selector("[aria-label='Like']")
        like_button.click()

        close = browser.find_element_by_css_selector("[aria-label='Close']")
        close.click()

        image_count += 1
        time.sleep(sleep_time)

def main():
    browser = webdriver.Chrome()
    login(browser)

    tags = [
        "fitness",
        "blackfitness",
        "workouts",
        "likeback",
        "like4like",
        "fitfam",
        "bootyworkout",
        "homeworkout",
        "likeback",
        "gym"
    ]

    while True:
        for tag in tags:
            visit_Tag(browser, f"https://www.instagram.com/explore/tags/{tag}")
        time.sleep(3600)
main()
