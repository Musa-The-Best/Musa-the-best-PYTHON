from flask import Flask

app = Flask(__name__)

@app.route("/")
def resume():
    return """
    <html>
    <head>
        <title>Resume</title>
    </head>
    <body>
        <h1>MR. GOAT</h1>
        <p>Email: GOATED@gmail.com</p>

        <h2>Education</h2>
        <p>Grade 8 Student</p>

        <h2>Skills</h2>
        <ul>
            <li>Python</li>
            <li>HTML</li>
            <li>SQL</li>
        </ul>

        <h2>Experience</h2>
        <p>Created simple projects using Flask.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)