# SPSMS
Special Publication Sales Management System offeres the possibility to sell ads in special publications of a newspaper

## Endpoints Backend
### POST /createUser
__Description:__ 
EP can be used to create new Users (e.g. internal User + Customers) in the Database.

__Request Arguments:__ 
None

__Required Header Arguments:__ 
tbd

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

__Sample Result:__ 
tbd

### GET /users
__Description:__ 
EP to get all users in the Database

__Request Arguments:__ 
None

__Required Header Arguments:__ 
tbd

__Sample Body:__ 
None

__Additional Information:__ 
None

__Sample Result:__ 
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