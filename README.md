
![Logo](https://raw.githubusercontent.com/mvishok/SimpleNotes/main/logo.png)


# SimpleNotes

SimpleNotes is a web application that allows users to create, view, and delete notes. It provides a user-friendly interface for managing personal notes, making it easy to jot down ideas, thoughts, and reminders. With session-based authentication, users can securely access their notes and perform actions specific to their account. SimpleNotes is built using Flask, PostgreSQL for data storage, and incorporates HTML and CSS for the frontend design. It offers a simple yet effective solution for organizing and managing personal notes online.


## Screenshot

![App Screenshot](https://i.ibb.co/yYFf9hL/image.png)


## Run Locally

To run the SimpleNotes project locally, please follow these steps:

1. Clone the project repository from GitHub:

```bash
git clone https://github.com/mvishok/SimpleNotes.git
```

2. Navigate to the project directory:

```bash
cd SimpleNotes
```

3. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Set up the PostgreSQL database:

 - Install PostgreSQL on your local machine if you haven't already.
 - Create a new database.
 - Update the database connection details in the app.py file:

```python
  DATABASE_URL = 'postgres://your_username:your_password@your_host:your_port/your_database'

```

6. Run the application:

```bash
python app.py
```

7. Access the application in your web browser at `http://localhost:3000`.

Now you can locally access and interact with the SimpleNotes web application. Feel free to create, view, update, and delete notes as needed.
## Acknowledgements

 - [Flask](https://flask.palletsprojects.com/)
 - [Jinja2](https://palletsprojects.com/p/jinja/)
 - [PostgreSQL](https://www.postgresql.org/)

## Author

👤 **Vishok M**

* Website: https://vishok.tech/
* Twitter: [@vishokmanikantan](https://twitter.com/vishokmanikantan)
* Github: [@mvishok](https://github.com/mvishok)
* LinkedIn: [@vishokmanikantan](https://linkedin.com/in/vishokmanikantan)

## Support

For support, please use [Github Issues](https://github.com/mvishok/SimpleDownloader/issues)

