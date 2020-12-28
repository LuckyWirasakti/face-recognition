from flask import Flask, render_template, request, json
from module import utils
from os import remove
import face_recognition

app = Flask(
    __name__, 
    static_url_path="",
    static_folder="static",
    template_folder="template"
)


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        encoding = []
        local = "template/media/ori.jpg"
        path = utils.b64_img(request.form['image'])        
        for i in [local, path]:
            encoding.append(face_recognition.face_encodings(face_recognition.load_image_file(i))[0])
        remove(path)
        if face_recognition.compare_faces([encoding[0]], encoding[1])[0]:
            result = "Wajah cocok"
        else:
            result = "Wajah tidak cocok"
        return app.response_class(
            response=json.dumps({
                'status': result
            }),
            mimetype='application/json'
        )
if __name__ == "__main__":
    app.run()