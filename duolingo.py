
#IMPORT SECTION
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver import ActionChains
#IMPORT SECTION

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
#VARIABLE SECTION
mailovi = []
inviteidvar = []
#VARIABLE SECTION

#def
age = random.randrange(18,52)
passint = random.randrange(10000000)
passstr = "pass" + str(passint) + "word"
#DEf
# problem u kodu je sto mail ne mogu definisati u varijabli globalno niti lokalno
# treba provaliti nacin kako bih to mogao uraditi, predpostavljam liste ili objekti,
#nesto tog tipa, inace mejlove uzima bez problema, samo globalno definisati svaki mejl pojedinacno

def getmails():

    tempmailurl = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=10"

    esp = requests.get(url=tempmailurl)

    print(esp)

    data = esp.json()

    mailnum = -1

    for mail in data:

        mailnum = mailnum + 1
        mailovi.append(str(data[int(mailnum)]))
        #NameError: name 'self' is not defined = "mail" + mailnum
    #    mailvar[mailnum] = str(data[int(mailnum)])
        #global mailvar[mailnum]
        print("Mail ", str(mailnum) + " " +  str(data[int(mailnum)]))

        if mailnum == 9:
            pass;
            print("I got 10 emails.")
            print(mailovi[4])
            for mailss in mailovi:
                print(mailss)
            seleniumf()
            #print(mailovi[5])



def seleniumf():
    try:
        browser = webdriver.Chrome(options=chrome_options)#service=PATH)
    #    browser.get("https://invite.duolingo.com/" + inviteidvar[0])
        #browser.get("https://sh.wikipedia.org/wiki/Robot")
#BDHTZTB5CWWKT2LG43RXMDEG5A
        #time.sleep(5)
        mailcount = -1
        for mail in mailovi:

            browser.get("https://invite.duolingo.com/" + inviteidvar[0])
            mailcount = int(mailcount) + 1

            try:
                ##CHOOSE GERMAN LANGUAGE
                elementgerman = WebDriverWait(browser, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//a[@data-test='language-de']"))
                )
                #elementgerman = browser.find_element_by_xpath("//a[@data-test='language-de']")
                elementgerman.click()

                time.sleep(5)
                #CHOOSE SCHOOL
                elementschool = WebDriverWait(browser, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//label[@data-test='school']"))
                )
                #elementschool = browser.find_element_by_xpath("//label[@data-test='school']")
                elementschool.click()

                time.sleep(1)

                continuebt = WebDriverWait(browser, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@data-test='set-goal']"))
                )
                continuebt.click()

                time.sleep(2)

                continuebt2 = WebDriverWait(browser, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@data-test='set-goal']"))
                )
                continuebt2.click()

                createprofbut = WebDriverWait(browser, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@data-test='create-profile']"))
                )

                createprofbut.click()

                time.sleep(2)

                fakenameurl = "https://api.namefake.com/"

                fakenameresp = requests.get(url=fakenameurl)

                fakenamedata = fakenameresp.json()
                fakenamestr = fakenamedata["name"]

                nameinputf = WebDriverWait(browser, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@data-test='full-name-input']"))
                )
                ageinputf = WebDriverWait(browser, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@data-test='age-input']"))
                )
                emailinputf = WebDriverWait(browser, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@data-test='email-input']"))
                )
                passinputf = WebDriverWait(browser, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@data-test='password-input']"))
                )

                print(fakenamestr)
                nameinputf.send_keys(fakenamestr)
                ageinputf.send_keys(age)
                emailinputf.send_keys(mailovi[mailcount])
                passinputf.send_keys(passstr)

                time.sleep(2)

                registerbutton = WebDriverWait(browser, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@data-test='register-button']"))
                )
                registerbutton.click()
                browser.refresh()

                time.sleep(2)

                browser.back()
                profiledw = WebDriverWait(browser, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@data-test='profile-dropdown']"))
                )

                time.sleep(2)

                hover = ActionChains(browser).move_to_element(profiledw)
                hover.perform()

                time.sleep(2)

                logout = WebDriverWait(browser, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//a[@data-test='logout-button']"))
                )
                logout.click()

                time.sleep(2)

                browser.get("https://invite.duolingo.com/" + inviteidvar[0])
            except:
                browser.quit()
        while(True):
            pass
    except:
        print("Error, try again.")




def main():

    inviteid = input("What is your InviteID? (example: `THISISCODE1010`): ")
    inviteidvar.append(str(inviteid))
    getmails()


main()
