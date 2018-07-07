Welcome to Log Analysis Project
Introduction
This is the solution for the Logs Analysis project we have to execute complex queries on a large database (> 1000k rows) to extract intersting stats.
Like 
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 
The database in question is a newspaper company database where we have 3 tables; articles, authors and log.

articles - Contains articles posted in the newspaper so far.
authors - Contains list of authors who have published their articles.
log - Stores log of every request sent to the newspaper server.
This project implements a single query solution for each of the question in hand. See main.py for more details.

To Run You will need:
Python3
Vagrant
VirtualBox
Setup
Install Vagrant And VirtualBox
Download then unzip the newsdata.zip file and navigate to the folder where the project exists 
Here is a link to download our database https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
To Run:

Launch Vagrant VM by typing "vagrant up", you can the log in with "vagrant ssh"

To load the data, use the command "psql -d news -f newsdata.sql" to connect a database and run the necessary SQL statements.

The database includes three tables:

Authors table
Articles table
Log table
To execute the program, run python3 SourceCode.py from the command line.