# RTUITLAB_backend

# Introduction

This is a 3 level project consist of purchase, shop and factory services, created by Suroegin Konstantin from IVBO-07-19
group. This project had been realised with djangorest framework. Every service connected with own database (Sqlite3). In
this project I used default django pattern MVC (Model-View-Control).

The main goal of services is:

- factory produces products and sending it to shops service.
- shops provides to user possibility to view shops and products list, adding in to cart and buy. After buying check
  sends to purchase service.
- purchases store users checks.

# Install and Run services

To install services, clone this repository. In every project folder create .env file, that provide security of data. At
factory .env must consist "SHOP_SECRET_KEY" and "SECRET_KEY", at shop - "PURCHASE_SECRET_KEY" and "SECRET_KEY", at
purchase - "SECRET_KEY". After in project directory run this commands:

```
  docker-compose pull
  docker-compose up
```

If errors occur, the ```docker-compose up --build``` can help. Download my docker image ,if it is still not working.

# API documentation

## Auth requests

Auth requests for Purchase and Shop is the same that differ only start of path. Factory app has not auth functions.

## POST /auth/jwt/create/

Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of
those credentials

#### Example

Request example

```json
{
  "email": "admin@mirea.ru",
  "password": "admin"
}
```

Response example

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxODQ4OTAyMCwianRpIjoiMGZkOThiZWEzYWMyNDEyY2E4NzQzMGJjZTk0MmYxMDAiLCJ1c2VyX2lkIjoxfQ.DpIyRE8ZnKeAbyaJPL0gykO8jN0OZnrZmm1IP_3mT3U",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MDIwLCJqdGkiOiI0ZWRhZmM5Mzc1Zjk0Nzk3YWZhYzg5NDEzMDkyYzAxMyIsInVzZXJfaWQiOjF9.dtUvmEQsEAUya0AcUTbMhQdGA09ViGWUFxRBPz-D8_w"
}
```

## POST /auth/jwt/create/

Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of
those credentials

#### Example

Request example

```json
{
  "email": "admin@mirea.ru",
  "password": "admin"
}
```

Response example

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxODQ4OTAyMCwianRpIjoiMGZkOThiZWEzYWMyNDEyY2E4NzQzMGJjZTk0MmYxMDAiLCJ1c2VyX2lkIjoxfQ.DpIyRE8ZnKeAbyaJPL0gykO8jN0OZnrZmm1IP_3mT3U",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MDIwLCJqdGkiOiI0ZWRhZmM5Mzc1Zjk0Nzk3YWZhYzg5NDEzMDkyYzAxMyIsInVzZXJfaWQiOjF9.dtUvmEQsEAUya0AcUTbMhQdGA09ViGWUFxRBPz-D8_w"
}
```

## POST /auth/jwt/refresh/

Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.

#### Example

Request example

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxODQ4OTE0MywianRpIjoiNDFkZjgxZDg1NTU1NDljMjlkNWVhNWMzYmRkODMxYzUiLCJ1c2VyX2lkIjoxfQ.rx6xjfqOpOHoTjLh0rQpuPH0LPnFv2k8fSYo6Yvy8jA"
}
```

Response example

```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

/////////////////////////////////////////////////////////////////////////////////////////////////////

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

## POST /auth/jwt/verify/

Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular
use.

#### Example

Request example

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NDg5MTY2LCJqdGkiOiJmMWJjOTUzMDMxZjY0NDM3ODlkN2NhNTJlMWNhYjJkYyIsInVzZXJfaWQiOjF9.TRY027u3X6fbdQGatXSo6eyKoZ6GkS52vg3ClxkwwrU"
}
```

Response example

```json
{}
```

///////////////////////////////////////////////////////////////////

## Purchase service

### POST /create_purchase

Connecting shop and purchase services and create purchase objects (checks). Return all purchase by category. Permission
level: owner

/////////////////////////////////////////////////////////////////////////////////////

## Shop service

### GET /shops

Return list of shops. Pagination available. Permission level : Anyone

#### Example

Response example

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "503shop",
      "category_choicer": "electronics"
    }
  ]
}
```

---

### GET /shops/<int:shop_pk>

Return list of products, that can be bought in this shop. Pagination available. Permission level : Anyone

#### Example

Response example

```json
[
  {
    "id": 2,
    "title": "macbook"
  },
  {
    "id": 1,
    "title": "iphone 69"
  },
  {
    "id": 3,
    "title": "apple watch"
  }
]
```

---

### GET /shops/<int:shop_pk>/<int:product_pk>

Return information about product. Permission level : Anyone

#### Example

Response example

```json
{
  "id": 1,
  "title": "iphone 69",
  "description": "sadasd",
  "price": "1500.00",
  "quantity": 40,
  "moderated": true,
  "shop": {
    "id": 1,
    "title": "503shop",
    "address": "asd",
    "phone_number": "asdasd",
    "category_choicer": "electronics"
  }
}
```

---

### POST /add_to_cart/<int:pk>

Adding product to ur cart. Be sure, that in ur cart products from one shop otherwise security will punish you.
Permission level : only owner of cart

#### Example

Request example

```json
{
  "quantity": 2
}
```

Response example

```json
{
    "id": 1,
    "final_price": "1110.00",
    "cartproduct_set": [
        {
            "id": 1,
            "quantity": 2,
            "price": "1110.00",
            "main_product": {
                "id": 3,
                "title": "apple watch",
                "description": "1",
                "price": "555.00",
                "quantity": 80,
                "moderated": true,
                "shop": 1
            },
            "cart": {
                "id": 1,
                "final_price": "1110.00",
                "current_shop": "503shop",
                "owner": 2
            }
        }
    ]
}
```
---

## DELETE /delete_from_cart/<int:cp_pk>

Opposite to previous. Delete product from cart.
Permission level : only owner of cart

#### Example

Response example

```json
{
    "id": 1,
    "final_price": "0.00",
    "cartproduct_set": []
}
```

###DELETE /clear_cart
Delete all products from your cart.
Permission level : only owner of cart
####Example
Response example
```json
{
    "id": 1,
    "final_price": "0.00",
    "cartproduct_set": []
}
```
---
### GET /cart_list
Return list of products in your cart
Permission level : only owner of cart
####Example
Response example
```json
{
    "id": 1,
    "final_price": "1110.00",
    "cartproduct_set": [
        {
            "id": 1,
            "quantity": 2,
            "price": "1110.00",
            "main_product": {
                "id": 3,
                "title": "apple watch",
                "description": "1",
                "price": "555.00",
                "quantity": 90,
                "moderated": true,
                "shop": 1
            },
            "cart": {
                "id": 1,
                "final_price": "1110.00",
                "current_shop": "503shop",
                "owner": 2
            }
        }
    ]
}
```
---
### POST /purchase
Buy all products in your carts and send request to add purchase.
Permission level : only owner of cart
####Example
Response example
```json
{
    "key": "1",
    "email": "kek@mirea.ru",
    "category": "electronics",
    "title": "503shop",
    "final_price": 970.0,
    "products": "[{\"id\": 1, \"title\": \"iphone 69\", \"quantity\": 2}]"
}
```
---
### POST /delivery
System path needed to delivery products

---


### GET /moderate/<int:pk>
Returns all not moderated products.
Permission level : admin
####Example

Response example
```json
[
    {
        "id": 1,
        "title": "iphone 69",
        "description": "",
        "price": null,
        "quantity": 120,
        "moderated": false,
        "shop": {
            "id": 1,
            "title": "503shop",
            "address": "asd",
            "phone_number": "asdasd",
            "category_choicer": "electronics"
        }
    },
    {
        "id": 3,
        "title": "apple watch",
        "description": "",
        "price": null,
        "quantity": 150,
        "moderated": false,
        "shop": {
            "id": 1,
            "title": "503shop",
            "address": "asd",
            "phone_number": "asdasd",
            "category_choicer": "electronics"
        }
    }
]
```
---
### PATCH /moderate/<int:pk>
Needed to moderate products (price and description).
Permission level : admin
####Example
Request example
```json
{
    "price":15,
    "description":"yes"
}
```

Response example
```json
{
    "id": 2,
    "title": "macbook",
    "description": "yes",
    "price": "15.00",
    "quantity": 56,
    "moderated": true,
    "shop": {
        "id": 1,
        "title": "503shop",
        "address": "asd",
        "phone_number": "asdasd",
        "category_choicer": "electronics"
    }
}
```
---


### POST /create_request
Send cooperation request to factory
Permission level : admin
####Example
Request example
```json
{
    "factory":"503zavod",
    "shop":"503shop",
    "products":[
        {
            "title":"kek",
            "quantity":3
        },
        {
            "title":"lol",
            "quantity":2
        }
    ]
}
```

Response example
```json
{
    "factory": "503zavod",
    "shop": "503shop",
    "category": "electronics",
    "products": "[{\"title\": \"kek\", \"quantity\": 3}, {\"title\": \"lol\", \"quantity\": 2}]"
}
```
---

## Factory service

Every path to this service starts with ```/api/factory/```

## POST /delivery

Can start delivery process by admin. Response status code and message.

## POST /request

This path is used to connect shop and factory. Here is used SECRET_KEY to protect data. Because of this it is able
requested only from shop app.

## POST /request

Creating DeliveryRequest that connect Shop and Factory. Return products, that will be produced by factory and code 201,
if something goes wrong return error code and message.

#### Example

Request example

```json
{
  "key": "1",
  "factory": "factory_name",
  "category": "grocery",
  "shop": "shop_name",
  "products": [
    {
      "title": "product1_title",
      "quantity": 10
    },  
    {
      "title": "product2_title",
      "quantity": 11
    }
  ]
}

