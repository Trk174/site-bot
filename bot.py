from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# ÎNLOCUIEȘTE CU URL-UL TĂU
url = "http://cyber4.rf.gd/premium.php"

try:
    driver.get(url)
    time.sleep(10) # Așteptăm să se încarce protecția JS
    print(f"Accesat {url} la ora {time.strftime('%H:%M:%S')}")
    print("Titlu pagina:", driver.title)
finally:
    driver.quit()
