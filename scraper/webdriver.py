from selenium import webdriver

def get_webdriver(driver_path = './webdriver/chromedriver'):
    driver = webdriver.Chrome(executable_path=driver_path)
    return driver

if __name__ == "__main__":
    d = get_webdriver()
    d.get('https://google.com')

# def get_webdriver():
#     return driver