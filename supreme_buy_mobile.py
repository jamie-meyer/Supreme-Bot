from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import time


class SupremeBuyer:  # SupremeBuyer(Buyer):
    def __init__(self):
        desired_capabilities = DesiredCapabilities().CHROME
        # desired_capabilities["pageLoadStrategy"] = "none"
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
        prefs = {'profile.default_content_setting_values': {
                                                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                            'notifications': 2, 'auto_select_certificate': 2,
                                                            'fullscreen': 2,
                                                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                            'media_stream_mic': 2, 'media_stream_camera': 2,
                                                            'protocol_handlers': 2,
                                                            'ppapi_broker': 2, 'automatic_downloads': 2,
                                                            'midi_sysex': 2,
                                                            'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                            'metro_switch_to_desktop': 2,
                                                            'protected_media_identifier': 2, 'app_banner': 2,
                                                            'site_engagement': 2,
                                                            'durable_storage': 2}}
        options.add_argument('--profile-directory=Profile 2')
        options.add_argument('--user-data-dir=/Users/jamie/Library/Application Support/Google/Chrome/')
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options, desired_capabilities=desired_capabilities)

    def buy_item(self, item_id, keywords,
                 name, email, phone, address, zipcode, city, state, cc_num, exp_month, exp_year, cvv):
        if not self.add_to_cart(item_id, keywords):
            return False
        self.checkout(name, email, phone, address, zipcode, city, state, cc_num, exp_month, exp_year, cvv)
        return True

    def add_to_cart(self, item_id, keywords):
        self.driver.get('https://supremenewyork.com/mobile/#products/{}'.format(item_id))
        #self.driver.execute_script("for(i=0;i<document.styleSheets.length;i++){document.styleSheets.item(i).disabled=true;}all=document.getElementsByTagName('*');for(i=0;i<all.length;i++){el=all[i];el.style.cssText='';el.style.width='';el.style.padding='0px';el.style.margin='2px';el.style.backgroundImage='none';el.style.backgroundColor='#fff';el.style.color='#000';}")
        # Clicking add to cart
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'cart-button')))
        atc = self.driver.find_element_by_class_name('cart-button')
        self.driver.execute_script("arguments[0].click();", atc)

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'checkout-now')))
        checkout = self.driver.find_element_by_id('checkout-now')
        self.driver.execute_script("arguments[0].click();", checkout)

        #self.driver.execute_script("for(i=0;i<document.styleSheets.length;i++){document.styleSheets.item(i).disabled=true;}all=document.getElementsByTagName('*');for(i=0;i<all.length;i++){el=all[i];el.style.cssText='';el.style.width='';el.style.padding='0px';el.style.margin='2px';el.style.backgroundImage='none';el.style.backgroundColor='#fff';el.style.color='#000';}")
        return True

    def checkout(self, name, email, phone, address, zipcode, city, state, cc_num, exp_month, exp_year, cvv):
        #time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'checkout-form')))
        form = self.driver.find_element_by_id('checkout-form')

        part1 = form.find_element_by_id('billing-info')
        self.driver.execute_script('document.getElementById("order_bn").value="{}";'.format(name))
        self.driver.execute_script('document.getElementById("order_email").value="{}";'.format(email))
        self.driver.execute_script('document.getElementById("order_tel").value="{}";'.format(phone))
        self.driver.execute_script('document.getElementById("order_billing_address").value="{}";'.format(address))
        self.driver.execute_script('document.getElementById("order_billing_zip").value="{}";'.format(zipcode))
        self.driver.execute_script('document.getElementById("order_billing_city").value="{}";'.format(city))

        Select(part1.find_element_by_id('order_billing_state')).select_by_visible_text(state)

        part2 = form.find_element_by_id('credit-card')

        self.driver.execute_script('document.getElementById("cnid").value="{}";'.format(cc_num))

        Select(part2.find_element_by_id('credit_card_month')).select_by_visible_text(exp_month)
        Select(part2.find_element_by_id('credit_card_year')).select_by_visible_text(exp_year)

        self.driver.execute_script('document.evaluate(\'//input[@placeholder="cvv"]\', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.value="{}";'.format(cvv))

        checkbox = part2.find_element_by_id('order_terms')
        self.driver.execute_script("arguments[0].click();", checkbox)

        #time.sleep(2)  # DELAY BEFORE BUY
        WebDriverWait(form, 5).until(EC.element_to_be_clickable((By.ID, 'submit_button'))).click()

    def close(self):
        self.driver.quit()

