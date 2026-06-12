import requests


def test_public_api_status():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status_code == 200

#타겟 사이트 httpbin.org은 HTTP 요청과 응답을 테스트하기 위한 공개 API입니다.