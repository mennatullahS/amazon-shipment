from selenium import webdriver
import time
from collections import OrderedDict
import datetime
import os
browser = webdriver.Firefox()
def loginFunc(str):
    url = 'https://www.amazon.com/gp/css/order-history?ie=UTF8&ref_=nav_nav_orders_first&'
    browser.get(url)    
    with open('pass.txt', 'r') as fPass:
        txtpass = fPass.readline()
    with open('user.txt', 'r') as fUser:
        txtuser = fUser.readline()
    browser.find_element_by_xpath('//input[@type="email"]').send_keys(txtuser)
    try:
       browser.find_element_by_xpath('//input[@type="password"]').send_keys(txtpass)
    except:
       browser.find_element_by_xpath('//input[@id = "continue"]').click();
       browser.find_element_by_xpath('//input[@type="password"]').send_keys(txtpass)
    browser.find_element_by_xpath('//input[@id="signInSubmit"]').click()
loginFunc("Hi")
all_orders = browser.find_elements_by_xpath('//span[@class = "a-button a-button-normal a-button-primary"]//span[@class = "a-button-inner"]//a')
for order in all_orders: 
    Orderurl = order.get_attribute("href")
    browser.get(Orderurl)
    MerchantName = browser.find_elements_by_xpath('//span[@class = "a-button a-button-normal a-button-primary"]').text
    ShipmentTrackingNumber = browser.find_elements_by_xpath('//span[@class = "a-button a-button-normal a-button-primary"]').text
    InvoiceNumber = browser.find_elements_by_xpath('//span[@class = "a-button a-button-normal a-button-primary"]').text
    PDFName = browser.find_elements_by_xpath('//span[@class = "a-button a-button-normal a-button-primary"]').text
    browser.find_element_by_xpath('//input[@id="signInSubmit"]').click()