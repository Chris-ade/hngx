# REST API Documentation

This documentation provides information on how to use the REST API for managing persons.

## Base URL
The base URL for all API endpoints is `https://hackinubee.pythonanywhere.com/api`

## Endpoints

### 1. Create a Person (POST)
- Create a new person with the specified details.
- **URL:** `/api`
- **Method:** POST
- **Request Format:**
  ```json
  {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@hngx.com",
    "gender": "male"
  }
  ```
- **Response Format:**
  ```json
  {
  "message": "Person created successfully",
  "id": 2
  }
  ```
- **Status Codes:**
- **201:** Person created successfully
- **400:** Bad Request (in case of errors)

### 2. Get a Person by ID (GET)
- Retrieve details of a person by specifying their ID.
- **URL:** `/api/<int:user_id>`
- **Method:** GET
- **Response Format:**
``` json
  {
  "person": {
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@hngx.com",
    "gender": "male"
  }
}
```
- **Status Codes:**
- **200:** OK (Person found)
- **404:** Not Found (Person not found or does not exist)
- **400:** Bad Request (in case of errors)

### 3. Update a Person by ID (PUT)
- Modify details of an existing person by specifying their ID.
- **URL:** `/api/<int:user_id>`
- **Method:** PUT
- **Request Format:**
``` json
{
  "age": 21
}
```
- **Response Format:**
``` json
{
  "message": "Person updated successfully"
}
```
- **Status Codes:**
- **200:** OK (Person updated successfully)
- **404:** Not Found (Person not found or does not exist)
- **400:** Bad Request (in case of errors)

### 4. Delete a Person by ID (DELETE)
- Remove a person from the database by specifying their ID.
- **URL:** `/api/<int:user_id>`
- **Method:** DELETE
- **Response Format:**
``` json
{
  "message": "Person deleted successfully"
}
```
- **Status Codes:**
- **200:** OK (Person deleted successfully)
- **404:** Not Found (Person not found or does not exist)
- **400:** Bad Request (in case of errors)

**Sample Usage**
- Create a Person
``` bash
curl -X POST -H "Content-Type: application/json" -d '{
  "name": "John Doe",
  "age": 30,
  "email": "johndoe@hngx.com",
  "gender": "male"
}' https://hackinubee.pythonanywhere.com/api
```
**Get a Person by ID**
``` bash
curl https://hackinubee.pythonanywhere.com/api/2
```
**Update a Person by ID**
``` bash
curl -X PUT -H "Content-Type: application/json" -d '{
  "age": 21
}' https://hackinubee.pythonanywhere.com/api/2
```
**Delete a Person by ID**
``` bash
curl -X DELETE https://hackinubee.pythonanywhere.com/api/2
```
