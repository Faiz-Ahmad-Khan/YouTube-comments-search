# YouTube-comments-search

This Flask-based API allows you to search comments from a YouTube video using various filters such as author name, date range, like count, reply count, and text content.

## Usage

### Endpoints

- `/search`
    - **Method**: `GET`
    - **Parameters**:
        - `search_author`: Search comments by author name.
        - `at_from`: Filter comments after a specific date (format: DD-MM-YYYY).
        - `at_to`: Filter comments before a specific date (format: DD-MM-YYYY).
        - `like_from`: Minimum number of likes for comments.
        - `like_to`: Maximum number of likes for comments.
        - `reply_from`: Minimum number of replies for comments.
        - `reply_to`: Maximum number of replies for comments.
        - `search_text`: Search comments by text content.

### Example

To search comments with specific criteria: `<base-url>/search?search_author=Fredrick&at_from=01-01-2023&at_to=01-02-2023&like_from=0&like_to=5&reply_from=0&reply_to=5&search_text=economic`

This will return comments where:
- Author name contains 'Fredrick'.
- Comments are posted between dates 1 Jan 2023 and 1 Feb 2023.
- Number of likes is between 0 to 5.
- Number of replies is between 0 to 5.
- Comment text contains 'economic'.

### Response

The API response will be a JSON array containing the filtered comments in the specified criteria.

## Setup

To set up this application locally, follow these steps:

1. Clone the repository.
2. Install required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python app.py`.
4. Access the API endpoints as described above.

## API Implementation Details

- This API is built using Flask, a Python web framework.
- The comments are fetched from the YouTube API using the provided endpoint.

## Customization

You can customize or extend this API based on your specific requirements by modifying the Flask application in `app.py`.

## Note

This is a basic implementation and might require enhancements, error handling, and further validation based on production needs.

For more information, please refer to the Flask documentation: [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
