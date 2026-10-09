# Architecture

<details><summary><b>Overview</b></summary>

This project is part of the [multi-language UI test automation ecosystem](https://github.com/Olexandr29/automation-the-internet-on-python-java-js/tree/main)
built around the same application under test (AUT): [The Internet](https://the-internet.herokuapp.com/).

This repository contains a Python-based UI test automation framework designed to automate web application scenarios using Selenium WebDriver and pytest.

The framework uses Python, venv, and pip for project and dependency management, GitHub Actions for CI/CD automation, and Allure Report for test result reporting.

The project follows the Page Object Model (POM) approach to separate test scenarios from page-specific UI interactions.

</details>


<details><summary><b>Repository Structure</b></summary>

The repository is organized as a Python-based UI test automation framework.

```text
automation-the-internet-python
├───.github
│   └───workflows           # GitHub Actions workflow
├───docs                    # Project documentation
├───pages                   # Page Object Modules
├───tests                   # Automated test classes and scenarios
├───test_data               # Test data
├───utils                   # Reusable utilities and Allure report generation script
├───.gitignore              # Specifies files and directories ignored by Git
├───pytest.ini              # Pytest configuration              
└───README.md               # Project overview and usage instructions
```

**Main Directories and Files**
| Directory / File     | Responsibility                                                                           |
| -------------------- | ---------------------------------------------------------------------------------------- |
| `.github/workflows/` | Contains GitHub Actions workflow definitions for automated test execution and reporting. |
| `docs/`              | Contains project documentation, including architecture documentation.                    |
| `pages/`             | Contains Page Object classes responsible for page-specific UI interactions.              |
| `tests/`             | Contains automated test classes that define test scenarios and assertions.               |
| `test_data/`         | Contains test data used by automated tests.                                              |
| `utils/`             | Contains reusable utilities and the script for generating Allure reports locally.        |
| `.gitignore`         | Specifies files and directories that should not be tracked by Git.                       |
| `pytest.ini`         | Contains pytest configuration settings.                                                  |
| `README.md`          | Contains the project overview, technology stack, structure, and usage instructions.      |

</details>

