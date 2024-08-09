# Locust Overview
A look into using Locust to validate notifications. Only for demo purposes, ideally containerize and deploy.

Documentation [here](https://docs.locust.io/en/stable/what-is-locust.html)

1. Use Python 3.11 (pyenv recommended if using multiple Python versions)
2. Install Poetry
3. Pull down this repo
4. Run `poetry install`
5. Copy the `example.env` file locally to .env and add information (project would use boto3 to pull these secrets)
6. Run the tests:
```
locust -f load_test_email.py -u 2 -r 1 -t 10s -H https://sandbox-api.va.gov/vanotify --headless
```

arguments:
- `-f` filename to run
- `-u` int, number of users to spawn
- `-r` float, rate per second at which to spawn users
- `-t` time string, stop after specified time, run only with headless or auto-start, else runs forever
- `-H` base url, here defaults to Perf
- `--headless`  disables the web interface
