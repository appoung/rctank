from flask import Flask, jsonify, render_template, request,Response#플라스크 관련
from camera import Camera
app = Flask(__name__)
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
   return Response(gen(Camera()),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def home():
	return render_template('index.html')
@app.route('/foward', methods=['GET'])
def foward():
	print("foward!")
	return Response(status=200)
@app.route('/backward')
def backward():
	print("backward!")
	return Response(status=200)
@app.route('/right')
def right():
	print("right")
	return Response(status=200)
@app.route('/left')
def left():
	print("left")
	return Response(status=200)
@app.route('/stop')
def stop():
	print("stop")
	return Response(status=200)
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)	#localhost:5000으로 서버접속

