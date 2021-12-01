# Short Description
I have created DRF application that uses MongoDB Database. User has ability to fill the DB with random values by runing the script. 
Application has only one endpoint: http://127.0.0.1:8000/api/ . With it user can access following data:
- Top 10 authors (by number of texts)
- Distribution of text creation in time (last 24 months) 

Stack of technologies: Docker, Python, DRF, MongoDB.
# How to launch the solution
1. Clone git repository 
```
git clone https://github.com/veronikadajneko/DjangoRest-MongoDB.git
```
2. Go to the project directory
```
cd project
```
3. Run docker command 
```
docker-compose up
```
# How to fill the database
In project directory run next command
```
docker-compose exec web python3 pymongo_test_insert.py
```
You can check the database http://localhost:8081

- database_name: library
- table_name: catalog_texts

# How to use the API
 Visit http://127.0.0.1:8000/api/ 
