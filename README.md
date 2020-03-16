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
print(op.fetch(url=url))


## or using example
url = "https://petstore.swagger.io/v2/swagger.json"
op = HttpOperation(url=url)
print(op.fetch())


## close log 
from environment import Environment
Environment.Shared().online()

##on terminal excute
python lib/test_http.py

#builder with json parsing
op = HttpOperation()
jsonData = op.request(url=url).jsonParse()

op3 = HttpOperation()
responseString = op3.fetch(url=url)