from selenium import webdriver

browser = webdriver.Chrome("C:\\selenium drivers\\chromedriver_win32\\chromedriver.exe")

browser.get('http://automationpractice.com/index.php')

browser.find_element_by_link_text('Sign in').click()

browser.find_element_by_xpath('//*[@id="email_create"]').send_keys("boney@test.com")
browser.find_element_by_id('SubmitCreate').click()

browser.close()

"""""
def func(x):
    return x + 5

def test_method():
    assert func(3) == 8
"""""
