# AQA Python - Test Automation Learning Project

## 🛠 Technologies Used

## 🚀 Setup

## 🧪 Running Tests

**Basic test execution:**

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_users.py

# Run specific test
pytest tests/test_users.py::test_get_users

Run the test and show `print()` output in the console:
pytest -s tests/test_users.py::test_get_users

Run with verbose output:
pytest -s -v tests/test_users.py::test_get_users