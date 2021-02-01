# -*- coding: UTF-8 -*-
from time import sleep
from selenium import webdriver
from random import randint
from selenium.webdriver import ActionChains


class SyntheticWatermelon(object):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", {'deviceName': 'iPhone 6'})
        self.driver = webdriver.Chrome(executable_path=r"D:\Chrome\chromedriver.exe", options=options)
        self.driver.set_window_rect(50, 50, 100, 800)
        self.driver.get("https://dushusir.com/xigua")
        self.driver.implicitly_wait(5)

    def run(self):
        while True:
            x_pos = randint(20, 150)
            y_pos = randint(200, 300)
            ActionChains(self.driver).move_by_offset(x_pos, y_pos).click().perform()
            ActionChains(self.driver).move_by_offset(-x_pos, -y_pos).perform()
            sleep(1)


game = SyntheticWatermelon()
game.run()
