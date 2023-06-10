from flask import Flask, render_template, request, redirect
import os
import psycopg2
import uuid

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(16)

# Initialize PostgreSQL connection
DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

session_id = None

@app.before_request
def before_request():
    global session_id
    if 'session_id' in request.cookies:
        session_id = request.cookies.get('session_id')
    else:
        session_id = str(uuid.uuid4())
        response = redirect(request.path)
        response.set_cookie('session_id', session_id)
        return response


@app.route('/styles.css')
def styles():
    return app.send_static_file('styles.css')


@app.route('/')
def index():
    global session_id

    if session_id:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes WHERE user_id = %s", (session_id,))
        notes = cursor.fetchall()
    else:
        notes = []
    return render_template('index.html', notes=notes, userId=session_id)


@app.route('/notes', methods=['POST'])
def create_note():
    global session_id

    title = request.form.get('title')
    content = request.form.get('content')
    

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (title, content, user_id) VALUES (%s, %s, %s)",
        (title, content, session_id)
    )
    conn.commit()

    return redirect('/')

@app.route('/notes/<note_id>/delete', methods=['GET'])
def delete_note(note_id):
    global session_id

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE id = %s", (note_id,))
    note = cursor.fetchone()

    if not note:
        return 'Note not found', 404

    if note[3] != session_id:
        return 'Unauthorized access to note', 403

    cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    conn.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
