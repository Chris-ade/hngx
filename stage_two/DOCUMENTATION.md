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
- **URL:** /api/<<int:user_id>>
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
