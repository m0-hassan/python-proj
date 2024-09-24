from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from tqdm import tqdm

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://quranicaudio.com/")

imam_name = "Abdullah Ali Jabir"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.LINK_TEXT, imam_name))
)

imam_element = driver.find_element(By.LINK_TEXT, imam_name)
imam_element.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, 
                                    "//a[span[contains(text(),'Download')]]"))
)

download = driver.find_element(By.XPATH,
                                "//a[span[contains(text(), 'Download')]]")
url = download.get_attribute('href')

# Get the URL & Surah Number Extracted
url_split = url.split('/')
base = '/'.join(url_split[:-1]) + '/'

for surah in range(1, 115):
    mp3 = base + str(surah).zfill(3) + ".mp3"

    with requests.get(mp3, stream=True) as response:
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))

        with open(f"{surah}.mp3", "wb")as file:
            with tqdm(total=total_size, unit='B', unit_scale=True, 
                    desc=f"Downloading Surah {surah}") as progress_bar:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                        progress_bar.update(len(chunk))

    print(f"Surah {surah} downloaded!")
