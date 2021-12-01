# Short Description
I have created DRF application that uses MongoDB Database. User have ability to fill the DB by runing the script. 
Application has only one endpoint: http://127.0.0.1:8000/api/ by which user can receive following date:
- Top 10 authors (by number of texts)
- Distribution of text creation in time (last 24 months) 
# How to launch the solution
You wiil need Docker, python3 and any integrated development environment for the Python programming language.
1. Clone git repository https://github.com/veronikadajneko/DjangoRest-MongoDB.git
2. Go to the project directory
```
cd project
```
2. Start Docker Desktop application
3. Run docker command 
```
docker-compose up
```
# How to fill the database
1. In project directory run command
```
docker-compose exec web python3 pymongo_test_insert.py
```
You can check the database http://localhost:8081

- database_name: library
- table_name: catalog_texts

# How to use the API
1. Visit http://127.0.0.1:8000/api/ 
