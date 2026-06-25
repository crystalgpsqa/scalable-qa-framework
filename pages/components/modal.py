import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Modal():
    def __init__(self, driver):
        self.driver = driver


    MODAL_CLOSE_SELECTORS = [
        "button.closePopupBtn",
        ".modal-wrapper button.closePopupBtn",

        "#usSiteGuideDialog button",
        "#usSiteGuideDialog .close",
        "#usSiteGuideDialog [aria-label='close']",

        "#systemPopup button",
        "#systemPopup .close",
        "#systemPopup [aria-label='close']",
        "#systemPopup button.closePopupBtn",
    ]

    MODAL_BLOCKERS = [
        ".ab-page-blocker",
    ]
    
    def click_outside_modal(self):
        try:
            ActionChains(self.driver).move_to_element_with_offset(
                self.driver.find_element(By.TAG_NAME, "body"),
                10,
                10
            ).click().perform()

            time.sleep(0.5)
            print("MODAL CLOSE ATTEMPTED BY SAFE OUTSIDE CLICK")

        except Exception as e:
            print("MODAL SAFE OUTSIDE CLICK ERROR:", e)


    def close_if_present(self):
        for _ in range(3):
            for selector in self.MODAL_CLOSE_SELECTORS:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)

                    for el in elements:
                        if el.is_displayed():
                            self.driver.execute_script("arguments[0].click();", el)
                            time.sleep(0.5)
                            print(f"MODAL CLOSED BY BUTTON: {selector}")
                            self.wait_until_blocker_disappears()
                            return

                except Exception as e:
                    print(f"MODAL BUTTON ERROR [{selector}]: {e}")

            #self.click_outside_modal()
            time.sleep(1)

        print("MODAL NOT FOUND AFTER RETRY")

    def wait_until_blocker_disappears(self):
        for blocker in self.MODAL_BLOCKERS:
            try:
                WebDriverWait(self.driver, 3).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, blocker))
                )
                print(f"MODAL BLOCKER DISAPPEARED: {blocker}")
            except Exception:
                pass

    #새로운 모달 대비 추후 보강 필요