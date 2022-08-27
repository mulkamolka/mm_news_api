```
pipenv --python 3.9
pipenv shell
pipenv sync
pipenv run start
pipenv run pytest
```


- development mode
```
DOT_ENV=development pipenv run start
```

- test mode
```
DOT_ENV=test pipenv run pytest
```


--- 
