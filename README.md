
# 🚀Project Instructions

### 1. Clone the repo
   
  ```terminal

    https://github.com/Omayski13/python_test

  ```

### 2.Create and Activate a Virtual Environment
**Run the following command to create a virtual environment:**

   ```terminal
   python -m venv venv

   ```
**Activate the virtual environment**
- *For Windows:*
   ```
   venv\Scripts\activate
   ```

- *For macOS (or Linux):*
  ```
   source venv/bin/activate
   ```

### 3. Install dependencies
 
   ```terminal
   
     pip install -r requirements.txt
  
   ```

### 4. Create a .env File
At the root level of the project (where manage.py is located), create a .env file using [this template](https://github.com/Omayski13/python_test/blob/main/interview_test/.env_template) or just copy from below:

  ```py

# Security
SECRET_KEY=

# Database
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

### 5. Run the migrations

  ```terminal

    python manage.py migrate

  ```

### 6. Run the project

  ```terminal

    python manage.py runserver

  ```

### 7. Import data in the tables
Use the files from csv_files directory in the project.
If your using PyCharm you can just drag them to the table name

*** for files sales and product when importing tick these two options:
- ✔️Insert inconvertible values as null
- ✔️Disable indexes and trigger,lock table
