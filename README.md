## The task
## 1. Prepare a Dockerfile that launches a document-oriented database of your choice
- Example: ElasticSearch
## 2. Prepare a script that fills the database with few (up to 100) documents of the following content
- Textual paragraph (can use Lorem Ipsum generator)
- Fictional name of the text author (can use any personal names generator)
- Random date when the text has been created (within few years from today)
## 3. Fill the database with generated data
- Manually (should be described in README file)
- Or automatically on container start
## 4. Implement a simple Web application
 - Update the Dockerfile to launch the Web application as a container
 - With REST or RPC interface (your choice)
 - A single endpoint should return the statistics
   - Top 10 authors (by number of texts)
   - Distribution of text creation in time (last 24 months) 
## 5. Prepare a README that describes
- How to launch the solution
- How to fill the database
- How to use the API
## 6. Publish full solution to one of the public code repositories 
- Example: GitLab

# How to launch the solution
