#Library!
import yt_dlp
from flask import Flask, render_template, request
import json
import requests
from bs4 import BeautifulSoup
import re

#Functions!
def yt_url(video_url):
    youtube_url = "https://www.youtube.com/watch?v=" + video_url
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            audio_url = info_dict['url']
            

        return audio_url
    except Exception as e:
        print("Error:", e)
        return "404:" + str(e)

def Scrap_youtube_search(url):
    try :
        # URL of the webpage
        url = url
        # Send a GET request to the URL
        response = requests.get(url)
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find script tags containing the variable ytInitialData
        script_tags = soup.find_all('script', text=re.compile(r'ytInitialData'))
        # Extract the content of ytInitialData variable
        yt_initial_data = None
        for script in script_tags:
            # Search for ytInitialData assignment using regular expression
            match = re.search(r'var ytInitialData = ({.*?});', script.text)
            if match:
                # Extract the content of ytInitialData
                yt_initial_data = match.group(1)
                break
        return json.loads(yt_initial_data)
    except:
        print("Something Cause Error ! Failed Process !")


def yt_search(search_query , typo = 0):
    # Print the extracted ytInitialData
    url = "https://www.youtube.com/results?search_query=" + search_query

    yt_initial_data = Scrap_youtube_search(url)

    html = ""
    json_data = {}
    for index in range(0,len(yt_initial_data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"])):
        try:
            Data = yt_initial_data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][index]["videoRenderer"]
            
            
            json_data["Data" + str(index)] = {"videoId"   : Data["videoId"] ,
            "thumbnail" : Data['thumbnail']['thumbnails'][-1]['url'] ,
            "title"     : Data['title']["runs"][0]["text"] ,
            "publishedTimeText" : Data['publishedTimeText']['simpleText'],
            "views"     : Data['viewCountText']['simpleText'] ,
            "Length"    : Data['lengthText']["simpleText"] } 
            
            Value = json_data["Data" + str(index)]
            html += f"""
            <div class="item horizontal-item">
                <img src="{Data['thumbnail']['thumbnails'][-1]['url']}" alt="Item 2 Image" class="thumbnail">
                <div class="data">
                    <h3>{Data['title']["runs"][0]["text"]}</h3>
                    <p>{Data['publishedTimeText']['simpleText']}</p>
                    <p>{Data['viewCountText']['simpleText']}</p>
                    <p>{Data['lengthText']["simpleText"]}</p>
                    <a href="#" onclick="sendData({Value})">Details</a>
                </div>
            </div> """


        except:
            #print("Nothing! at ", index)
            pass
    if typo == 0 : return html 
    else: return json_data

#Web script!

def index_html(Data):
    index_html = """
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
            margin: 20px auto; /* Center the search container */
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

        .item.horizontal-item {
            display: flex;
            align-items: center;
            padding: 10px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px; /* Add margin between items */
        }

        .item.horizontal-item .thumbnail {
            width: 200px; /* Adjust the width as needed */
            height: auto; /* Maintain aspect ratio */
            margin-right: 10px;
            border-radius: 5px;
        }

        .item.horizontal-item .data {
            flex: 1; /* Take remaining space */
        }

        .item.horizontal-item h3 {
            margin-top: 0;
        }

        .item.horizontal-item p {
            margin: 5px 0;
        }

        .item.horizontal-item a {
            display: block;
            margin-top: 10px;
            text-decoration: none;
            color: #333;
            font-weight: bold;
        }
    </style>
    <script>
    function sendData(data) {
        const url = 'Listen';
        const query = `?videoId=${encodeURIComponent(data.videoId)}&thumbnail=${encodeURIComponent(data.thumbnail)}&title=${encodeURIComponent(data.title)}&publishedTimeText=${encodeURIComponent(data.publishedTimeText)}&views=${encodeURIComponent(data.views)}&Length=${encodeURIComponent(data.Length)}`;
        window.location.href = url + query;
    }
    </script>

</head>
<body>

<header>
    <h1>My Website</h1>
</header>

<div class="search-container">
    <form class="search-form" action="/" method="post">
        <input type="text" name="query" placeholder="Search...">
        <button type="submit">Search</button>
    </form>
</div>

<div class="items">""" + f""" 

{Data}

    
</div>

</body>
</html>

"""
    return index_html

def Listen_html(Data):
    html = """
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
            transition: background-color 0.3s;
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
</head> """ + f"""
<body>
    <div class="audio-player">
        <img class="thumbnail" src="{Data["thumbnail"]}" alt="Thumbnail">
        <h2 class="title">{Data['title']}</h2>
        <span class="view-count">{Data['views']}</span>
        <audio controls>
            <source src="{Data['audio_url']}" type="audio/mpeg">
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
        const audio = document.querySelector('audio'); """ + """

        function togglePlayPause() {
            if (audio.paused) {
                audio.play();
            } else {
                audio.pause();
            }
        }

        function skip(time) {
            audio.currentTime += time;
        }

        function changeVolume(volume) {
            audio.volume = volume;
        }
    </script>
</body>
</html>



"""
    return html

#Application!

app = Flask(__name__)

# Define a route for handling the search request
@app.route('/', methods=['GET', 'POST'])
def search():
    global q_data
    if request.method == 'POST':
        try :
            query = request.form['query'] + " Music"
            print("Search Query:", query)
            query = query.replace(" ", "+")
            return index_html( yt_search(query , 0 ))
        except:
            data = request.get_json()
            data['audio_url'] = yt_url(data['videoId'])
            print("Data Processed:\n", Listen_html(data))
            return "request made"
    else:
        
        return index_html("")

@app.route('/Data/<query>', methods=['GET', 'POST'])
def Search(query):
    global q_data
    
    print("Search Query:", query)
    query = query.replace(" ", "+")
    return  yt_search(query , 1 )
        

@app.route('/Listen', methods=['GET', 'POST'])
def Listen():
    data = {
            'videoId'       : request.args.get('videoId', 'No video ID provided'),
            'thumbnail'      : request.args.get('thumbnail', 'No thumbnail provided'),
            'title'          : request.args.get('title', 'No title provided'),
            'publishedTimeText' : request.args.get('publishedTimeText', 'No published time provided'),
            'views'         : request.args.get('views', 'No views provided'),
            'Length'         : request.args.get('Length', 'No length provided') 
            }
    data['audio_url'] = yt_url(data['videoId'])

    return Listen_html(data)
    
@app.route('/Data/Listen', methods=['GET', 'POST'])
def Listen2():
    data = {
            'videoId'       : request.args.get('videoId', 'No video ID provided'),
            'thumbnail'      : request.args.get('thumbnail', 'No thumbnail provided'),
            'title'          : request.args.get('title', 'No title provided'),
            'publishedTimeText' : request.args.get('publishedTimeText', 'No published time provided'),
            'views'         : request.args.get('views', 'No views provided'),
            'Length'         : request.args.get('Length', 'No length provided') 
            }
    data['audio_url'] = yt_url(data['videoId'])

    return data
    
#if __name__ == "__main__":
#    app.run(debug=True)
