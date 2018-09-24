from flask import Flask, request
from caesar import rotate_character

app = Flask(__name__)
app.config['DEBUG']= True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label>
                Rotate By:
            </label>
            <input type="text" name="rot" value=0 />
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Rotate" />
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rotation_num = int(request.form['rot'])
    text = request.form['text']
    encrypted = rotate_character(text, rotation_num)
    return form.format(encrypted)

@app.route("/")
def index():
    return form.format("")

app.run()

