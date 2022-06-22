import os, time, os.path, pyperclip, pyautogui, ctypes
from colorama import Fore
from selenium import webdriver

def autologin():
    os.system('cls')
    print("""Enter token""")
    print()
    entertoken = str=(input(f"""Token >"""))
    print("\n\n")
    if len(entertoken) >= 59:
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.maximize_window()
        driver.get('https://discord.com/login')
        js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}' # c'etait le plus chiant
        time.sleep(3)
        driver.execute_script(js + f'login("{entertoken}")')
        time.sleep(10)
        if driver.current_url == 'https://discord.com/login':
            os.system('cls')
            print(f"""{Fore.LIGHTRED_EX}[!] Connection interompu""")
            driver.close()
        else:
            os.system('cls')
            print(f"""{Fore.LIGHTGREEN_EX}[!!] Connection Etabli""")
        input(f"""# appuyez sur entrer pour quitter""")
    else:
        print(f"""{Fore.LIGHTRED_EX}[!] Probleme avec le token, verifier le""")
        time.sleep(2)
        os.system('cls')
autologin()
#fin
