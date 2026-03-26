import time
from selenium.webdriver.common.by import By

class Modal():
    def __init__(self, driver):
        self.driver = driver


    MODAL_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        ".modal-wrapper button.closePopupBtn"
    )

    def close_if_present(self):
        try:
            elements = self.driver.find_elements(By.CSS_SELECTOR, "button.closePopupBtn")

            for el in elements:
                if el.is_displayed():
                    self.driver.execute_script("arguments[0].click();", el)
                    time.sleep(0.5)
                    return

        except:
            pass


    def close_modal_if_present(self):
        for _ in range(3):
            try:
                elements = self.driver.find_elements(*self.MODAL_CLOSE_BUTTON)

                for el in elements:
                    if el.is_displayed():
                        time.sleep(0.5)
                        self.driver.execute_script("arguments[0].click();", el)

                        WebDriverWait(self.driver, 3).until(
                            EC.invisibility_of_element(el)
                        )

                        print("MODAL CLOSED")
                        return

            except Exception as e:
                print("MODAL ERROR:", e)

            time.sleep(1)

    print("MODAL NOT FOUND AFTER RETRY")