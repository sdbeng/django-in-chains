## Django project
Hook up a users and blog app to a template based application. Working with classes and models.

### Useful commands
- to drop in a shell
`$ python3 manage.py shell`
- add new data
```
>>> from users.models import User
>>> jane = User(first_name='jane', last_name='Doe',email='jane@doe.com',age=72)
>>> jane.save()
>>> User.objects.all()
<QuerySet [<User: jane Doe | jane@doe.com>]>
```
- run migrations
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
- to query for 1 user id
```
>>> from users.models import User
>>> User.objects.get(first_name='jane').id
```
- The sqlmigrate command doesn’t actually run the migration on your database - it just prints it to the screen so that you can see what SQL Django thinks is required. It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.
```
python3 manage.py sqlmigrate users 0001
```
sample output:
```
BEGIN;
--
-- Create model User
--
CREATE TABLE "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(265) NOT NULL, "last_name" varchar(265) NOT NULL, "email" varchar(265) NOT NULL, "age" integer NOT NULL);
COMMIT;
```

- you can also run python manage.py check; this checks for any problems in your project without making migrations or touching the database.
`$python3 manage.py check`