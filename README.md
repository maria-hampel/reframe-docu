# Reframe Docu

This is documentation for the Reframe HPC Framework, as well as some openly available Test Suites. Additionally, there are some simple tests in this repository.

## Documentation
The documentation can be found in the documentation subfolder. While ReframeHPC.md gives an overview of the framework, TestSuites.md contains test suites of different clusters, as well as a short description of the hpctestlib.

## Running tests
If you want to run the test suites, build and run the Docker container:
```bash
docker build -f Dockerfile -t first-test .
docker run -h myhost -it --mount type=bind,source=$(pwd),target=/home/user/test first-test:latest /bin/bash
cd test
```
Run a test by choosing a test and config file, e.g.:
```bash
reframe -C config/base.py -c first-test/test.py -r
```