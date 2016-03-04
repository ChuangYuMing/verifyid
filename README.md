# verifyid
驗證身分證字號

##使用
```
pip install verifyid
```

```python
from verifyid import verifyid

verify = verifyid.IdentyNumber()
verify.check_identy_number("your number")   # return True or False
verify.get_city(your number)  # return city name ex:("高雄市")
```
