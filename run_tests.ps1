# 반복 실행용 테스트 스크립트

# 1회 실행
# pytest -s --html=reports/report.html --self-contained-html


# 반복 실행 + timestamp report 저장
# 필요할 때 주석 해제해서 사용

# 1..10 | ForEach-Object {

#     $time = Get-Date -Format "yyyyMMdd_HHmmss"

#     pytest -s `
#     --html=reports/report_$time.html `
#     --self-contained-html
# }