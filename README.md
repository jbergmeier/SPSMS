# SPSMS
Special Publication Sales Management System offeres the possibility to sell ads in special publications of a newspaper. The following backend description shows which endpoints can be used to insert users/customers, add new areas, add categories and create a booking in the system.

## Domain
__DEV:__
http://webcoffee-spsms-dev.herokuapp.com

## Authorization
Login and get token:
https://webcoffee.eu.auth0.com/authorize?audience=SPSMS-API-DEV&response_type=token&client_id=16zBUXWV3bO9qdlQjRiKEgtDRm0KFgyp&redirect_uri=https://localhost:5000

### Sample Test Users and Roles
__Admin Role:__
Username: spsms-admin@webcoffee.io
Password: admin001!

__Manager Role:__
Username: spsms-manger@webcoffee.io
Password: manager001!

__Sales Role:__
Username: spsms-sales@webcoffee.io
Password: sales001!

### Roles and Permissions in Auth0
__SPSMS-Administrator:__
Full access - Admin

__post:user__	Create new users	
__get:user__	Read User Details	
__post:group__	Create new Groups 
__get:group__	Read Group details	
__get:area__	Read are and fixed prices	
__post:area__	Create new areas and fixed Prices	
__get:category__	Read Categories	
__post:category__	Create new Categories	
__post:sales__	Post Prebooking and Orders	
__get:sales__	Get Sales activities

__SPSMS-Manager:__
Manager access

__get:area__	Read are and fixed prices	
__post:area__	Create new areas and fixed Prices	
__get:category__	Read Categories	
__post:category__	Create new Categories	
__post:sales__	Post Prebooking and Orders	
__get:sales__	Get Sales activities

__SPSMS-Sales:__
Sales access for Sales rep

__get:area__	Read are and fixed prices	
__get:category__	Read Categories	
__get:sales__	Get Sales activities
__post:sales__	Post Prebooking and Orders

## Endpoints
### User/Customer Management
#### POST /users
__Description:__ 
EP can be used to create new Users (e.g. internal User + Customers) in the Database.

__Request Arguments:__ 
None

__Required Header Arguments:__
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: post:user

__Sample Body:__ 
```json
{
	"firstname": "Jack",
	"lastname": "Bauer",
	"email": "info@webcoffee.io",
	"company": "webcoffee.io GmbH",
	"address": "Christinenweg 25",
	"postalcode": "59069",
	"postalplace": "Hamm",
	"country": "Germany"
}
```
__Additional Information:__ 
None

__Sample Response:__ 
tbd

#### GET /users
__Description:__ 
EP to get all users in the Database

__Request Arguments:__ 
None

__Required Header Arguments:__ 
tbAuthorization argument needed for header with Bearer Token.
Auth0 Permission needed: get:user

__Sample Body:__ 
None

__Additional Information:__ 
None

__Sample Response:__ 
```json
{
    "success": true,
    "user": [
        {
            "email": "joern@webcoffee.io",
            "firstname": "Joern",
            "id": 6,
            "lastname": "Bergmeier"
        }
    ]
}
```

#### GET /users/<int:id>
__Description:__ 
EP get specified user

__Request Arguments:__ 
<int:id> - ID of user

__Required Header Arguments:__ 
tbAuthorization argument needed for header with Bearer Token.
Auth0 Permission needed: get:user

__Sample Body:__ 
None

__Additional Information:__ 
None

__Sample Response:__ 
```json
{
  "success": true,
  "user": [
    {
      "email": "phil@webcoffee.io",
      "firstname": "Phil",
      "id": 1,
      "lastname": "Mustermann"
    }
  ]
}
```

#### PATCH /users/<int:id>
__Description:__ 
EP to get update a specific user/customer in the Database

__Request Arguments:__ 
<int:id> - UserID

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: post:user

__Sample Body:__ 
All fields from POST call can be used. No field is mandatory. Only given fields will be changed.
```json
{
	"company": "webcoffee.io GmbH"
}
```

__Additional Information:__ 
None

__Sample Response:__ 
Long user details will be shown incl. made changes.
```json
{
  "success": true,
  "user": {
    "address": "Christinenweg 25",
    "company": "webcoffee.io GmbH",
    "country": "Germany",
    "email": "joern@webcoffee.io",
    "firstname": "Nicy",
    "id": 1,
    "lastname": "Web",
    "postalcode": "59069",
    "postalplace": "Hamm"
  }
}
```

#### DELETE /users/<int:id>
__Description:__ 
EP to delete a specific user/customer in the Database

__Request Arguments:__ 
<int:id> - UserID

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: post:user

__Sample Body:__ 
None

__Additional Information:__ 
None

__Sample Response:__ 
Long user details of deleted users will be shown in response incl. success message.
```json
{
  "deleted User": {
    "address": "Christinenweg 25",
    "company": "webcoffee.io GmbH",
    "country": "Germany",
    "email": "jack@webcoffee.io",
    "firstname": "Cool",
    "id": 6,
    "lastname": "Coffee",
    "postalcode": "59069",
    "postalplace": "Hamm"
  },
  "success": true
}
```

### Categories
#### GET /categories
__Description:__ 
EP to show all created categories

__Request Arguments:__ 
None

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: get:category

__Sample Body:__ 
None

__Additional Information:__ 
None

__Sample Response:__ 
Short Array response of all existing categories
```json
{
  "categories": [
    {
      "code": "TDIFF",
      "id": 1,
      "name": "Different"
    },
    {
      "code": "TFRONT",
      "id": 2,
      "name": "Single Front Page"
    },
    {
      "code": "TLOCAL",
      "id": 3,
      "name": "Local Page"
    }
  ],
  "success": true
}
```

#### GET /categories/<int:id>
__Description:__ 
EP to show specific category by ID

__Request Arguments:__ 
<int:id> - Id of category

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: get:category

__Sample Body:__ 
None

__Additional Information:__ 
None

__Sample Response:__ 
Long show response of spcified category
```json
{
  "categories": {
    "code": "TC04201",
    "column_max": 7,
    "column_min": 1,
    "id": 1,
    "mm_max": 370,
    "mm_min": 5,
    "name": "Web Ind Category",
    "notes": "This is the first Category hihi"
  },
  "success": true
}
```

#### POST /categories
__Description:__ 
EP to create new category

__Request Arguments:__ 
None

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: post:category

__Sample Body:__ 
Define a new category.
Mandatory Fields:

__mm_min:__ minimum millimeter for this category (INT)
__mm_max:__ maximum millimiter for this category (INT)
__column_min:__ minimum columns for this category (INT)
__column_max:__ maximum columns for this category (INT)
__name:__ Name of category (String)
__code:__ unique code of category (checked during insertation) (String)
 
```json
{
	"name": "NEW Category",
	"code": "NE3",
	"mm_min": 5,
	"mm_max": 370,
	"column_min": 1,
	"column_max": 7,
	"notes": "Category Text"
}
```

__Additional Information:__ 
None

__Sample Response:__ 
Short Array response of the created category

```json
{
  "category": {
    "code": "NE23",
    "id": 4,
    "name": "NEW Category"
  },
  "success": true
}
```


#### PATCH /categories/<int:id>
__Description:__ 
EP change existing category

__Request Arguments:__ 
<int:id> - category id

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: post:category

__Sample Body:__ 
Define a new category.
Possible field for change: see POST

```json
{
	"name": "NEW Category",

}
```

__Additional Information:__ 
None

__Sample Response:__ 
Long response of the changed category incl. the made changes

```json
{
  "Category": {
    "code": "PATCH",
    "column_max": 7,
    "column_min": 1,
    "id": 4,
    "mm_max": 2,
    "mm_min": 5,
    "name": "Test ",
    "notes": "This is the patched Category"
  },
  "success": true
}

```


#### DELETE /categories/<int:id>
__Description:__ 
EP delete existing category

__Request Arguments:__ 
<int:id> - category id

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: post:category

__Sample Body:__ 
None

__Additional Information:__ 
Delete is only possible if dependencies have been removed before from endpoint /category_area. Otherwise the request will fail with 422.

__Sample Response:__ 
Short response of the deleted category. 

```json
{
  "deleted Category": {
    "code": "NE23",
    "id": 5,
    "name": "NEW Category"
  },
  "success": true
}

```


### Areas
#### GET /areas
__Description:__ 
EP to show all created areas

__Request Arguments:__ 
None

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: get:area

__Sample Body:__ 
None

__Additional Information:__ 
None

__Sample Response:__ 
Short Array response of all existing areas
```json
{
  "areas": [
    {
      "id": 1,
      "name": "Test Area"
    },
    {
      "id": 2,
      "name": "Soester Anzeiger"
    },
    {
      "id": 3,
      "name": "Web"
    }
  ],
  "success": true
}
```

#### GET /areas/<int:id>
__Description:__ 
EP to show spcific area

__Request Arguments:__ 
<int:id> - ID of area

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: get:area

__Sample Body:__ 
None

__Additional Information:__ 
None

__Sample Response:__ 
long show specified area
```json
{
  "area": {
    "code": "New",
    "dp_mm_price": 5.0,
    "dp_mm_price_text": 2.5,
    "gp_mm_price": 7.0,
    "gp_mm_price_text": 4.0,
    "id": 1,
    "name": "PROD Area"
  },
  "success": true
}
```

#### GET /areas/<int:id>/categories
__Description:__ 
EP categories of a spcified area

__Request Arguments:__ 
<int:id> - ID of area

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: get:area

__Sample Body:__ 
None

__Additional Information:__ 
None

__Sample Response:__ 
long all categories which are available for a specified area
```json
{
  "categories": [
    {
      "code": "TC04201",
      "id": 1,
      "name": "Web Category"
    },
    {
      "code": "New2",
      "id": 2,
      "name": "Main Page "
    }
  ],
  "success": true
}
```

#### GET /areas/<int:area_id>/categories/<int:Category_id>
__Description:__ 
EP shows a specific category of a specific area

__Request Arguments:__ 
<int:id_area> - ID of area
<int:id_category> - ID of category

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: get:area

__Sample Body:__ 
None

__Additional Information:__ 
None

__Sample Response:__ 
Show long details of a spcific area and a specific category. Use categoryAreaDetails --> ID for prebookings
```json
{
  "area": {
    "id": 2,
    "name": "Soester Pfohltier"
  },
  "category": {
    "code": "TC04201",
    "column_max": 7,
    "column_min": 1,
    "id": 1,
    "mm_max": 370,
    "mm_min": 5,
    "name": "Web Ind Category",
    "notes": "This is the first Category hihi"
  },
  "categoryAreaDetails": {
    "activated": true,
    "id": 1,
    "id_area": 1,
    "id_category": 1,
    "valid_from": "Sun, 24 May 2020 13:46:07 GMT",
    "valid_to": "Fri, 24 May 2120 13:27:05 GMT"
  },
  "success": true
}
```

#### POST /areas/<int:area_id>/categories/<int:Category_id>
__Description:__ 
EP adds a specific category to a area

__Request Arguments:__ 
<int:id_area> - ID of area
<int:id_category> - ID of category

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: post:area

__Sample Body:__ 
Optional:
__valid_from:__ Datetime of the activation date (Datetime), default = Now
__valid_to:__ Datetime of the deactivation date (Datetime), default = '2120-05-24 13:27:05.332153'

```json
{
	"valid_from": "2020-05-24 13:27:05.332153",
	"valid_to": "2120-05-24 13:27:05.332153"
}
```

__Additional Information:__ 
None

__Sample Response:__ 
Show details of added Area/Category entry
```json
{
  "category_area": {
    "activated": true,
    "id": 10,
    "id_area": 2,
    "id_category": 2,
    "valid_from": "Fri, 24 May 2120 13:27:05 GMT",
    "valid_to": "Sun, 24 May 2020 13:27:05 GMT"
  },
  "success": true
}
```

#### POST /areas
__Description:__ 
EP to create new area

__Request Arguments:__ 
None

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: post:area

__Sample Body:__ 
Define a new area.
Mandatory Fields:

__gp_mm_price:__ millimeter regular price (float)
__gp_mm_price_text:__ millimeter regular price for text (float))
__dp_mm_price:__ millimeter local price (float)
__dp_mm_price_text:__ millimeter local price for text (float)
__name:__ Name of area (String)
__code:__ unique code of area (checked during insertation) (String)
 
```json

{
	"name": "Sample Area",
	"code": "Area51",
	"gp_mm_price" : 7.00,
	"gp_mm_price_text": 4.00,
	"dp_mm_price": 5.00,
	"dp_mm_price_text": 2.50
}

```

__Additional Information:__ 
None

__Sample Response:__ 
Short Array response of the created category

```json
{
  "area": {
    "id": 4,
    "name": "Sample Area"
  },
  "success": true
}
```

#### PATCH /areas/<int:id>
__Description:__ 
EP change existing area

__Request Arguments:__ 
<int:id> - area id

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: post:area

__Sample Body:__ 
Change existing area.
Possible field for change: see POST

```json
{
	"name": "Changed area",

}
```

__Additional Information:__ 
None

__Sample Response:__ 
Long response of the changed area incl. the made changes

```json
{
  "Area": {
    "code": "New",
    "dp_mm_price": 5.0,
    "dp_mm_price_text": 2.5,
    "gp_mm_price": 7.0,
    "gp_mm_price_text": 4.0,
    "id": 1,
    "name": "Changed Area"
  },
  "success": true
}

```


#### DELETE /areas/<int:id>
__Description:__ 
EP delete existing area

__Request Arguments:__ 
<int:id> - area id

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: post:area

__Sample Body:__ 
None

__Additional Information:__ 
Delete is only possible if dependencies have been removed before from endpoint /category_area. Otherwise the request will fail with 422.

__Sample Response:__ 
Short response of the deleted area. 

```json
{
  "deleted area": {
    "id": 5,
    "name": "Changed Area"
  },
  "success": true
}
```

### Prebookings
#### GET /prebookings
__Description:__ 
EP to show all prebookings

__Request Arguments:__ 
None

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: get:sales

__Sample Body:__ 
None

__Additional Information:__ 
None

__Sample Response:__ 
Show all prebookings incl. related categories and areas details
```json
{
  "prebookings": [
    {
      "area": [
        {
          "id": 1,
          "name": "PROD Area from Pfohltier"
        }
      ],
      "bookingDate": "Mon, 25 May 2020 21:26:52 GMT",
      "category": [
        {
          "code": "TC04201",
          "id": 1,
          "name": "Web Ind Category"
        }
      ],
      "company": "webcoffee.io GmbH",
      "email": "joern@webcoffee.io",
      "firstname": "Nicy",
      "id": 7,
      "lastname": "Web"
    },
    {
      "area": [
        {
          "id": 1,
          "name": "PROD Area from Pfohltier"
        }
      ],
      "bookingDate": "Mon, 25 May 2020 21:26:52 GMT",
      "category": [
        {
          "code": "la3r3r3rla",
          "id": 2,
          "name": "Test "
        }
      ],
      "company": "webcoffee.io GmbH",
      "email": "joern@webcoffee.io",
      "firstname": "Nicy",
      "id": 8,
      "lastname": "Web"
    },
    {
      "area": [
        {
          "id": 1,
          "name": "PROD Area from Pfohltier"
        }
      ],
      "bookingDate": "Mon, 25 May 2020 21:26:52 GMT",
      "category": [
        {
          "code": "la3r3r3rla",
          "id": 2,
          "name": "Test "
        }
      ],
      "company": "webcoffee.io GmbH",
      "email": "klausi@webcoffee.io",
      "firstname": "Hans",
      "id": 9,
      "lastname": "Klaus"
    }
  ],
  "success": true
}
```

#### GET /prebookings/<int:id>
__Description:__ 
EP to show specific prebooking by ID

__Request Arguments:__ 
<int:id> - Id of prebooking

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: get:sales

__Sample Body:__ 
None

__Additional Information:__ 
None

__Sample Response:__ 
Long show response of specified prebooking
```json

  "prebookings": [
    {
      "area": [
        {
          "code": "New",
          "dp_mm_price": 5.0,
          "dp_mm_price_text": 2.5,
          "gp_mm_price": 7.0,
          "gp_mm_price_text": 4.0,
          "id": 1,
          "name": "PROD Area"
        }
      ],
      "bookingDate": "Sun, 24 May 2020 14:44:16 GMT",
      "category": [
        {
          "code": "TC04201",
          "column_max": 7,
          "column_min": 1,
          "id": 1,
          "mm_max": 370,
          "mm_min": 5,
          "name": "Web Ind Category",
          "notes": "This is the first Category"
        }
      ],
      "company": "webcoffee.io GmbH",
      "email": "joern@webcoffee.io",
      "firstname": "Nicy",
      "id": 1,
      "lastname": "Web"
    }
  ],
  "success": true
}
```

#### POST /prebooking
__Description:__ 
EP to create new prebooking

__Request Arguments:__ 
None

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: post:sales

__Sample Body:__ 
Define a new prebooking.
id_user defines the "customer" from users table. Id_area_category is from endpoint area/<int:id>/categories/id --> id

```json
{
	"id_user": 1,
	"id_area_category": 1
}
```

__Additional Information:__ 
user and area_category (see info above) has to be defined before.

__Sample Response:__ 
Short Array response of the created prebooking

```json
{
  "prebooking": {
    "ad_date": "Mon, 25 May 2020 21:17:57 GMT",
    "id": 6,
    "id_area_category": 1,
    "id_customer": 1
  },
  "success": true
}
```

#### DELETE /prebookings/<int:id>
__Description:__ 
EP delete existing prebooking

__Request Arguments:__ 
<int:id> - prebooking id

__Required Header Arguments:__ 
Authorization argument needed for header with Bearer Token.
Auth0 Permission needed: post:sales

__Sample Body:__ 
None

__Additional Information:__ 
None
__Sample Response:__ 
Short response of the deleted category. 

```json
{
  "deleted_prebooking": {
    "ad_date": "Sun, 24 May 2020 14:48:13 GMT",
    "id": 4,
    "id_area_category": 3,
    "id_customer": 5
  },
  "success": true
}

```

## Unit Test Setup
To test the Endpoints with test_app.py you need to meet the following requirements.
- Import ENV from setup.sh file (on MAC type: source ./setup.sh)
- Import an install all requirements from requirements.txt
- Get Bearer token for ADMIN and SALES and change it in the head of the test_app.py file to check rights properly. Login credentials you can get from README (see above)

Start Testing with python test_app.py - All Test should be passed

