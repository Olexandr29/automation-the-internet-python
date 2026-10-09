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



<details><summary><b>Components and Responsibilities</b></summary>

<details><summary>I) Pages</summary>

The framework follows the Page Object Model (POM) approach. Page-specific UI interactions are encapsulated in dedicated Page Object classes, while shared browser interaction functionality is provided by the `BasePage` class.

1) BasePage

`BasePage` is a common base class inherited by the Page Object classes.

It provides shared functionality for:

- WebDriver and explicit wait management;
- Element location and visibility-based synchronization;
- Reusable UI interactions, such as clicking, typing, etc.;
- Keyboard and browser navigation operations;
- Logging through the custom Logger utility;
- Reporter — provides reusable test steps with console logging and optional Allure integration.


The class reduces duplication across Page Objects by centralizing common browser interaction functionality.

2) Page Object Classes

Each Page Object represents a specific page or functional area of the application under test.

| Component | Responsibility |
|---|---|
| `HomePage` | Provides navigation to the main application sections, including login, dropdown, checkbox, and broken images pages. |
| `LoginPage` | Encapsulates login form interactions, successful and unsuccessful authentication scenarios, and password field verification. |
| `SecurePage` | Represents the authenticated page and provides methods for verifying page content and logging out. |
| `DropdownPage` | Encapsulates dropdown visibility, option selection, keyboard interaction, and focus verification. |
| `CheckboxPage` | Encapsulates checkbox visibility, selection state verification, state changes, and keyboard interactions. |
| `BrokenImagesPage` | Encapsulates broken images page interactions, image count and visibility checks, and image loading verification. |

Page Objects use the shared functionality inherited from `BasePage` while exposing methods specific to their respective pages and UI components.
</details>


<details><summary>II) Test</summary>

The test layer contains automated test scenarios that verify the expected behavior of the application under test.

The test layer is implemented using **pytest** and follows the Page Object Model approach. Test classes interact with Page Objects instead of directly locating and manipulating web elements.

| Component        | Responsibility                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `BaseTest (base_test.py)`       | Provides shared test setup, Chrome WebDriver initialization, browser configuration, initial navigation to the aplication home page, and browser cleanup.            |
| `conftest.py`       | Implements a pytest test-reporting hook that attaches a screenshot to the Allure report when a test fails during its execution phase.       |
| `TestLogin (test_login.py)`      | Verifies successful and unsuccessful login scenarios, logout behavior, secure area access after logout, and password field maskig.   |
| `TestDropdown (test_dropdown.py)`   | Verifies dropdown visibility, available options, option selection, keyboard interaction, and browser navigation behavior. |
| `TestCheckbox (test_checkbox)`    | Verifies checkbox visibility, initial states, state changes, behavior after refresh, and keyboard interaction.                  |
| `TestBrokenImages (test_broken_images)` | Verifies page content, dociment readiness, header and footer elements,image count, and image loading status.                                           |

Test classes use assertions to validate application behavior and are organized into logical groups such as `smoke` and `regression`.

Parametrized tests use `pytest.mark.parametrize` to execute the same test logic with different input values. For example, `TestLogin` uses parametrized credentials and expected messages to cover multiple unsuccessful login scenarios.

1) BaseTest

`BaseTest` is the common base test class that provides shared test setup and teardown functionality throught the `setup_test` pytest fixture.

Its responsibilities include:

* Creating a Chrome WebDriver instance before each test;
* Configuring browser options, including incognito mode;
* Enabling headless execution in GitHub Actions;
* Initializing the `HomePage` Page Object;
* Opening the application home page;
* Closing the WebDriver session after each test exectution.

The `setup_test` fixture uses `yield` to separate test setup from teardown. After the test finishes, `driver.quit()` closes the browser session.

2) conftest.py
`conftest.py` constains a `pytest_runtest_makereport` hook that integrates test failure handling with Allure reporting.

Its responsibilities include:
- Inspecting the result of each test execution phase;
- Detecting failures during the test call phase;
- Retrieving the WebDriver instance from the test class;
- Capturing a browser screenshot;
- Attaching the screenshot to the Allure report as a PNG image.

The screenshot is capture when test fails during its execution phase, provided the test instance exposes a `driver` attribute.

3) Test Page Initialization
Each test class defines an additional autouse fixture that depends on `setup_test`. It opens the corresponding page through the `HomePage` Page object and wraps the navigation step in `Reporte.step` for reporting.

This approach keeps browser initialization in BaseTest and page-specific navigation in the respective test classes.

</details>


<details><summary>III) Test Data Modules</summary>

Test data is stored in dedicated Python modules under the `test_data/` directory.

These modules centralize page URLs, valid and invalid input values, expected messages, and expected UI values used by the test scenarios.

| Component          | Responsibility                                                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `LoginData`        | Stores valid and invalid credentials, security-related input values, expected authentication and logout messages, and page URLs.                             |
| `DropdownData`     | Stores the dropdown page URL and expected option labels, including the default option.                                                                       |
| `CheckboxData`     | Stores the checkboxes page URL and checkbox identifiers used in test assertions.                                                                             |
| `BrokenImagesData` | Stores the page URL, expected header and footer content, expected image count, footer link text, and a method for generating image-related warning messages. |

The test data classes provide reusable values for test methods, reducing duplicated data in test implementations and separating test data from test execution logic.

</details>

<details><summary>IV) Allure Reporting</summary>

Allure Report is used to collect and present test execution results, reporting steps, environment information, execution metadata, and failure screenshots in an interactive HTML report.

The framework integrates Allure with pytest through `allure-pytest`. The `Reporter` utility provides reporting steps, while the `pytest_runtest_makereport` hook in `conftest.py` attaches screenshots when tests fail during the call phase. See **II) Tests** for details of the failure screenshot handling.

**Local Allure Reporting**

A PowerShell script automates local test execution and Allure report generation.

Its responsibilities include:

* Cleaning previous test results and creating a fresh `allure-results/` directory;
* Adding environment information to `environment.properties`;
* Adding execution metadata to `executor.json`;
* Restoring report history from the previous `allure-report/history/` directory, when available;
* Running pytest with Allure result collection enabled;
* Generating the HTML report in `allure-report/`;
* Opening the generated report in a browser.

If tests fail, the script displays a warning and continues with report generation. If report generation fails, the script terminates with an error.

Local execution flow:

```text
PowerShell script
       ↓
Clean allure-results/
       ↓
Configure environment.properties
       ↓
Configure executor.json
       ↓
Restore previous Allure history
       ↓
pytest --alluredir=allure-results
       ↓
Generate Allure report
       ↓
Open report in browser
```

**GitHub Actions Reporting and Deployment**

The GitHub Actions workflow `Run tests on Linux` automates test execution and report publication.

The workflow runs on pushes and pull requests targeting `main`, manual dispatch, and a weekly schedule.

The `test` job performs the following operations:

* Checks out the repository;
* Sets up Python 3.12 and Java 17;
* Installs Allure Commandline and the Python test dependencies;
* Restores previous Allure history from the GitHub Actions cache;
* Runs pytest with Allure result collection enabled;
* Adds environment information and execution metadata;
* Generates the Allure HTML report;
* Saves report history to the cache;
* Uploads the raw Allure results as a workflow artifact;
* Uploads the generated HTML report as a GitHub Pages artifact.

The `deploy` job depends on the `test` job and publishes the uploaded Pages artifact to GitHub Pages. Its `if: always()` condition allows deployment to run even if the preceding job fails, provided the required deployment steps and artifacts are available.

CI execution and deployment flow:

```text
GitHub Actions
       ↓
Checkout repository
       ↓
Setup Python + Java + Allure
       ↓
Install Python dependencies
       ↓
Restore Allure history from cache
       ↓
Copy history → allure-results/history
       ↓
Run pytest with Allure
       ↓
Configure environment.properties
       ↓
Configure executor.json
       ↓
Generate Allure report
       ↓
Save Allure history to cache
       ↓
Upload Allure Results artifact
       ↓
Upload Allure Report as Pages artifact
       ↓
Deploy job
       ↓
GitHub Pages
```

**Local vs CI Allure Reporting**

| Stage                | Local                      | CI                         |
| -------------------- | -------------------------- | -------------------------- |
| Test execution       | PowerShell script + pytest | GitHub Actions + pytest    |
| History restoration  | Previous local report      | GitHub Actions cache       |
| Environment metadata | `environment.properties`   | `environment.properties`   |
| Execution metadata   | `executor.json`            | `executor.json`            |
| Report generation    | `allure generate`          | `allure generate`          |
| Open report          | `allure open`              | Not required               |
| Raw results          | `allure-results/`          | Uploaded workflow artifact |
| Report publication   | Local browser              | GitHub Pages               |

See the [published Allure report](https://olexandr29.github.io/automation-the-internet-js/) for an example of the reporting output.

</details>




</details>


