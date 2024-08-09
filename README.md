# Locust Overview
A look into using Locust to validate notifications. This is only for demo purposes, ideally we would containerize and deploy.

1. Use Python 3.11 (pyenv recommended if using multiple Python versions)
2. Install Poetry
3. Pull down this repo
4. Run `poetry install`
5. Copy the `example.env` file locally to .env and add information (project would use boto3 to pull these secrets)
6. Run the tests:
```
locust -f load_test_email.py -u 1 -r 1 --run-time 2s --host https://sandbox-api.va.gov/vanotify --headless
```