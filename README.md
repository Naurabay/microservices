Task:
Create a new table: arrival flights, with the following columns:
- id (int, primary key)
- destination (varchar)
- flight (varchar)
- airline (varchar)
- terminal (integer)
- std (date) default now
- status (varchar) default "new"

Services: 
1. Create a new flight every 10 sec.
2. Read all flights from the database and start bording on airblanes that are near terminal number 2.
3. All flights with destination Dubai and Warsaw are delayed because of weather conditions
4. Delete every 15 sec old flights with status 'On time'.



