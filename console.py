#!/usr/bin/python3
""" Class for Command promt. """


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = "(hbnb) "
    class_check = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Exit command to exit the program print()\n"""
        return True

    def emptyline(self):
        """shouldn’t execute anything"""
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        Exceptions:
            SyntaxError: when there is no args given
            NameError: when there is no object taht has the name
        """
        print(args)
        if not args:
            print("** class name missing **")
        elif args in HBNBCommand.class_check:

            lists = args.split()
            print('list[0]===', lists[0])
            obj = eval("{}()".format(lists[0]))
            obj.save()
            print(obj.id)
            storage.reload()

        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance based on the class name"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.class_check:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        #print(all_objs)
        key = args[0] + '.' + args[1]
        #print(key)
        if key in all_objs:
                print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.class_check:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
 #       print(all_objs)
        key = args[0] + '.' + args[1]
        if key in all_objs:
            all_objs.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ shouldn’t execute anything. """

        if not args:

            obj_dict = storage.all()
            obj_list = []
            for key in obj_dict.keys():
                obj_list.append(str(obj_dict[key]))

            if len(obj_list) != 0:
                print(obj_list)
        else:
            #print('args===', args)
            args = args.split()
            #print('args split ===', args)
            if args[0] in HBNBCommand.class_check:

                obj_list = []
                obj_dict = storage.all()
                for key in obj_dict:
                    name = key.split('.')
                    if name[0] == args[0]:
                        obj_list.append(str(obj_dict[key]))

                if len(obj_list) != 0:
                    print(obj_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, args):
        """ shouldn’t execute anything. """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[0] not in HBNBCommand.class_check:
            print("** class doesn't exist **")
            return

        value = str(args[3]).strip("\"':")
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            print('obj_id===args[1] ====', obj_id, args[1])
            name = obj_id.split('.')
            print('name===', name)
            if name[1] == args[1]:

                setattr(all_objs[obj_id], args[2], value)
                storage.save()
                return
        print("** no instance found **")


if __name__ == '__main__':


    HBNBCommand().cmdloop()
