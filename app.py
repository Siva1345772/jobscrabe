from flask import Flask, Response
import urllib.request

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_html():
    url = "https://in.indeed.com/jobs?q=digital+marketing&l=chennai&radius=25&start=2"

    # Send request
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )

    # Open and read response
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')

    # Return as downloadable file without saving
    return Response(
        html,
        mimetype="text/html",
        headers={"Content-Disposition": "attachment;filename=indeed_source.html"}
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
