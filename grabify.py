# Python code to send mail
import smtplib
import io
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from random import seed
from random import randint

def grabify(grab_user, grab_pass, grab_link):
    driver = webdriver.Chrome(
        "C:\\Users\\lavon\\Desktop\\Chrome\\chromedriver")
    driver.implicitly_wait(0.6)
    driver.get("https://grabify.link/login")
    time.sleep(getRandomTime())
    driver.find_element_by_xpath(
        "//input[@id='username-or-email']").send_keys(grab_user)
    driver.find_element_by_xpath(
        "//input[@id='password']").send_keys(grab_pass)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    driver.find_element_by_xpath("//a[normalize-space()='Home']").click()
    driver.find_element_by_xpath("//input[@id='linkToShorten']").send_keys(grab_link)
    driver.find_element_by_xpath("//button[@id='create']").click()
    time.sleep(getRandomTime())
    text = driver.find_element_by_id("customLink").text

    time.sleep(getRandomTime())
    driver.close()
    return text
def getRandomTime():
    randTime = randint(3, 5)
    return randTime

def email_setup(USERNAME, PASSWORD, sender_mail, receivers_mail, text):
    try:
        with open(receivers_mail) as file:
            array = []
            for line in file:
                array.append(line)
        # list of reciver email_id to the mail

        # [item for item in input("Enter Receiver Mail Address :- ").split()] this is used to take user input of receiver mail id

        # getting length of list
        length = len(array)

        # Iterating the index
        # same as 'for i in range(len(list))'

        # Here we iterate the loop and send msg one by one to the reciver
        for i in range(length):
            X = array[i]
            reciver_mail = X

            print(reciver_mail)

            message = MIMEMultipart()
            message['From'] = USERNAME
            message['To'] = reciver_mail  # Pass Reciver Mail Address
            message['Subject'] = 'Important Matter'  # The subject line

            mail_content = '''Hello,
            This is an important matter to come to your attention {}'''.format(text)

            # The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))
            # Create SMTP session for sending the mail
            # open the file to be sent

            # Open PDF file in binary mode
            # The file is in the directory same as where you run your Python script code

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(USERNAME, PASSWORD)
            text = message.as_string()
            s.sendmail(USERNAME, reciver_mail, text)
            s.quit()

            print('Mail Sent')

    except Exception:
        print("Mail delivery failed.")

def email_sender():
    sender_mail = input("What is your gmail?\n")
    USERNAME = sender_mail
    PASSWORD = input("What is your Password?\n")
    receivers_mail = input("What is the email list path?\n")
    grab_user = input("What is your grabify username?\n")
    grab_pass = input("What is your grabify password?\n")
    grab_link = input("Paste in your link to be converted: ")
    text = grabify(grab_user, grab_pass, grab_link)
    email_setup(USERNAME, PASSWORD, sender_mail, receivers_mail, text)


email_sender()