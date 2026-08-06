# AQA API Tests

A Python API test automation project for the [GoREST Users API](https://gorest.co.in/). The repository demonstrates automated REST API testing of user CRUD operations, input validation, authentication behavior, and query filtering. It is structured as a small reusable test framework rather than a collection of direct HTTP calls inside tests.

## Technology stack

- **Python 3.11** — runtime used by the CI workflow.
- **Pytest 9.0.3** — test runner, fixtures, assertions, and parametrized validation checks.
- **Requests 2.33.1** — HTTP client for REST API calls.
- **python-dotenv 1.2.2** — loads local API configuration from `.env`.
- **GitHub Actions** — installs dependencies and runs the suite on pushes and pull requests to `main`, with optional manual execution.

Dependency versions are pinned in `requirements.txt`.

## Test coverage

The suite contains 19 discovered tests covering:

- creating a user and verifying the response and presence in the users list;
- retrieving an existing user by ID and validating its returned fields;
- updating all user fields and confirming the changes with a subsequent GET request;
- deleting a user and confirming it can no longer be retrieved or listed;
- `404` responses and error bodies for non-existent user IDs;
- required-field validation for name, gender, email, and status through Pytest parametrization;
- requests with missing or invalid authorization tokens, including the API's endpoint-specific behavior;
- public access to the users list without a token;
- filtering users by status and partial name.

Tests validate HTTP status codes and JSON response content. Tests that create data generate unique email addresses and clean up created users after execution.

## Project structure

```text
.
├── .github/workflows/api-tests.yml  # GitHub Actions workflow
├── .env.example                     # Required configuration keys
├── requirements.txt                 # Pinned Python dependencies
├── src/aqa_api/
│   ├── api_client.py                # Shared HTTP request function
│   ├── config.py                    # Environment configuration
│   ├── data_generators.py           # Unique test email generation
│   ├── test_data.py                 # Shared payloads and constants
│   └── users_api.py                 # Users endpoint functions
└── tests/
    ├── conftest.py                  # Test data and lifecycle fixtures
    └── users/                       # CRUD, validation, auth, and filter tests
```

The request layer is separated from test logic: `api_client.py` builds and sends requests, while `users_api.py` exposes endpoint-specific functions used by the tests.

## Setup and execution

Clone the repository and enter its directory:

```bash
git clone https://github.com/vitaliiyz/aqa-api-tests.git
cd aqa-api-tests
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the pinned dependencies:

```bash
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and provide the GoREST API URL and your own access token. Do not commit this file.

```dotenv
BASE_URL=https://gorest.co.in/public/v2
ACCESS_TOKEN=YOUR_API_TOKEN
```

Run the complete suite from the repository root:

```bash
python -m pytest -v
```

## Framework highlights

- A shared request client applies the base URL and default bearer-token headers.
- Endpoint wrappers keep HTTP details out of test cases.
- Function-scoped fixtures prepare fresh payloads and manage created-user cleanup with `yield` teardown.
- UUID-based email generation prevents collisions between test runs.
- Shared helpers reduce duplication in non-existent-resource checks.
- Parametrization runs the same required-field validation against four payload fields.

## CI

The `API tests` GitHub Actions workflow runs on pushes and pull requests targeting `main`, and through manual dispatch. It uses Ubuntu and Python 3.11, restores the pip cache, installs `requirements.txt`, and executes `pytest -v`. `BASE_URL` and `ACCESS_TOKEN` are supplied through GitHub repository secrets. No test-report publishing or artifact upload is currently configured.
