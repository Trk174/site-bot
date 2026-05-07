from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# Token secret — trebuie să fie identic cu KEEPALIVE_TOKEN din index.php
KEEPALIVE_TOKEN = "cy8r4_k33p_2024_x7z"

# Accesăm homepage-ul cu token-ul secret, anti-botul ne lasă să trecem direct
url = f"http://cyber4.rf.gd/?keepalive={KEEPALIVE_TOKEN}"

try:
    driver.get(url)
    time.sleep(5)  # mai scurt, nu mai trebuie să așteptăm JS challenge
    print(f"Accesat {url} la ora {time.strftime('%H:%M:%S')}")
    print("Titlu pagina:", driver.title)
finally:
    driver.quit()
