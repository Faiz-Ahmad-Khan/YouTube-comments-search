from flask import Flask, request, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

def filter_comments(comments, filters):
    filtered_comments = comments.get("comments", [])
    for key, value in filters.items():
        if key == "at_from" and value:
            value = datetime.strptime(value, "%a, %d %b %Y %H:%M:%S GMT")
            filtered_comments = [c for c in filtered_comments if isinstance(c, dict) and datetime.strptime(c.get("at", ""), "%a, %d %b %Y %H:%M:%S GMT") >= value]
        elif key == "at_to" and value:
            value = datetime.strptime(value, "%a, %d %b %Y %H:%M:%S GMT")
            filtered_comments = [c for c in filtered_comments if isinstance(c, dict) and datetime.strptime(c.get("at", ""), "%a, %d %b %Y %H:%M:%S GMT") <= value]
        elif key in ["like_from", "like_to", "reply_from", "reply_to"]:
            filtered_comments = [c for c in filtered_comments if isinstance(c, dict) and value[0] <= c.get(key, 0) <= value[1]]
        elif key == "search_author":
            filtered_comments = [c for c in filtered_comments if isinstance(c, dict) and value.lower() in c.get("author", "").lower()]
        elif key == "search_text":
            filtered_comments = [c for c in filtered_comments if isinstance(c, dict) and value.lower() in c.get("text", "").lower()]

    return filtered_comments

@app.route('/search', methods=['GET'])
def search_comments():
    try:
        api_url = "https://app.ylytic.com/ylytic/test"
        api_response = requests.get(api_url)
        data = api_response.json()

        search_author = request.args.get('search_author', '')
        at_from = request.args.get('at_from', '')
        at_to = request.args.get('at_to', '')
        like_from = int(request.args.get('like_from', 0))
        like_to = int(request.args.get('like_to', 100))
        reply_from = int(request.args.get('reply_from', 0))
        reply_to = int(request.args.get('reply_to', 100))
        search_text = request.args.get('search_text', '')

        filters = {
            'search_author': search_author,
            'at_from': at_from,
            'at_to': at_to,
            'like_from': (like_from, like_to),
            'reply_from': (reply_from, reply_to),
            'search_text': search_text
        }

        filtered_comments = filter_comments(data, filters)

        return jsonify(filtered_comments)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)