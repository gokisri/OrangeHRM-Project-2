OrangeHRM Project 2 – Selenium Pytest Automation Framework
A clean, modular automation framework using Python, Pytest, and Selenium WebDriver to test core functionalities of the OrangeHRM application.

 Tech Stack

Component         	     Description
Language	                Python
Testing Framework	        Pytest
Automation Tool	          Selenium WebDriver
IDE	                      PyCharm
Reporting	                pytest-html for HTML reports
Logging                 	Custom logs for test execution tracking

📁 Project Structure

orangehrm-project-2/
├── tests/
│   ├── test_forgot_password.py
│   ├── test_admin_title.py
│   ├── test_admin_headers.py
│   └── test_admin_main_menu.py
├── pages/
│   ├── login_page.py
│   ├── admin_page.py
├── config/
│   └── config.ini
├── utilities/
│   ├── custom_logger.py
│   ├── read_properties.py
│   └── screenshots/
├── Reports/
├── logs/
├── conftest.py
├── requirements.txt
└── README.md

Test Cases Covered


1️⃣ Forgot Password Link Validation
Navigate to Login Page

Verify username textbox is visible

Enter valid username

Click on Reset Password

✅ Expected: User sees the message:
"Reset Password link sent successfully"

2️⃣ Admin Page Title Validation
 
 Navigate to Admin Page

 Validate the title of the page

✅ Expected: "OrangeHRM"

3️⃣ Admin Page Headers Validation
Navigate to Admin Page

Validate the presence of these headers:

User Management

Job

Organization

Qualification

Nationalities

Corporate Banking

Configuration

✅ Expected: All headers are visible

4️⃣ Admin Page Side Menu Validation
Navigate to Admin Page

Validate the visibility of the following menu items on the left pane:

Admin

PIM

Leave

Time

Recruitment

My Info

Performance

Dashboard

Directory

Maintenance

Buzz

✅ Expected: All menu items are present




🔧 How to Run


1. Install dependencies:
pip install -r requirements.txt

2. Execute all test cases with HTML report:
   pytest -v -s --html=Reports/report.html --self-contained-html
   
4. Run a specific test:
   pytest tests/test_forgot_password.py

📸 Screenshots
On failure, screenshots are captured automatically and saved in:
utilities/screenshots/

🪵 Logs
Execution logs are saved in the logs/ folder with timestamps.

📄 Reports
HTML test reports are stored in the Reports/ directory and can be opened in a browser.

📌 Configurable via config.ini
Set your:
Base URL
Browser (chrome, firefox, edge)
Test credentials
















