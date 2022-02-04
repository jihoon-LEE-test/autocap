from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess


subprocess.Popen(r'***** --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
###### '*****' 부분에 chrome.exe 설치된 디렉토리 입력 ######
# ex. C:\Program Files (x86)\Google\Chrome\Application\chrome.exe

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)



# subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
# #지정한 user-agent로 설정합니다.
# user_agent = "Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36"
# option.add_argument('user-agent=' + user_agent)
# #
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
option.add_argument('--window-size= x, y') #실행되는 브라우저 크기를 지정할 수 있습니다.
option.add_argument('--start-maximized') #브라우저가 최대화된 상태로 실행됩니다.
# option.add_argument('--start-fullscreen') #브라우저가 풀스크린 모드(F11)로 실행됩니다.
option.add_argument('--mute-audio') #브라우저에 음소거 옵션을 적용합니다.
# option.add_argument('incognito') #시크릿 모드의 브라우저가 실행됩니다.
# option.add_argument('headless')
option.add_extension('fdpohaocaechififmbbbbbknoalclacl.zip')
# chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]


driver = webdriver.Chrome('chromedriver.exe', options=option)

# try:
#     driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
#     driver.get("chrome-extension://fdpohaocaechififmbbbbbknoalclacl/popup.html")
# except:
#     print(1)
#     chromedriver_autoinstaller.install(True)
#     driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

driver.implicitly_wait(10)
# 페이지 가져오기(이동)
driver.get('https://google.co.kr')

# 5초후 종료
time.sleep(5)
driver.quit() # 웹 브라우저 종료. driver.close()는 탭 종료