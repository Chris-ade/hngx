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
- **Response Format:**
  ```json
  {
  "message": "Person created successfully",
  "id": 2
  }
- **Status Codes:**
- **201:** Person created successfully
- **400:** Bad Request (in case of errors)
