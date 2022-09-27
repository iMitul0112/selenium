# from selenium import webdriver

# username = "AppleApple"
# password = "123456"

# url = "http://www.stealmylogin.com/demo.html"

# driver = webdriver.Chrome("/home/appgambit/Downloads/chromedriver")

# driver.get(url)

# driver.find_element_by_name("username").send_keys(username)
# driver.find_element_by_name("password").send_keys(password)
# driver.find_element_by_css_selector("input[type=\"submit\" i]").click()

# print("logged in succesfully")

# from selenium import webdriver

# userName = "1021"
# password = "welcome"

# url = "http://appgambithq.paywheel.net/paywheelnewui/login/login-card"

# driver = webdriver.Chrome("/home/appgambit/Downloads/chromedriver")

# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(20)

# driver.find_element_by_name("userName").send_keys(userName)
# driver.find_element_by_name("passWord").send_keys(password)
# # driver.find_element_by_css_selector(".sign-button[_ngcontent-lis-c16]").click()
# driver.find_element_by_class_name("sign-button").click()

# print("logged in succesfully")

# from selenium import webdriver

# userName = ""
# password = ""

# url = "https://www.instagram.com/"

# driver = webdriver.Chrome("/home/appgambit/Downloads/chromedriver")

# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(20)

# driver.find_element_by_name("username").send_keys(userName)
# driver.find_element_by_name("password").send_keys(password)
# # driver.find_element_by_class_name("             qF0y9          Igw0E     IwRSH      eGOV_       acqo5   _4EzTm    bkEs3                          CovQj                  jKUp7          DhRcB                                                    ").click()
# driver.find_element_by_xpath("//button[contains(@type,'submit')]").click()

# print("logged in succesfully")

from selenium import webdriver

userName = "mitul.shah@***.com"
password = ""

url = "https://slack.com/intl/en-in/"

driver = webdriver.Chrome("/home/appgambit/Downloads/chromedriver")

driver.get(url)
driver.maximize_window()
driver.implicitly_wait(20)

# driver.find_element_by_name("username").send_keys(userName)
# driver.find_element_by_name("password").send_keys(password)
# driver.find_element_by_class_name("             qF0y9          Igw0E     IwRSH      eGOV_       acqo5   _4EzTm    bkEs3                          CovQj                  jKUp7          DhRcB                                                    ").click()
# driver.find_element_by_xpath("//a[@class='c-button ss-c-workspace-detail__action v--primary']//span[@class='p-workspaces_list__link_icon_text'][contains(text(),'Launch Slack')]").click()
# driver.find_element_by_xpath("//a[contains(text(),'use Slack in your browser')]").click()
# driver.find_element_by_xpath("//div[@class='ql-editor ql-blank']//p").click()
driver.find_element_by_class_name("c-nav--signed-out__link").click()
driver.implicitly_wait(20)
# driver.find_element_by_class_name("c-input_text c-input_text--large p-get_started_email_form__input").send_keys(userName)
driver.find_element_by_id("signup_email").send_keys(userName)
driver.find_element_by_id("submit_btn").click()
# driver.find_element_by_class_name("c-link c-button-unstyled margin_right_250 p-get_started__email_app_link").click()
driver.find_element_by_css_selector(".p-get_started__email_app_link").click()
driver.find_element_by_css_selector(".button--medium").click()

print("logged in succesfully")