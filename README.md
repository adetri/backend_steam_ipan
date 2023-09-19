# API Spec
## Authentication
All API must use this authentication

Request :

- Header :
  - X-Api-Key : "your secret api key"
## Login

Request :

- Method : POST
- Endpoint : /ath/login
- Header :
  - Content-Type: application/json
  - Accept: application/json
- Body :
```login
{
    "email" : "test@gmail.com",
    "password" : "testpass"
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
- Endpoint : /ath/refresh
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
