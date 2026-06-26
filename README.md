# Python UI Test Automation Framework for the Internet
The goal of the repository and the project in general is to strengthen Python programming skills and gain practical experience out of tutorial-based learning but also with realistic web applications(app) with standard web elements that are commonly used across most web apps and across different business domains.

The application under test (AUT) is: https://the-internet.herokuapp.com/.

Additionally this project provides an opportynity to:
- Apply practical experience with Selenium WebDriver, GitHub Actions and Allure reporting that was gained in previous [Java](https://github.com/Olexandr29/eCommerce) and [JavaScript](https://github.com/Olexandr29/eCommerce_JS) projects.
- Broadedn automation quality assurance (AQA) experience out of the eCommerce domain.
- Expand my AQA tech stack and broaden the range of projects I am qualified to work on.
## Tech Stack
- Python
- Selenium WebDriver
- Pytest
- GitHub Actions
- Allure report
## Project Structure
```text
automation-the-internet-python/
├── .github/
│   └── workflows/
│       └── first_flow.yml
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── secure_page.py
├── test_data/
│   └── login_data.py
├── tests/
│   ├── base_test.py
│   └── test_login.py
├── .gitignore
└── README.md
```
## Run Tests

<details><summary> <b>1) Locally</b> </summary>

- with information just about testing session and without print messages: 
```
pytest
```
- with info about testing session and print messages: 
```py
pytest -s
```
- run a specific test from test suit:
```
pytest -k "specific test name"
```
- run test with Allure:
```
pytest --alluredir=allure-results
```
generate and open Allure report:
```
allure generate allure-results -o allure-report --clean
allure open allure-report
```
</details>

<details><summary> <b> 2) Remotely </b> </summary>

Tests run via GitHub Actions. [The workflow](https://github.com/Olexandr29/automation-the-internet-python/actions/workflows/first_flow.yml) is triggered automatically on every push and also can be triggered manually.

Additionally, Allure reporting is implemented.
After each GitHub Actions workflow run, an Allure artifact is generated and available for download.
The report can be further generated locally via the following command:
```
allure serve .
```

</details>