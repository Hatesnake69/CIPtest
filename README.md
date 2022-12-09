# CIPtest
to run this code you need to:
- run ```copy example.env .env```
- run ```docker-compose up --build --no-deps ```

after that is done you can view application at http://127.0.0.1:8000/docs

GET /statistics requires from_date: date, to_date: date filter_column: [created_at, views, clicks, rub_cost, cost_per_click, cost_per_view], desc: bool parameters
<br> it responses with list of statistic entities

POST /statistics requires "views": positiveint, "clicks": positiveint, rub_cost: Optional[float], cost_per_click: Optional[float], cost_per_view: Optional[float] fields 
<br> it responses with json of statistic entity

DELETE /delete_all_statistics deletes all db records and returns "message": "All data successfully deleted"


To run tests: ```docker exec -it app pytest```