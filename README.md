# SPSMS
Special Publication Sales Management System offeres the possibility to sell ads in special publications of a newspaper

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