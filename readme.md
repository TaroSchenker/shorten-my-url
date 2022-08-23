# LAP 4 CODING CHALLENGE - The Real URL Shortener

## Installation
* Clone repo
* cd into the folder - `cd shorten-my-urk`
* `pipenv shell`
* `pipenv install`
* locally - `pipenv run dev` running on http://127.0.0.1:3000 

## Deployment
*  deployed to Heroku - https://url-shorten-quick.herokuapp.com/

## Wins & Challenges

### Wins


### Challenges


### Future To-do's

## Contacts



## How to deployto heroku
    1. SQL lite doesnt work well for hosting so we have to change the Db
    2. goto heroku, login
    3. goto resourcs. Search for Heroku postgres. 
    4. goto settings, reveal config vars. there is a database url and your post gres link. copy it. 
    5. insert it into your env file for the DATABASE_URL variable. 
    6. in init we have to add this code 
    if 'postgres:' in database_uri:   
    database_uri = database_uri.replace('postgres:','postgresql:')
    because the namming convention is slightly different. the url we enterered into env could also be changed direct but this is safer in case of future changes .
    7. init the db with pipenv run init_db

## Deploy api
    1. create Procfile
    2 .add web: pipenv run start to Procfile
    3. goto hroku to set up a deployment pileline. enter github repo name. 
    4. connect to repo and clik deploy.     
