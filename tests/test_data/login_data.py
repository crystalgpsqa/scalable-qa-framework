from config.settings import USERNAME, PASSWORD

LOGIN_VALIDATION_FAIL_DATA = [
    {"username": USERNAME, "password": "rlagpal12", "reason": "invalid_credentials"},
    #{"username": "wrongidtest11@naver.com", "password": PASSWORD, "reason": "invalid_credentials"},
    {"username": "", "password": "", "reason": "empty_email"},
    {"username": USERNAME, "password": "", "reason": "empty_password"},
    {"username": "11", "password": "", "reason": "invalid_email"}
]

# TODO:
# 인증실패형(wrong password / nonexistent account)은
# alert 동작이 flaky 하므로 validation 실패형 안정화 후 별도 분리 예정