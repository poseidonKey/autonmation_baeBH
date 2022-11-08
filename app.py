from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import urllib.request

driver = webdriver.Chrome('chromedriver')
# search = '고양이'
search = '쥐'
fileName = 'mouse_image'
number = 30
interval = 0.2

driver.get(
    f'https://www.google.com/search?q={search}&tbm=isch&tbs=il:ol&hl=ko&sa=X&ved=0CAAQ1vwEahcKEwiA7q_9p537AhUAAAAAHQAAAAAQBg&biw=1583&bih=827')
time.sleep(1)

firstIamge = driver.find_element(
    by=By.CSS_SELECTOR, value='#islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img')
firstIamge.click()
for i in range(number):
    try:
        time.sleep(interval)
        image = driver.find_element(
            by=By.CSS_SELECTOR, value='#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id.b0vFpe > div > a > img')
        imageSource = image.get_attribute('src')
        urllib.request.urlretrieve(imageSource, f'{fileName}_{i+1}.jpg')

    except:
        print(f'{i+1}번째 오류 발생')
    else:
        print(f'{i+1}번째 save')
    finally:
        nextBtn = driver.find_element(
            by=By.CSS_SELECTOR, value='#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.mWagE.fDqwl > a:nth-child(4) > div')
        nextBtn.click()


# time.sleep(10)
driver.quit()
