from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # List of video file names
    videos = ["balcony.mp4", "bite.mp4", "Burette.mp4"]
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)