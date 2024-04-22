def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
        }
        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
        }
        .search-container {
            text-align: center;
            margin: 20px auto;
        }
        .search-form {
            display: inline-block;
            padding: 20px;
            border-radius: 10px;
            background-color: #ddd;
        }
        .search-form input[type="text"] {
            padding: 10px;
        }
        .search-form button {
            padding: 5px 10px;
            background-color: #333;
            color: #fff;
            border: none;
            cursor: pointer;
        }
        .item {
            display: flex;
            align-items: center;
            padding: 10px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .thumbnail {
            width: 200px;
            height: auto;
            margin-right: 10px;
            border-radius: 5px;
        }
        .data {
            flex: 1;
        }
        .data h3 {
            margin-top: 0;
        }
        .data p {
            margin: 5px 0;
        }
        .data a {
            display: block;
            margin-top: 10px;
            text-decoration: none;
            color: #333;
            font-weight: bold;
        }
    </style>
</head>
<body>

<header>
    <h1>My Website</h1>
</header>

<div class="search-container">
    <form class="search-form">
        <input type="text" name="query" placeholder="Search...">
        <button type="button">Search</button>
    </form>
</div>

<div class="items">
    <!-- Sample Item -->
    <div class="item">
                <img src="https://i.ytimg.com/vi/-4JV4hur1PM/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBZowGWFFb399CHtSHm3PopKR9LQA" alt="Item 2 Image" class="thumbnail">
                <div class="data">
                    <h3>Tera Hua Video Song With Lyrics | Atif Aslam | Loveyatri | Aayush Sharma | Warina Hussain |Tanishk B</h3>
                    <p>5 years ago</p>
                    <p>146,671,148 views</p>
                    <p>3:52</p>
                    <a href="#" onclick="sendData({'videoId': '-4JV4hur1PM', 'thumbnail': 'https://i.ytimg.com/vi/-4JV4hur1PM/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBZowGWFFb399CHtSHm3PopKR9LQA', 'title': 'Tera Hua Video Song With Lyrics | Atif Aslam | Loveyatri | Aayush Sharma | Warina Hussain |Tanishk B', 'publishedTimeText': '5 years ago', 'views': '146,671,148 views', 'Length': '3:52'})">Details</a>
                </div>
            </div>
</div>

<script>
function sendData(data) {
    const url = 'Listen';
    const query = `?videoId=${encodeURIComponent(data.videoId)}&thumbnail=${encodeURIComponent(data.thumbnail)}&title=${encodeURIComponent(data.title)}&publishedTimeText=${encodeURIComponent(data.publishedTimeText)}&views=${encodeURIComponent(data.views)}&Length=${encodeURIComponent(data.Length)}`;
    window.location.href = url + query;
}
</script>

</body>
</html>
"""

def listen():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beautiful Audio Player</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .audio-player {
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 300px;
            text-align: center;
        }
        .thumbnail {
            width: 100%;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        audio {
            width: 100%;
            outline: none;
            margin-bottom: 20px;
        }
        .controls {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .control-button {
            background-color: #007bff;
            border: none;
            color: #fff;
            padding: 10px 20px;
            border-radius: 5px;
            margin: 0 10px;
            cursor: pointer;
        }
        .control-button:hover {
            background-color: #0056b3;
        }
        .volume {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 10px;
        }
        .volume input[type="range"] {
            width: 100px;
            margin: 0 10px;
        }
        .title {
            font-weight: bold;
            margin-bottom: 10px;
        }
        .view-count {
            color: #666;
            font-size: 0.8em;
        }
    </style>
</head> 
<body>
    <div class="audio-player">
        <img class="thumbnail" src="" alt="Thumbnail">
        <h2 class="title"></h2>
        <span class="view-count"></span>
        <audio controls>
            <source src="" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        <div class="controls">
            <button class="control-button" onclick="togglePlayPause()">Play/Pause</button>
            <button class="control-button" onclick="skip(-10)">-10s</button>
            <button class="control-button" onclick="skip(10)">+10s</button>
        </div>
        <div class="volume">
            <label for="volume">Volume:</label>
            <input type="range" id="volume" name="volume" min="0" max="1" step="0.1" value="1" oninput="changeVolume(this.value)">
        </div>
    </div>

    <script>
        window.onload = function() {
            const urlParams = new URLSearchParams(window.location.search);
            const videoId = urlParams.get('videoId');
            const thumbnail = urlParams.get('thumbnail');
            const title = urlParams.get('title');
            const views = urlParams.get('views');
            const publishedTimeText = urlParams.get('publishedTimeText');
            const length = urlParams.get('Length');

            // Set the audio player details
            document.querySelector('.thumbnail').src = thumbnail;
            document.querySelector('.title').textContent = title;
            document.querySelector('.view-count').textContent = `${views} views`;
            
            // Example for setting the audio source, change as necessary
            document.querySelector('audio source').src = `https://example.com/audio/${videoId}.mp3`;
            document.querySelector('audio').load();
        };

        function togglePlayPause() {
            const audio = document.querySelector('audio');
            if (audio.paused) {
                audio.play();
            } else {
                audio.pause();
            }
        }

        function skip(time) {
            const audio = document.querySelector('audio');
            audio.currentTime += time;
        }

        function changeVolume(volume) {
            const audio = document.querySelector('audio');
            audio.volume = volume;
        }
    </script>
</body>
</html>

"""
from flask import Flask, render_template, request,jsonify,redirect, redirect, url_for, session
app = Flask(__name__)

# Define a route for handling the search request
@app.route('/', methods=['GET', 'POST'])
def search():
    return index()
    
@app.route('/Listen', methods=['GET', 'POST'])
def search2():
    video_id = request.args.get('videoId', 'DefaultVideoId')
    thumbnail = request.args.get('thumbnail', 'DefaultThumbnail')
    return video_id + ":" + thumbnail


if __name__ == "__main__":
    app.run(debug=True)
