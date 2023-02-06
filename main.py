# 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
from multiprocessing import process

import openai
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import subprocess
from subprocess import Popen, PIPE
import pyautogui
import time
import pyttsx3
from selenium.common.exceptions import StaleElementReferenceException

# Initialize the web driver
driver = webdriver.Chrome()

# Navigate to StackOverflow
driver.get("https://stackoverflow.com")
time.sleep(2)


element_by_class = driver.find_element(By.CSS_SELECTOR, ".flex--item.s-btn.s-btn__primary.js-accept-cookies.js-consent-banner-hide")
element_by_class.click()
time.sleep(1)
language = input("please tell you file language: ")
# flex--item s-btn s-btn__primary js-accept-cookies js-consent-banner-hide
# Locate the element by its class name and click on it
element_by_class = driver.find_element(By.CSS_SELECTOR, ".s-topbar--menu-btn.js-left-sidebar-toggle")
element_by_class.click()
time.sleep(1)
element_by_class = driver.find_element(By.CSS_SELECTOR, "#nav-questions")
element_by_class.click()
time.sleep(1)
element_by_class = driver.find_element(By.CSS_SELECTOR, ".s-btn.s-btn__filled.s-btn__sm.s-btn__icon.ws-nowrap")
element_by_class.click()
time.sleep(1)
element_by_class = driver.find_element(By.CSS_SELECTOR, "input[value='MostVotes']")
element_by_class.click()
time.sleep(1)
text_field = driver.find_element(By.CSS_SELECTOR, ".s-input.js-tageditor-replacing")
text_field.send_keys(language)
pyautogui.press('enter')
time.sleep(1)
element_by_class = driver.find_element(By.CSS_SELECTOR, ".s-btn.s-btn__sm.s-btn__primary.flex--item")
element_by_class.click()

element = driver.find_element(By.CSS_SELECTOR, "a[rel='next']")
click = input("Do you want to change the page? (Enter 1 to click, or any other value to leave as is): ")
if click == "1":
    pages = input("on which page do you want to go: ")
    pages = int(pages)
    for i in range(pages - 1):
        element = driver.find_element(By.CSS_SELECTOR, "a[rel='next']")
        element.click()
        time.sleep(2)

prompt_lists = []
header_elements = driver.find_elements(By.CSS_SELECTOR, ".s-post-summary--content-title")
headers_list = []
for i, header_element in enumerate(header_elements):
    headers_list.append(header_element.text)
    exec(f"header_list{i + 1} = headers_list[i]")
    prompt_lists.append(headers_list[i])

time.sleep(5
           )
driver.quit()
import webbrowser

# data = input("Enter the data to be searched: ")

# construct the search query
# search_query = "https://www.youtube.com/search?q=" + data

# open the web browser with the search query
# webbrowser.open_new_tab(search_query)
# Enter your API key
openai.api_key = "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"

model_engine = "text-davinci-003"
datas = []
s = input("from: ")
s = int(s)
k = input("To: ")
for s in range(int(k)):
    prompt2 = "Please solve this problem for me and give me example with code: " + prompt_lists[s]
    completion1 = openai.Completion.create(
        engine=model_engine,
        prompt=prompt2,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    datas.append("\nYour Question:" + prompt_lists[s] + "\n" + "Your Answer:-" + completion1.choices[0].text)
    print("Your Question:" + prompt_lists[s] + "?" + "\n" + "Your Answer:-" + completion1.choices[0].text)

engine = pyttsx3.init()

file_name = input("Enter the name of the file: ")
if language == "C++":
    file_path = file_name + ".cpp"
if language == "javascript":
    file_path = file_name + ".js"
if language == "python":
    file_path = file_name + ".py"
if language == "html":
    file_path = file_name + ".html"
pyautogui.hotkey('winleft', 'left')
pyautogui.hotkey('Ctrl', 'Alt', 's')
# pyautogui.typewrite('obs studio')
pyautogui.press('enter')

time.sleep(10)
pyautogui.hotkey('ctrl', 'alt', 'h')
time.sleep(5)
# create a .cpp file
with open(file_name, "w") as file:
    file.write("")
# open the file in Visual Studio Code
pro = subprocess.Popen(['code', '-n', file_path], shell="true", stdout=PIPE, stderr=PIPE)
Values = []
diff = len(datas) - len(Values)
for i in range(diff):
    Values.append("nothing")
for i in range(len(datas)):
    Values[i] = datas[i]

time.sleep(5)
with open(file_path, "w") as file:
    pyautogui.hotkey('ctrl', 's')
    for i in range(len(Values)):
            bon = 1
            pyautogui.hotkey('ctrl', 's')
            engine.setProperty('volume', 0.9)  # Increase the volume of the voice
            engine.setProperty('pitch', -0.5)
            engine.setProperty('rate', 130)
            engine.say(Values[i])
            time.sleep(2)
            for char in Values[i]:
                # if bon == 1:
                #     pyautogui.hotkey('alt', 'tab')
                #     pyautogui.click()
                #     time.sleep(2)
                #     pyautogui.hotkey('alt', 'tab')
                #     pyautogui.click()
                #     time.sleep(2)
                #     pyautogui.hotkey('alt', 'tab')
                #     pyautogui.click()
                #     time.sleep(2)
                #     pyautogui.hotkey('alt', 'tab')
                #     pyautogui.click()
                #     time.sleep(2)
                # bon = 2
                file.write(char)
                file.flush()
                time.sleep(0.05)
            engine.runAndWait()

# time.sleep(3)
# for data in datas:
#   time.sleep(2)
#       for char in data:
#        file.write(char)
#       file.flush()
#       time.sleep(0.06)

time.sleep(5)
pyautogui.hotkey('ctrl','shift', 's')
pyautogui.press("enter")
time.sleep(10)
pyautogui.hotkey('ctrl', '`')
time.sleep(5)
pyautogui.write('echo "# All_problem_codes" >> README.md')
pyautogui.press("enter")
time.sleep(2)
pyautogui.write('git init')
pyautogui.press("enter")
time.sleep(2)
pyautogui.write('git add README.md')
pyautogui.press("enter")
time.sleep(2)
pyautogui.write('git commit -m "first commit"')
pyautogui.press("enter")
time.sleep(2)
pyautogui.write('git branch -M main')
pyautogui.press("enter")
time.sleep(2)
pyautogui.write('git remote add origin https://github.com/devkumar2313/All_problem_codes.git')
pyautogui.press("enter")
time.sleep(2)
pyautogui.write('git push -u origin main')
pyautogui.press("enter")
time.sleep(0.1 * len(completion1.choices[0].text))
pro.terminate()


