# azure-json-validator
# **Azure JSON Validator – Azure Function App**

## **📌 Overview**
This project is a simple and lightweight **Azure Function App** that validates incoming JSON data.  
It checks whether the required fields are present and whether the values follow basic data quality rules.  
The project demonstrates how to build and deploy serverless APIs using **Python + Azure Functions**.

---

## **✨ Features**
- Validates JSON input sent via HTTP POST  
- Checks required fields: `name`, `age`, `email`  
- Ensures:
  - `age` is a number and greater than 0  
  - `email` contains `@`  
- Returns validation report:
  ```json
  {
    "isValid": true/false,
    "errors": []
  }
