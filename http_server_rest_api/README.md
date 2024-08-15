## Coding task 3: REST API server
This task involves implementing a simple HTTP server using Tornado that provides a REST API for filtering mocked DB by tags and subtags. If no tag is passed by a query parameter, the server return 400 status code.

#### API endpoints
- `GET /taggedContent?tag=<tag>`: Returns a list of content items that have the specified tag.

#### How to run
1. Install the required packages using `pip install -r requirements.txt`.
2. Run the server using `python rest_api_server.py`.