from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # List of video file names
    videos = ["balcony.mp4", "bite.mp4", "Burette.mp4"]
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    # Set host to '0.0.0.0' and use the PORT environment variable if available
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)