## Poetry

### Add packages
```shell
$ poetry add <PACKAGE_NAME>
```

### Running tests
```shell
$ poetry run pytest
```

### Run application
```shell
$ poetry run uvicorn app.api.endpoints:app --reload 
```