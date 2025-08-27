# Department Management System

## Overview
The Department Management System is a web-based application designed to streamline the management of departments and users within an organization. It provides a user-friendly interface for managing department data and user information, along with a robust backend API for handling operations.

## Features
- **Department Management**: Create, update, and delete department records.
- **User Management**: Manage user accounts associated with departments.
- **Responsive Design**: A modern and responsive frontend for seamless user experience.
- **Real-Time Updates**: Real-time functionality for dynamic data handling.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Version Control**: Git

## Project Structure
```
department_management_system/
├── department_api/
│   ├── requirements.txt
│   ├── src/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── main.py
│   │   ├── test_api.py
│   │   ├── test_models.py
│   │   ├── database/
│   │   │   └── app.db
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── department.py
│   │   │   └── user.py
│   │   ├── routes/
│   │   │   ├── department.py
│   │   │   └── user.py
│   │   ├── static/
│   │   │   ├── favicon.ico
│   │   │   └── index.html
├── instance/
└── schema.sql
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/lankyghana/department-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd department-management-system/department_api
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   python src/main.py
   ```

## Usage
- Access the application in your browser at `http://127.0.0.1:5000`.
- Use the provided API endpoints for programmatic access.

## API Endpoints
### Department Endpoints
- `GET /departments`: Retrieve all departments.
- `POST /departments`: Create a new department.
- `PUT /departments/<id>`: Update an existing department.
- `DELETE /departments/<id>`: Delete a department.

### User Endpoints
- `GET /users`: Retrieve all users.
- `POST /users`: Create a new user.
- `PUT /users/<id>`: Update an existing user.
- `DELETE /users/<id>`: Delete a user.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Flask documentation
- GitHub community

---
Feel free to reach out for any questions or suggestions!
