# Reqres Sample API Testing using Python
This repository contains a sample API testing framework in Python for testing the Reqres API. The framework is designed to demonstrate how to perform automated API testing using popular libraries and tools.

## Requirements
To run this project, you need to have the following installed on your system:
</br>
- Python 3.x
- pip (Python package manager)

## Installation
1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/absiddik7/API_Testing_Python
   ```

2. Navigate to the project directory:
   ```bash
   cd API_Testing_Python
   ```
4. Install the required dependencies:
    ```bash
   pip install -r requirements.txt
    ```
   
## Usage
This project uses Pytest for writing and running test cases. The test cases are written in Python and can be found under the 'test' directory.

## Running all the Tests
   To run all the test cases, use the following command:
   ```bash
   pytest
   ```
      
## Running a Specific Test
To run a specific test cases, use the following command (ex: pytest test_folder/test_file_name.py):
```bash
pytest test/test_create_user.py
```
## Generate HTML Rport
To run and generate full HTML details report of all the executed test, you can simply write the following commands on Terminal:
Install Pytest-HTML by writing the following command on Terminal
 ```bash
   pip install pytest-html
   ```
Then write the following command on Terminal
 ```bash
   pytest --html==YOUR_REPORT_FILE_NAME.html
   ```
For this project we generate the report file as below
```bash
   pytest --html==report.html
   ```
To see the reports, open the Project window, and then right-click report.html to open the file on a browser.
![image](https://github.com/absiddik7/API_Testing_Python/assets/49263226/a282b432-2fcb-4f39-b02c-3f5357066168)



