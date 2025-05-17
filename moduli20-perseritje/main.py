data = {
    "name" : "Trim",
    "age": 17 ,
    "address" : {
        "street": "Prishtina",
        "zip" : 10000
         },
    "contact": [
        {
            "type": "email"
        },
        {
            "type":"phone"
        }
    ]
}

print(data["name"])

print(data["address"]["street"])

print(data["contact"][1]["type"])