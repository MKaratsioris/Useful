# Flask API using SQlite

## Endpoints:
| Method |          Route        |           Description          |
|:------:|:---------------------:|:------------------------------:|
|  GET   | /employees            |  List all employees            |
|  POST  | /employee             |  Add a new employee            |
|  GET   | /employee/<last_name> |  Get employee(s) by last name  |
|  PUT   | /employee/update      |  Update salary                 |
| DELETE | /employee/delete      |  Delete an employee            |

## Details
- One connection per request ✅
- Closed cleanly at the end ✅
- File-based DB for persistence ✅