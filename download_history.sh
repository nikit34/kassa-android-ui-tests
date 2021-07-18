curl -v --location --output artifacts.zip --request GET --header 'PRIVATE-TOKEN: '$PRIVATE_TOKEN'' "https://gitlab.rambler.ru/api/v4/projects/6933/jobs/artifacts/master/download?job=pages"
unzip artifacts.zip || true
cp -r ./public/history/ ./allure-results/history || true
