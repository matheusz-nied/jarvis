from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Caminho para o ChromeDriver
service = Service("/usr/local/bin/chromedriver-linux64/chromedriver")

# Caminho para o Chrome instalado
options = Options()
options.binary_location = "/usr/bin/google-chrome"

# Use o seu perfil do Chrome
options.add_argument("--user-data-dir=/home/kaizen/chrome-selenium-profile")
options.add_argument("--profile-directory=Default")  # ou "Profile 1", "Profile 2", etc
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Outras flags recomendadas
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.youtube.com")
time.sleep(30)
driver.quit()
