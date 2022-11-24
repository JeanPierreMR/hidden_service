from stem.control import Controller
from flask import Flask, render_template, request

#setting up the webpage service
app = Flask("security_page")
port = 5000
host = "127.0.0.1"
hidden_svc_dir = "c:/temp/"

#here you can add routes
@app.route('/', methods =['GET'])
def index():
    return render_template('index.html')


    
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