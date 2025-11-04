# FastAPI setup for meme share application

## Done by Venkataraman T S K

This is a FastAPI backend consisting of 3 main files namely main.py, models.py and __init__.py file. the main.py file contains the core logic, where models.py consists of the schema we would be working, very useful in terms of database connections in future and finally, __init__.py , making this file explicit would allow us to handle imports and relative imports  work when modules are imported as `python.main:app`

the basic format of the data is passed is the "id" which would be the identifier, the title, dsecription and then the timestamp of the post. The backend offers Create, Read, Update, Delete options , thus covering GET, POST, PUT, DELETE api methods simplified.
