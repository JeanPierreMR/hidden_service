from stem.control import Controller
from flask import Flask, render_template, request, send_file
import os
import shutil

#setting up the webpage service
app = Flask("security_page")
port = 5000
host = "127.0.0.1"
hidden_svc_dir = "c:/temp/"


def makeTemplate(title,text):
    with open("templates/template.html", "r") as f:
        contents = f.readlines()

    for i in range(len(contents)):
        if "[[title]]" in contents[i]:
            contents[i] = contents[i].replace("[[title]]",title)
        if "[[text]]" in contents[i]:
            contents[i] = contents[i].replace("[[text]]",text)

    with open('hidden_service_custom/templates/index.html', 'w') as fp:
        for item in contents:
            fp.write("%s\n" % item)



#here you can add routes
@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method=='POST':
        title = str(request.form['title'])
        text = str(request.form['text'])
        makeTemplate(title, text)

        path = './hidden_service_custom'
        path1 = "./" + 'your_hidden_service' + ".zip"
        # if os.path.exists(path):
        #     shutil.rmtree(path, ignore_errors=False, onerror=None)
        #     os.remove(path1)
        # os.mkdir(path)
        # src_path = "./run.py"
        # dst_path = path + "/run.py"
        # shutil.copy(src_path, dst_path)
        # print('Copied')
        # print(path)
        shutil.make_archive('your_hidden_service', 'zip',path)
        return send_file(path1, as_attachment=True)
        # return render_template("index.html")
        

    else:
        return render_template('index.html')


    
# @app.route('/home')
# def home():
#     return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/messages', methods =['GET', 'POST'])
def messages():
    if request.method=='POST':
        message = str(request.form['message'])
        return render_template("messages.html")

    else:
        return render_template('messages.html')
    
if __name__ == "__main__":
    print(" * Getting controller")
    controller = Controller.from_port(address="127.0.0.1", port=9151)
    try:
        controller.authenticate(password="")
        controller.set_options([
            ("HiddenServiceDir", hidden_svc_dir),
            ("HiddenServicePort", "80 %s:%s" % (host, str(port)))
            ])
        svc_name = open(hidden_svc_dir + "/hostname", "r").read().strip()
        print(" * Created host: %s" % svc_name)
    except Exception as e:
        print(e)
    app.run()