# Unit Testing Libraries

### unittest
This library comes with Python. While in the folder `./tests/` run the following code
```bash
python3 -m unittest test_<file_name>.py
```
If you add the following lines in the script:
```python
if __name__ == '__main__':
    unittest.main()
```
then while in the folder `./tests/` run the following code
```bash
python3 test_<file_name>.py
```

### pytest
```sh
pip install pytest
```
While in the folder `./tests/` run the following code
```bash
pytest test_<file_name>.py
```
If you want to run a specific test from the `test_<file_name>.py`, then
```bash
pytest test_<file_name>.py::<function_name>
```
If you want to see the prints that are included in the script, then include the `-s` flag
```bash
pytest test_<file_name>.py::<function_name> -s
```

### pytest-mock
```sh
pip install pytest-mock
```

Then in the testing functions, we can use the mocker as a parameter.


### pytest-coverage
```sh
pip install pytest-cov
```
While in the folder `./tests/` run the following code
```bash
pytest --cov test_<file_name>.py
```

To create `.html` reports, while in the folder `./tests/` run the following code
```bash
coverage html
```
The `index.html` file will be saved inside the folder `htmlcov` in the test directory.