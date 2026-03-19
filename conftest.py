# pytest가 자동으로 인식하는 특수 파일
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
# fixture 정의 위치

# driver 생성 위치

# 전역 hook 정의 위치