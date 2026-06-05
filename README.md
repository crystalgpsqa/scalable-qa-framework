# Scalable QA Framework

pytest + Selenium 기반의 UI 자동화 테스트 프레임워크입니다.

단순 테스트 자동화가 아닌,
유지보수성, 재사용성, flaky 대응, CI/CD, Evidence 수집을 고려한 구조를 목표로 구현했습니다.

대상 사이트:
- Olive Young Global Mall

주요 목표:
- Page Object Model(POM) 적용
- Flow Layer 분리
- Reusable Component 설계
- Screenshot / HTML Report 기반 Evidence 수집
- GitHub Actions 기반 CI 자동화



## Tech Stack

- Python
- pytest
- Selenium
- webdriver_manager
- pytest-html
- GitHub Actions
- dotenv



## Project Structure

scalable-qa-framework/
├─ config/
├─ flows/
├─ pages/
│  ├─ components/
├─ tests/
│  ├─ test_data/
├─ utils/
├─ artifacts/
├─ reports/
├─ .github/workflows/
└─ conftest.py



## 설계 의도

단순히 테스트를 통과시키는 것이 아니라,
유지보수성과 재사용성을 고려한 자동화 프레임워크를 목표로 설계했습니다.

### POM 적용

Locator와 테스트 로직을 분리하여
UI 변경 시 수정 범위를 최소화하고자 했습니다.

### Flow Layer 적용

페이지 조작 로직과 검증(assert)을 분리하여
테스트 시나리오를 보다 명확하게 표현하고
유지보수를 쉽게 만들고자 했습니다.

### Reusable Component 적용

Header, Modal, Alert 등 여러 페이지에서 공통으로 사용하는 요소를 컴포넌트화하여 중복 코드를 줄이고 재사용성을 높였습니다.



### Evidence Collection

테스트 실패 시 원인 분석을 쉽게 하기 위해
자동 Screenshot 저장 및 HTML Report 생성 기능을 구현했습니다.

GitHub Actions 환경에서는 Report와 Screenshot을 Artifact로 업로드하여
실행 결과를 다운로드하고 확인할 수 있도록 구성했습니다.


### Modal Overlay Issue

초기 테스트 실행 시 랜딩 페이지에서 노출되는 팝업으로 인해 클릭이 차단되는 문제가 발생했습니다.

원인 분석 결과 Modal Overlay가 사용자 입력을 가로채고 있었으며,
ElementClickInterceptedException이 발생했습니다.

이를 해결하기 위해 Modal Component를 분리하고,
BasePage의 공통 click() 동작 전에 Modal 처리 로직을 추가하여 안정성을 개선했습니다.


### Alert Flaky Issue

로그인 실패 시 Selenium Alert이 발생하는 경우와
발생하지 않는 경우가 혼재되어 있었습니다.

특히 Validation Fail과 Authentication Fail의 동작 방식이 달라
동일 테스트에서도 결과가 달라지는 flaky 현상이 발생했습니다.

이를 해결하기 위해 Alert Component를 분리하고,
Alert 메시지 자체보다는 로그인 실패 결과를 우선 검증하는 방향으로 테스트를 개선했습니다.


### CI Environment Variables

로컬 환경에서는 .env 파일을 사용하여 테스트 계정을 관리했지만,
GitHub Actions 환경에서는 .env 파일이 존재하지 않아 로그인 테스트가 실패했습니다.

원인 분석 결과 USERNAME, PASSWORD 값이 None으로 주입되고 있음을 확인했습니다.

이를 해결하기 위해 GitHub Secrets를 적용하여
CI 환경에서도 안전하게 계정 정보를 사용할 수 있도록 개선했습니다.


### Evidence Collection

테스트 실패 시 원인 분석을 쉽게 하기 위해
자동 Screenshot 저장 및 HTML Report 생성 기능을 구현했습니다.

GitHub Actions 환경에서는 Report와 Screenshot을 Artifact로 업로드하여
실행 결과를 다운로드하고 확인할 수 있도록 구성했습니다.



## 실행 방법

### 1. 저장소 클론

git clone https://github.com/crystalgpsqa/scalable-qa-framework.git

cd scalable-qa-framework

### 2. 가상환경 생성 및 활성화

python -m venv venv

Windows:
venv\Scripts\activate

### 3. 패키지 설치

pip install -r requirements.txt

### 4. 환경변수 설정

프로젝트 루트에 .env 파일 생성

QA_USERNAME=your_email@example.com
QA_PASSWORD=your_password

### 5. Smoke Test 실행

pytest -m smoke -s

### 6. 전체 테스트 실행

pytest -s

### 7. HTML Report 생성

pytest -s --html=reports/report.html --self-contained-html



## CI/CD

GitHub Actions를 활용하여 Smoke Test를 자동 실행하도록 구성했습니다.

### Workflow

git push

↓

GitHub Actions 실행

↓

Headless Chrome 환경에서 pytest 실행

↓

HTML Report 생성

↓

Screenshot Artifact 수집

↓

Artifact 업로드

### 적용 내용

- GitHub Actions 기반 자동 실행
- Ubuntu Linux Runner 사용
- Headless Chrome 실행
- GitHub Secrets 기반 계정 정보 관리
- pytest-html Report 생성
- Screenshot Artifact 업로드

### 사용된 Secrets

GitHub Actions에서는 .env 파일 대신 GitHub Secrets를 사용합니다.

- QA_USERNAME
- QA_PASSWORD



## 향후 개선 계획

현재는 UI 자동화 테스트 프레임워크의 기본 구조를 구축한 상태이며,
다음과 같은 방향으로 확장할 계획입니다.

### 테스트 실행 스크립트 분리

반복 실행 및 운영 편의성을 위해 실행 스크립트를 분리할 예정입니다.

예시:

scripts/
├─ run_smoke.ps1
├─ run_regression.ps1
└─ run_flaky_check.ps1

### 테스트 데이터 관리 고도화

현재는 Python 기반 테스트 데이터를 사용하고 있으며,
향후 JSON / CSV 기반 데이터 관리 구조를 적용할 예정입니다.

### API 테스트 추가

requests + pytest 기반 API 테스트를 추가하여
UI 테스트와 API 테스트를 함께 운영할 수 있는 구조로 확장할 계획입니다.

### 테스트 리포트 고도화

CI 환경에서 생성되는 HTML Report와 Screenshot Artifact를
보다 체계적으로 관리할 수 있도록 개선할 예정입니다.

### Clean Portfolio Repository 구성

학습 과정과 실험 흔적을 포함한 저장소와 별도로,
포트폴리오 제출용 저장소를 구성하여
구조와 문서를 정리할 계획입니다.

### 테스트 시나리오 확장

현재 로그인 중심 자동화 시나리오를 구현한 상태이며,
향후 실제 사용자 핵심 플로우를 대상으로 테스트 범위를 확장할 계획입니다.

예시:

- 상품 검색
- 상품 상세 페이지 진입
- 장바구니 담기
- 장바구니 검증
- Checkout 페이지 진입
- 로그아웃

이를 통해 단순 기능 검증을 넘어
실제 사용자 관점의 End-to-End 시나리오를 자동화할 예정입니다.