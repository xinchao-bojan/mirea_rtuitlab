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
## Admin panel

To have access to the admin panel enter /admin after the service path

## Auth requests

Auth requests for Purchase and Shop is the same that differ only start of path. Factory app has not auth functions. There are a lot of functions in my authentication system (reset passwords and logins, deleting,patching users) but I will write only useful for this task

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
---


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
---

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
---

## POST /auth/users


#### Example

Request example

```json
{
  "email": "user@example.com",
  "password": "string"
}
```

Response example

```json
{
  "email": "user@example.com",
  "id": 2
}
```
---


///////////////////////////////////////////////////////////////////

## Purchase service

Every path to this service starts with ```/api/purchase/```
Superuser : login:admin@mirea.ru password: admin


### POST /create_purchase

Connecting shop and purchase services and create purchase objects (checks). Uses a secret key and cannot be called by
the user.

---

### GET /purchase_list

Return list of purchases. Permission level: owner Response example

#### Example

Response example

```json
[
  {
    "id": 19,
    "final_price": "12.00",
    "purchaseproduct_set": [
      {
        "id": 8,
        "title": "iphone 69",
        "product_pk": 1,
        "quantity": 2,
        "purchase": 19
      }
    ],
    "category": {
      "id": 5,
      "title": "electronics",
      "default": true,
      "owner": null
    },
    "pm_choicer": "default"
  },
  {
    "id": 20,
    "final_price": "9330.00",
    "purchaseproduct_set": [
      {
        "id": 9,
        "title": "iphone 69",
        "product_pk": 1,
        "quantity": 2,
        "purchase": 20
      },
      {
        "id": 10,
        "title": "macbook",
        "product_pk": 2,
        "quantity": 2,
        "purchase": 20
      }
    ],
    "category": {
      "id": 5,
      "title": "electronics",
      "default": true,
      "owner": null
    },
    "pm_choicer": "default"
  },
  {
    "id": 21,
    "final_price": "9122.00",
    "purchaseproduct_set": [
      {
        "id": 11,
        "title": "apple watch",
        "product_pk": 3,
        "quantity": 2,
        "purchase": 21
      }
    ],
    "category": {
      "id": 5,
      "title": "electronics",
      "default": true,
      "owner": null
    },
    "pm_choicer": "default"
  }
]
```

---

### GET /purchase_by_category/<str:category>

Return a list of purchases by category . Pagination available. Permission level : owner
#### Example

Response example

```json
[
    {
        "id": 20,
        "final_price": "9330.00",
        "purchaseproduct_set": [
            {
                "id": 9,
                "title": "iphone 69",
                "product_pk": 1,
                "quantity": 2,
                "purchase": 20
            },
            {
                "id": 10,
                "title": "macbook",
                "product_pk": 2,
                "quantity": 2,
                "purchase": 20
            }
        ],
        "category": {
            "id": 1,
            "title": "grocery",
            "default": true,
            "owner": null
        },
        "pm_choicer": "cash"
    }
]
```
---

### GET /update_purchase/<int:pk>

Return a list of purchases by personal key . Permission level : owner

#### Example

Response example

### PATCH /update_purchase/<int:pk>

Update category or payment method . Permission level : owner

#### Example

Response example

```json
{
  "id": 20,
  "final_price": "9330.00",
  "purchaseproduct_set": [
    {
      "id": 9,
      "title": "iphone 69",
      "product_pk": 1,
      "quantity": 2,
      "purchase": 20
    },
    {
      "id": 10,
      "title": "macbook",
      "product_pk": 2,
      "quantity": 2,
      "purchase": 20
    }
  ],
  "category": {
    "id": 1,
    "title": "grocery",
    "default": true,
    "owner": null
  },
  "pm_choicer": "cash"
}
```

---
###POST /create_category
Create custom category. Permission level: Owner
####Example
Request example
```json
{
    "title":"mirea"
}
```
Response example
```json
"Категория mirea успешно создана"
```
---

### GET /check_user

Check if user has account in purchase app by email.
#### Example
Request example
```json
{
    "email":"kek@mirea.ru"
}
```
Response satus code 200 

---

## Shop service
Every path to this service starts with ```/api/shop/```
Superuser : login:admin@mirea.ru password: admin

### GET /purchase_by_category/<str:category>

Return list of . Pagination available. Permission level : Anyone

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
Superuser : login:admin password: admin

## POST /delivery
Can start delivery process by admin. Return products that had been delivered or response status code and message.


Response example
```json
{
    "shop": "503shop",
    "products": "[{\"title\": \"iphone 69\", \"quantity\": 8}, {\"title\": \"macbook\", \"quantity\": 4}, {\"title\": \"apple watch\", \"quantity\": 10}]"
}

```
---

## POST /request

This path is used to connect shop and factory. Here is used SECRET_KEY to protect data. Because of this it is able
requested only from shop app.

