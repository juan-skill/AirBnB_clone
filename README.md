![](https://i.ibb.co/d5N85Nh/hbnb.png)

# AirBNB / Implementation for python shell console

This is a project that implements a console in python,  its arguments are composed by  a command and its argumenst. Where a command can be written with its corresponding argument to execute it in relation to the classes that make up the project that seeks to imitate the room rental page, airbnb


##Project Description
In this project is created a data model that managed its objects via a command interpreter and store and persist objects to a file. This is the first step of a project that have to imitate the airbnb web page. This part made an abstraction betwee the object and how it is stored in a way that this object can be accesed later, even the fact the machine were shut down.

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUZGDONYM4%2F20200220%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200220T040201Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=076c88a1fdf168d8e7097a0fc4d34ef11171309bbccba541f0a94c8e92703171)

##Class diagram

<a href="https://ibb.co/g7h4mJk"><img src="https://i.ibb.co/W3jVGfm/Consle-UML.png" alt="Consle-UML" border="0"></a>


##Command Interpreter
A command interpreter is an application that shows only the commands, it does not have a powerful graphical interface since it only works with plain text. This is responsible for waiting for the user to enter a specific command to execute an action. In this project you can use commands such as create, destroy, show, among others, in order to manipulate object creations of predefined classes. Like the purple color classes in the diagram, and in this way have persistent information management


## Usage

This is the shell using in interactive mode
```Python
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
This is the way to use in case of non interactive mode

```Python
$$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$
```

### Supported Types

| Type   | Function |
|--------|--------|
| create|  Creates new instance |
| show      | Prints the string represtentation of an instance |
| destroy      | Deletes an instance based on the class |
| all | Print all representation of all instances |
| update      | Update instances based on the class |


##Example

```Python
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
my_model.save()
print(my_model)

```

output

```Python
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'Holberton', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
```


#Authors
