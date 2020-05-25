# SPSMS
Special Publication Sales Management System offeres the possibility to sell ads in special publications of a newspaper

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

#### PATCH /users/id
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

#### DELETE /users/id
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
  "deleted User id": {
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


#### PATCH /categories/id
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


#### DELETE /categories/id
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

#### PATCH /areas/id
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


#### DELETE /areas/id
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
  "deleted are": {
    "id": 5,
    "name": "Changed Area"
  },
  "success": true
}
```

