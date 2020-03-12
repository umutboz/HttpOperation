# httpOperation
Http Operations Libraries for Python

## import package example


```python
from httpOperation import HttpOperation
```

## using example
```python
url = "https://petstore.swagger.io/v2/swagger.json"
op = HttpOperation()
print(op.request(url=url))


## or using example
url = "https://petstore.swagger.io/v2/swagger.json"
op = HttpOperation(url=url)
print(op.request())


## close log 
from environment import Environment
Environment.Shared().online()

##on terminal excute
python lib/test_http.py