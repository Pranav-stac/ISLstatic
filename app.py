from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # List of video file names
    videos = ["balcony.mp4", "bite.mp4", "Burette.mp4"]
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    # Set host to '0.0.0.0' to make the server accessible externally and specify the port
    app.run(host='0.0.0.0', port=5000, debug=True)
