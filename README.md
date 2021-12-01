# How to launch the solution
1. Clone git repository https://github.com/veronikadajneko/Docker-MongoDB-Django-Rest-Framework.git
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
