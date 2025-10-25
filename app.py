from flask import Flask, Response
import urllib.request

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_html():
    url = "https://in.indeed.com/jobs?q=digital+marketing&l=chennai&radius=25&start=2"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive',
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')

        return Response(
            html,
            mimetype="text/html",
            headers={"Content-Disposition": "attachment;filename=indeed_source.html"}
        )
    except urllib.error.HTTPError as e:
        return f"Error fetching page: {e.code} {e.reason}", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
