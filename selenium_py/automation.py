from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')
chrome_browser.maximize_window()
assert 'Selenium Easy Demo' in chrome_browser.title
# assert 'Selenium Easy Demo' in chrome_browser.body
show_msg_button = chrome_browser.find_element_by_class_name("btn-default")
print(show_msg_button.get_attribute("innerHTML"))

# assert 'Show Message' in chrome_browser.page_source()
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I am extra cool')
show_msg_button.click()
output_msg = chrome_browser.find_element_by_id("display")
assert "I am extra cool" in output_msg.text
chrome_browser.close()
