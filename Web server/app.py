from flask import Flask, render_template
#import requests

room = {
            'lamp': 'off',
            'coolFan': 'off',
            'studyLamp' : 'off',
            'bulb' : 'off'
        }

ip = {
            'room' : 'http://192.168.137.244',
            'kitchen' : 'http://192.168.137.245',
            'hall' : 'http://192.168.137.243'
    }

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html',data = room)

@app.route('/')
def starting():
    return render_template('index.html',data = room)

@app.route("/<location>%<device>%<action>")
def action(location,device,action):
    #requests.get('http://192.168.137.244/LED=ON')
    device = str(device)
    location = str(location)
    action = str(action)
    url = ip[location] + '/' + device + '/' + action
    #requests.get(url)
    room[device] = action
    return render_template('index.html',data = room)


##@app.route('/ledoff/led/')
##def blinkoff():
##    #requests.get('http://192.168.137.244/LED=OFF')
##    room['lamp'] = 'off'
##    return render_template('index.html',data = room)
##



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
