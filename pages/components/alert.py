from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class alert():
    def __init__(self, driver):
        self.driver = driver

    def wait_and_handle_alert(self):
        try:
            alert = WebDriverWait(self.driver, 2, poll_frequency=0.1).until(
                EC.alert_is_present()
            )
            text = alert.text
            alert.accept()
            return text

        except TimeoutException:
            return None