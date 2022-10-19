### SokoFresh API Challenge

> This API mimics user management functionalities to include **creating**, **updating** and **deleting** user profiles and their product portfolios.

# Badges
[![Build Status](https://github.com/Gichia/soko-fresh-challenge/actions/workflows/main.yml/badge.svg)](https://github.com/Gichia/soko-fresh-challenge/actions)


# Summary
The Farmers API allows users to create and manage their accounts on the platform. Add multiple addresses and multiple value chains and also manage them


Getting started
--------------------
1. Clone this repository
```
    https://github.com/Gichia/soko-fresh-challenge.git
```

2. Navigate to the cloned repository

Pre-requisites
----------------------
1. Python3.10
2. Postman
3. Git

Installation
---------------------------------
1. Create a virtual environment
```
    python3.10 -m venv ./venv
```

2. Activate the virtual environment
```
    source venv/bin/activate
```

3. Switch to 'develop' branch on git
```
    git checkout develop
```

5. Install requirements
```
    pip install -r requirements.txt
```

Run the application
---------------------------------
```
    uvicorn app.main:app --port 8000
```

Access the application
---------------------------------

The application docs can be accessed on a browser on the specified port.
```
    http://localhost:8000/docs
```

> When you run the application, you can also test the following endpoints using postman
-----------------------------------------------

# Run on Docker
> The API is also shipped with docker files for easy installation. Requires only the `.env` file and you are good to go.

Pre-requisites
----------------------
1. Docker
2. Docker Compose

Run the application
---------------------------------
```
    docker-compose up
```

Access the application
---------------------------------

The application docs can be accessed on a browser on the specified port.
```
    http://localhost:8001/docs
```

## Test Live Version
> A live version of the API can be accessed at `https://soko-fresh-challenge.herokuapp.com/docs`.

**Unrestricted endpoints**

| Endpoint | Functionality |
----------|---------------
GET / | Show sthe welcome message
POST /auth/register | Register a new user
POST /auth/login | Login a user

**Restricted endpoints**

Endpoint | Functionality
---------|---------------
GET /users | Get all users paginated
GET /users/&lt;user_id&gt; | Get user details
PUT /users | Update the logged in user details
DELETE /users | Delete the user account plus their addresses and value chains
POST /users/address | Add a new address
PUT /users/address/&lt;addr_id&gt; | Update the address details
DELETE /users/address/&lt;addr_id&gt; | Delete an address
POST /value_chains | Add a new value chain
PUT /value_chains/&lt;chain_id&gt; | Update the value chain details
DELETE /value_chains/&lt;chain_id&gt; | Delete a value chain


Authors
-----------------------------
**Peter Gichia** -_Created By_-[Gichia](https:/github.com/Gichia)

License
--------------------------
This project is licensed under the MIT license. See [LICENSE](https://github.com/Gichia/soko-fresh-challenge/blob/develop/LICENCE) for details.

