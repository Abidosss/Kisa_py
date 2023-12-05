# import json

# with open(".\json\schema_ccreply.json","r") as f:
#     data = f.read()

# print(type(data))
# js = json.loads(data)
# print(type(js["properties"]["decrypted_text"]["description"]))
# js2 = js["properties"]["decrypted_text"]["description"]
# print(js2)

from flask import Flask, send_file
import os
app = Flask(__name__)

@app.route("/download")
def index():
    filepath = 'D:\_GitStore\School\Kisa_py\json' 
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.debug = True
    app.run()