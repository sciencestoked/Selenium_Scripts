import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import webbrowser
from selenium import webdriver
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from tqdm import notebook
import time


def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def send_message(url):
    driver.get(url)
    time.sleep(10)
    element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]', 40)
    msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    msg_box.send_keys('\n')
    time.sleep(10)

def prepare_msg(dataframe, name_col, phone_col):
    file = dataframe[[name_col, phone_col]]
    base_msg = """
Hello Ma’am/Sir,
Only *2 days* are left for registering in the grand technical event 💫 *Skillathon 2.0* 💫 being organized by BFX prISM, IIT (ISM) Dhanbad ✨. 
We hope, you have updated the students regarding the deadline for the registration process which is on 📍 *10th June, 2022* 📍. 
Our team would appreciate maximum participation from your side.
Thanking you✨, 
Team BFX prISM.
"""
    base_url = 'https://web.whatsapp.com/send?phone={}&text={}'
    for i,j in notebook.tqdm(file.iterrows()):
        phone_no = j[phone_col]
        if len(str(phone_no))==10:
            phone_no = int("91"+str(phone_no))
        Name = j[name_col].title()
        msg = urllib.parse.quote(base_msg)#.format(Name))
        url_msg = base_url.format(phone_no, msg)
        try:
            send_message(url_msg)
            #print(f'{phone_no} : {Name}')
        except:
            print(f"Error in : {Name}'s case. " )





dummy2 = pd.read_excel("Datasheet.xlsx")





chrome_options = Options()
chrome_options.add_argument("--user-data-dir-Session")
chrome_options.add_argument("--profile-directory=Default")

PATH = "chromedriver_v103/chromedriver"
s=Service(PATH)
driver = webdriver.Chrome(service=s, options=chrome_options)
prepare_msg(dummy2, 'Name', 'Phone')
