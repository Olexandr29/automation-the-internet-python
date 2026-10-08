$resultsDir = "allure-results"
$reportDir = "allure-report"

# 1. Clean previous Allure results
if (Test-Path $resultsDir) {
    Remove-Item $resultsDir -Recurse -Force
}

New-Item -ItemType Directory -Force -Path $resultsDir | Out-Null

# 2. Create environment information
@"
os_platform=windows
os_release=11
os_version=10.0.26200
python_version=3.14.5
"@ | Set-Content "$resultsDir/environment.properties"

# 3. Create executor information
@"
{
  "reportName": "My local Allure report",
  "name": "Local",
  "buildName": "Local Test Run"
}
"@ | Set-Content "$resultsDir/executor.json" -Encoding UTF8

# 4. Restore history from previous report
$previousHistory = "$reportDir/history"
$currentHistory = "$resultsDir/history"

if (Test-Path $previousHistory) {
    Copy-Item -Path $previousHistory `
              -Destination $currentHistory `
              -Recurse `
              -Force

    Write-Host "Allure history restored."
}
else {
    Write-Host "Previous Allure history not found. First run."
}

# 5. Run tests
pytest -s @args --alluredir=$resultsDir

if ($LASTEXITCODE -ne 0) {
    Write-Warning "Tests failed. Allure report will still be generated."
}

# 6. Generate Allure report
allure generate $resultsDir -o $reportDir --clean

if ($LASTEXITCODE -ne 0) {
    throw "Allure report generation failed."
}

# 7. Open Allure report
allure open $reportDir