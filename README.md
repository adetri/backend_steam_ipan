# API Spec
## Authentication
All API must use this authentication

Request :

- Header :
  - X-Api-Key : "your secret api key"
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

## Input Item

Request :

- Method : POST
- Endpoint : **/item/additem**
- Header :
  - Content-Type: application/json
  - Accept: application/json
- Body :
```refresh
{
    "name" : "Item Name",
    "price" : "100000",
    "category" : "1",
    "discount" : "0",
    "subitem" :
      {
          "name" : "sub item name 1",
          "price" : "0",
          "discount" : "0",
      },
      {
          "name" : "sub item name 2",
          "price" : "1000",
          "discount" : "100",
      }


}
```
Response :
```login_response
{

    "code" : "201",
    "item_id" : "Item ID"
}
```


## Update Item

Request :

- Method : POST
- Endpoint : **/item/updateitem/{item_id}**
- Header :
  - Content-Type: application/json
  - Accept: application/json
- Body :
```refresh
{
    "id" : "Item ID",
    "name" : "Item Name",
    "price" : "100000",
    "category" : "1",
    "discount" : "0",

}
```
Response :
```login_response
{

    "code" : "202",
    "item_id" : "Item ID"
}
```


## Update Sub Item

Request :

- Method : POST
- Endpoint : **/item/updatesubitem/{item_id}**
- Header :
  - Content-Type: application/json
  - Accept: application/json
- Body :
```refresh
{
    "id" : "Item ID",
    "name" : "Item Name",
    "price" : "100000",
    "discount" : "0",

}
```
Response :
```login_response
{

    "code" : "202",
    "item_id" : "Item ID"
}
```

## Get one Item

Request :

- Method : GET
- Endpoint : **/item/get/{item_id}**
- Header :
  - Content-Type: application/json
  - Accept: application/json

Response :
```login_response
{

    "code" : "200",
    "item_id" : "Item ID"
    "name" : "Item Name",
    "price" : "100000",
    "discount" : "0",
    "subitem" :
          {
              "name" : "sub item name 1",
              "price" : "0",
              "discount" : "0",
          },
          {
              "name" : "sub item name 2",
              "price" : "1000",
              "discount" : "100",
          }

}
```


## Get one Sub Item

Request :

- Method : GET
- Endpoint : **/item/getsubitem/{subitem_id}**
- Header :
  - Content-Type: application/json
  - Accept: application/json

Response :
```login_response
 {
    "id" : "sub item name 1",
    "name" : "sub item name 1",
    "price" : "0",
    "discount" : "0",
},
```

## Get Item By Category

Request :

- Method : GET
- Endpoint : **/item/getbycategory/{category_id}**
- Header :
  - Content-Type: application/json
  - Accept: application/json

Response :
```login_response
{
      "data" :
  [{
      "item_id" : "Item ID"
      "name" : "Item Name",
      "price" : "100000",
      "discount" : "0",
      "subitem" :
            {
                "name" : "sub item name 1",
                "price" : "0",
                "discount" : "0",
            },
            {
                "name" : "sub item name 2",
                "price" : "1000",
                "discount" : "100",
            }
      },{
      "item_id" : "Item ID"
      "name" : "Item Name",
      "price" : "100000",
      "discount" : "0",
      "subitem" :
            {
                "name" : "sub item name 1",
                "price" : "0",
                "discount" : "0",
            },
            {
                "name" : "sub item name 2",
                "price" : "1000",
                "discount" : "100",
            }
      }
  
  ]
      "code" : "200",
}
```



