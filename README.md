# SQL Autotest Project.

This project is designed to automate the testing of a simple SQLite database. The Python script `sql_autotest.py` creates a database, populates it with test user data, and then verifies the data using SQL queries. The script uses the `unittest` library to ensure that the database contains the expected information

## Prerequisites

To run this project, you will need the following installed on your system:

- Python 3.x
- SQLite (included with Python)
- Virtual environment tools (`venv`)

## Project Structure

- **`sql_autotest.py`**: The main script for creating the SQLite database, inserting test data, and running the tests.
- **`venv/`**: The virtual environment directory (created after setup).

## Setup Instructions

1. **Clone the Repository**

   Clone the repository to your local machine:
   ```
   git clone https://github.com/yourusername/sql_autotest_project.git
   cd sql_autotest_project
   ```

2. **Create a Virtual Environment**

   Create a virtual environment to manage dependencies:
   ```
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Linux/macOS:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

4. **Install Dependencies**

   Install the required dependencies (in this case, `unittest` is part of the standard library, so no additional installations are needed).

5. **Run the Script**

   After activating the virtual environment, run the script to create the database, insert test data, and verify it:
   ```
   python sql_autotest.py
   ```

## How the Script Works

- The script creates an SQLite database named `test_database.db` and a table named `users`.
- It inserts 20 test users into the `users` table.
- It uses the `unittest` framework to verify that the first three records in the database match the expected data.
- All records in the `users` table are printed for verification.

## Connecting to a Server with Visual Studio Code

If you need to deploy this project to a remote server, follow these steps:

1. **Install the Remote - SSH Extension**

   Install the **Remote - SSH** extension in Visual Studio Code.

2. **Add SSH Host**

   - Click on the Remote Explorer icon on the sidebar.
   - Click on the "+" button to add a new SSH host.
   - Use the following command to connect to your server:
     ```
     ssh user@your_server_ip
     ```

3. **Connect and Edit Files**

   After connecting, you can edit files directly on the server using Visual Studio Code.

4. **Deploy the Project**

   Copy the project files to the server using SCP or by directly dragging and dropping in Visual Studio Code:
   ```
   scp -r ./sql_autotest_project user@your_server_ip:/home/user/sql_project
   ```

## Running the Project on the Server

1. **SSH into Your Server**

   Connect to your server via SSH:
   ```
   ssh user@your_server_ip
   ```

2. **Navigate to the Project Directory**

   Go to the directory where the project is located:
   ```
   cd /home/user/sql_project
   ```

3. **Create a Virtual Environment on the Server**

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Run the Script on the Server**

   Execute the script to run the tests:
   ```
   python sql_autotest.py
   ```

## Expected Output

- The script should output all the records from the database.
- It will also show the test results, indicating that the first three records match the expected data.

## Cleaning Up

To remove the database file after running the tests, use the following command:
```
rm test_database.db
```

## Contributing

Feel free to submit issues or pull requests if you find any problems or have suggestions for improvement.

## License

This project is open source and available under the [MIT License](LICENSE).

