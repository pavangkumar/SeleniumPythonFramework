# 🐍 Selenium Python Framework

A simple **Selenium Python Test Automation Framework** using **Pytest**,
**Page Object Model (POM)**, and **Data-Driven Testing**.

------------------------------------------------------------------------

## 📂 Project Structure

``` bash
SeleniumPythonFramework
│── allure-results/
│── configurations/
│── data/
│── logs/
│── pages/
│── reports/
│── tests/
│── utilities/
│   ├── install_packages.bat
│   ├── requirements.txt
```

------------------------------------------------------------------------

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/your-username/SeleniumPythonFramework.git
cd SeleniumPythonFramework
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

``` bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Running Tests

### Run all tests

``` bash
pytest -v -s
```

### Run tests by tag (example: smoke)

We use `@pytest.mark.smoke` for tagging tests.

``` bash
pytest -v -s -m smoke
```

------------------------------------------------------------------------

## 📊 Reports

### 1️⃣ Generate **HTML Report**

``` bash
pytest --html=reports/report.html --self-contained-html
```

Report will be saved in `reports/` folder.

### 2️⃣ Generate **Allure Report** (if configured)

``` bash
pytest --alluredir=allure-results
allure serve allure-results
```

------------------------------------------------------------------------

## 🔗 Workflow Diagram

``` mermaid
flowchart TD
    A[Clone Repository] --> B[Install Dependencies]
    B --> C[Run Tests]
    C --> D[Generate Reports]
    D --> E[View Results]
```

------------------------------------------------------------------------

✅ Now you're ready to run and explore the framework! 🚀
