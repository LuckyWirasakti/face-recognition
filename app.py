from flask import Flask, render_template, request, json

app = Flask(
    __name__, 
    static_url_path="",
    static_folder="template/media",
    template_folder="template"
)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if True:
            result = "Wajah cocok"
        else:
            result = "Wajah tidak cocok"
            
        response = app.response_class(
            response=json.dumps({
                'status': result
            }),
            mimetype='application/json'
        )
        return response
         
if __name__ == "__main__":
    app.run()