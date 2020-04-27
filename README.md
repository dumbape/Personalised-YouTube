# Personalised-YouTube

## Features
1. Async calls youtube Data API v3 (refer MiniYT/data/models.py) - uses Threading. 
   Fetch interval can be set by admin before starting server. (Instructions ahead)
   Stores relevant data in DB and indexes on tile + description in order to perform Full Text Search (FTS).
   We use PostgreSQL's GIN index feature to create indexes on a combination of fields. (Refer MiniYT/data/models.py)
2. Get API returns list of all videos in DB in a paginated fashion acc to latest publishedTime (refer MiniYT/api/views.py)
3. Search API returns list of matched videos to a query in a paginated fashion acc to latest publishedTime (Refer MiniYT/api/views.py)
4. Project is dockerized. A docker-compose.yml and a Dockerfile have been provided to quickly build and deploy locally.

## Get it running
1. Make sure docker is present and running
2. Run in the folder containing `docker-compose.yml`:
   `docker-compose up -d --build`
3. Goto `http://0.0.0.0:8000/admin/`. Login using Username `root` and password `root`.
4. Goto `Api fetchs` under `Data` section and click the only entry which says `False`.
5. Fill in the relevant details - `searchQuery`, `apiKey`, `fetchInterval` (in seconds). Make sure these are correct as 
   you won't be able to edit it after checking `FetchAPI`. Once you are sure, check the `FetchAPI` option and click on Save.
   Now, all these fields will be read-only. You have to start the container again to be able to modify these.
6. The server starts pulling videos from the youtube server. If there is any error, you can see it in the logfile of docker.
7. To list all the videos, goto: `http://0.0.0.0:8000/api/list`. It is a dashboard where you can see the entries in the database 
   in a paginated fashion.
8. To search videos, goto: 'http://0.0.0.0:8000/api/search?query=<your_query>' to see the relevant results on the dashboard.
   The API fetches partial matches too, from the title and description.
   
To stop, take down the containers - `docker-compose down -v`.
