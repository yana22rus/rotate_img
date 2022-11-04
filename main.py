import os
from getpass import getuser
from uuid import uuid4

from PIL import Image
from flask import Flask, render_template, request, redirect

from db.db import *

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join("img")

app.secret_key = "426a0a76-5477-41bd-a225-7f0d4b835f1a"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////home/{getuser()}/main.sqlite'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1042 * 1042


@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]

        filename = f'{uuid4()}.{file.filename.split(".")[-1].lower()}'

        file.filename = filename

        file.save(os.path.join("static", UPLOAD_FOLDER, file.filename))

        cursor.execute("""INSERT INTO Img (name_file) VALUES (?)""", (filename,))

        connection.commit()

        cursor.execute(f"""SELECT id FROM img WHERE name_file='{filename}'""")

        data_id = cursor.fetchone()[0]

        return redirect(f"/rotate/{data_id}")

    return render_template("upload.htm")


@app.route("/rotate/<int:id>", methods=["GET", "POST"])
def rotate(id):
    cursor.execute(f"""SELECT name_file FROM img WHERE id='{id}'""")

    name_file = cursor.fetchone()[0]

    if request.method == "POST":
        if request.form["btn"] == "Влево":
            img = Image.open(os.path.join("static", "img", name_file))

            rotated = img.rotate(90)

            rotated.save(os.path.join("static", "img", name_file))

        if request.form["btn"] == "Вправо":
            img = Image.open(os.path.join("static", "img", name_file))

            rotated = img.rotate(-90)

            rotated.save(os.path.join("static", "img", name_file))

    return render_template("rotate.htm", img=name_file)


if __name__ == "__main__":
    app.run(debug=True)
