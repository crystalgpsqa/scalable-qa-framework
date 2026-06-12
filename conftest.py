# pytest가 자동으로 인식하는 특수 파일
import pytest
import pytest_html
import base64
import shutil
from selenium import webdriver
from datetime import datetime
from pathlib import Path
from config.settings import USERNAME, PASSWORD
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def clean_artifacts():

    screenshot_dir = Path("artifacts/screenshots")

    if screenshot_dir.exists():
        shutil.rmtree(screenshot_dir)

    screenshot_dir.mkdir(parents=True, exist_ok=True)


@pytest.fixture
def valid_user():
    return {
        "username": USERNAME,
        "password": PASSWORD
    }


@pytest.fixture
def driver(request):
    chrome_options = Options()

    HEADLESS = True #디버깅시 False로 변경

    if HEADLESS:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")

    chrome_options.add_argument("--disable-gpu") #GPU 렌더링 끄기, 일부 환경에서 안정성 향상
    chrome_options.add_argument("--no-sandbox") #Chrome sandbox 제한 완화, GitHub Actions/Linux에서 Chrome 실행 실패 방지
    chrome_options.add_argument("--disable-dev-shm-usage") #shared memory 사용 방식 변경, Docker/Linux CI 환경에서 메모리 문제로 인한 Chrome 실행 실패 방지

    driver = webdriver.Chrome(options=chrome_options)

    request.node.driver = driver
    yield driver
    driver.quit()

def clear_alert(driver):
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("LEFTOVER ALERT CLEARED")
    except:
        pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)

        if driver:
            screenshot_dir = Path("artifacts/screenshots")
            screenshot_dir.mkdir(parents=True, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = screenshot_dir / f"{item.name}_{timestamp}.png"

            driver.save_screenshot(str(screenshot_path))
            print(f"\nSCREENSHOT SAVED: {screenshot_path}")

            with open(screenshot_path, "rb") as f:
                screenshot_data = f.read()

            encoded_image = base64.b64encode(screenshot_data).decode("utf-8")

            extras.append(
                pytest_html.extras.image(
                    encoded_image,
                    mime_type="image/png",
                    extension="png"
                )
            )
            #extras.append(pytest_html.extras.image(base64.b64encode(screenshot_data).decode()))

            report.extras = extras

            
            
