curl -v --location --output history.zip --request GET --header "PRIVATE-TOKEN: $PRIVATE-TOKEN" "https://gitlab.rambler.ru/api/v4/projects/6933/jobs/artifacts/master/download?job=pages"
unzip history.zip || true
cp -r ./public/history/ ./allure-results/history || true