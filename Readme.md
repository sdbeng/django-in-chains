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