# API Spec
## Authentication
All API must use this authentication

Request :

- Header :
  - Authorization : "Bearer < token >"
## Login

Request :

- Method : POST
- Endpoint : **/ath/login**
- Header :
  - Content-Type: application/json
  - Accept: application/json
- Body :
```login
{
    "username" : "usename",
    "password" : "password"
}
```
Response :
```login_response
{
    "access" : "Acces Token",
    "refresh" : "Refresh Token"
}
```

## Refresh Token

Request :

- Method : POST
- Endpoint : **/ath/refresh**
- Header :
  - Content-Type: application/json
  - Accept: application/json
- Body :
```refresh
{
    "refresh" : "refresh Token",
}
```
Response :
```login_response
{

    "access" : "Acces Token",
    "refresh" : "Refresh Token"
}
```

## Get all pegawai

Request :

- Method : GET
- Endpoint : **/pegawai/fatch-all-pegawai**
- Header :
  - Content-Type: application/json
  - Accept: application/json
  - Authorization : "Bearer YOUR_ACCESS_TOKEN",
- Response :
```login_response
{
    "pegawai": [
        {
            "id": 2,
            "role": {
                "id": 2,
                "name": "Admin",
                "level": 2
            },
            "name": "det2",
            "phone": "085157792607"
        },
        {
            "id": 3,
            "role": {
                "id": 2,
                "name": "Admin",
                "level": 2
            },
            "name": "",
            "phone": "0851577922607"
        },
        {
            "id": 4,
            "role": {
                "id": 2,
                "name": "Admin",
                "level": 2
            },
            "name": "test2312",
            "phone": "0851577926107"
        },
        {
            "id": 5,
            "role": {
                "id": 2,
                "name": "Admin",
                "level": 2
            },
            "name": "test2312",
            "phone": "08515779261207"
        }
    ]
}
```

## Get pegawai

Request :

- Method : GET
- Endpoint : **/pegawai/get-pegawai/{pk}**
- Header :
  - Content-Type: application/json
  - Accept: application/json
  - Authorization : "Bearer YOUR_ACCESS_TOKEN",

- Response :
```login_response
{
    "pegawai": {
        "id": 2,
        "role": {
            "id": 2,
            "name": "Admin",
            "level": 2
        },
        "name": "det2",
        "phone": "085157792607"
    },
    "msg": "Success"
}
```

## Update Pegawai

Request :

- Method : PUT
- Endpoint : **/pegawai/edit-pegawai/{pk}**
- Header :
  - Content-Type: application/json
  - Accept: application/json
  - Authorization : "Bearer YOUR_ACCESS_TOKEN",

- Body :
```login_response

{
       
        "name": "det",
        "phone": "085157792607",
        "role": 1
}

```
- Response :
```login_response
{

    "pegawai": {
        "id": 1,
        "name": "det",
        "phone": "085157792607",
        "role": 1
    },
    "msg": "Success"

}
```
## Delete pegawai

Request :

- Method : DELETE
- Endpoint : **/pegawai/delete-pegawai/{pk}**
- Header :
  - Content-Type: application/json
  - Accept: application/json
  - Authorization : "Bearer YOUR_ACCESS_TOKEN",

- Response :
```login_response
{
    "msg": "Delete data success"
}
```

## Insert Pegawai

Request :

- Method : POST
- Endpoint : **/pegawai/reate-pegawai**
- Header :
  - Content-Type: application/json
  - Accept: application/json
  - Authorization : "Bearer YOUR_ACCESS_TOKEN",

- Body :
```login_response

{
    "name": "test2312",
    "phone": "08515779261207",
    "role": 2
}

```
- Response :
```login_response
{
    "msg": "Success",
    "pegawai": {
        "id": 5,
        "name": "test2312",
        "phone": "08515779261207",
        "role": 2
    }
}
```


## Get All Role

Request :

- Method : GET
- Endpoint : **/pegawai/fatch-all-role**
- Header :
  - Content-Type: application/json
  - Accept: application/json
  - Authorization : "Bearer YOUR_ACCESS_TOKEN",

- Response :
```login_response
{
    "role": [
        {
            "id": 1,
            "name": "DEV",
            "level": 1
        },
        {
            "id": 2,
            "name": "Admin",
            "level": 2
        }
    ]
}
```
## Get Role

Request :

- Method : GET
- Endpoint : **/pegawai/get-role/{pk}**
- Header :
  - Content-Type: application/json
  - Accept: application/json
  - Authorization : "Bearer YOUR_ACCESS_TOKEN",

- Response :
```login_response
{
    "role": {
        "id": 2,
        "name": "Admin",
        "level": 2
    }
}
```

## Update Pegawai

Request :

- Method : PUT
- Endpoint : **/pegawai/edit-role//{pk}**
- Header :
  - Content-Type: application/json
  - Accept: application/json
  - Authorization : "Bearer YOUR_ACCESS_TOKEN",

- Body :
```login_response

{
    "name": "admitest",
    "level": 3   
}

```
- Response :
```login_response
{
    "role": {
        "id": 2,
        "name": "admitest",
        "level": 3
    },
    "msg": "Update Success"
}
```

## Delete pegawai

Request :

- Method : DELETE
- Endpoint : **/pegawai/delete-role/{pk}**
- Header :
  - Content-Type: application/json
  - Accept: application/json
  - Authorization : "Bearer YOUR_ACCESS_TOKEN",

- Response :
```login_response
{
    "msg": "Delete data success"
}
```

