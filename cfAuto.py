from selenium import webdriver
from getpass import getpass

driver = webdriver.Chrome()
driver.get("http://codeforces.com/enter")

handle = input("Enter your handle : ")
pwd = getpass("Enter your password : ")

handle_box = driver.find_element_by_id("handle")
handle_box.send_keys(handle)

pwd_box = driver.find_element_by_id("password")
pwd_box.send_keys(pwd)

login_btn = driver.find_element_by_class_name("submit")
login_btn.submit()

contest_code = input("Enter contest code : ")
ques = input("Enter question number (A/B/C/D/E/F) : ")

driver.get("http://codeforces.com/problemset/problem/" + contest_code +  "/" + ques)

path = input("Enter path to solution : ")
choose_file = driver.find_element_by_name("sourceFile")
choose_file.send_keys(path)

submit = driver.find_element_by_class_name("submit")
submit.submit()

print ("Congrats ! Successfully submitted")