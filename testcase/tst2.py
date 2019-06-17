from validator import validate
dictionary = {
    "foo": "bar"
}
validation = {
    "foo": [lambda x: x == "bar"]
}
print(validate(validation,dictionary))