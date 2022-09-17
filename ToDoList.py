import os
from pathlib import Path
import json
import sys


class Item(object):
    def __init__(self, title, description, author, is_checked):
        self.title = title
        self.description = description
        self.author = author
        self.is_checked = is_checked

    def __repr__(self):
        return f"< title: {self.title} \n description: {self.description} \n made by: {self.author}>"

    def __str__(self):
        return f" title: {self.title} \n description: {self.description} \n made by: {self.author} \n is checked: {self.is_checked}"

    def dump(self):
        return {'title': self.title,
                'description': self.description,
                'author': self.author, 'is_checked': self.is_checked}

    def set_is_checked(self, value):
        if (value):
            self._is_checked = 'V'
        self._is_checked = 'X'


def print_list(items):
    for i in range(len(items)):
        print("Item " + str(i) + ":")
        print(items[i])


def add_item(items):
    title = input("Please add a title for the item ")
    description = input("Please add a description for the item ")
    author = input("Please add an author for the item ")
    is_checked = 'X'
    item = Item(title, description, author, is_checked)
    items.append(item)
    return items


def delete_item(items):
    num_for_deletion = input("Please insert the number item for deletion ")
    int_num = int(num_for_deletion)
    del items[int_num]
    return items


def update_item(items):
    num_for_updation = input("Please insert the number item to update ")
    int_num = int(num_for_updation)
    title = input("Want to update the title? (if not press space) ")
    description = input(
        "Want to update the description? (if not press space) ")
    author = input("Want to update the author? (if not press space) ")
    is_checked = input("Want to mark the item as done? (if not press " ") ")
    if (title is not " "):
        setattr(items[int_num], 'title', title)
    if (description is not " "):
        setattr(items[int_num], 'description', description)
    if (author is not " "):
        setattr(items[int_num], 'author', author)
    if (is_checked is not " "):
        setattr(items[int_num], 'is_checked', 'V')
    return items


def turn_into_json(items):
    res = json.dumps([o.dump() for o in items], indent=3)
    return res


def main():

    my_file = Path("toDoList.json")
    if (my_file.exists()):
        try:
            if os.stat(my_file).st_size > 0:
                print("All good")
            else:
                print("empty file")
                sys.exit(1)
        except OSError:
            print("No file")
            sys.exit(1)
        # JSON file
        try:
            with open('toDoList.json', "r") as f:
                # Reading from file
                data = json.loads(f.read())
                items = []
                for i in range(len(data)):
                    # check in try catch if there is X or V
                    title = data[i]['title']
                    description = data[i]['description']
                    author = data[i]['author']
                    is_checked = data[i]['is_checked']
                    item = Item(title, description, author, is_checked)
                    items.append(item)

                # Closing file
                f.close()
        except FileNotFoundError:
            msg = "Sorry, the file does not exist."
            print(msg)  # Sorry, the file John.txt does not exist.
            sys.exit(1)
    else:
        items = []

    def menu(items):

        ans = True
        while ans:
            print("""
            1.Add new itwm
            2.Delete an item
            3.Update an item
            4.Show items list
            5.Exit/Quit
            """)
            ans = input("What would you like to do? ")
            if ans == "1":
                items = add_item(items)
                print("\n item Added ")
            elif ans == "2":
                items = delete_item(items)
                print("\n item Deleted ")

            elif ans == "3":
                items = update_item(items)
                print("\n item updated ")
            elif ans == "4":
                json_list = turn_into_json(items)
                try:
                    with open("toDoList.json", "w") as f:
                        f.write(json_list)
                        f.close()
                except FileNotFoundError:
                    msg = "Sorry, the file does not exist."
                    print(msg)  # Sorry, the file John.txt does not exist.
                    sys.exit(1)
                print_list(items)

            elif ans == "5":
                print("\n Goodbye")
                ans = False
            elif ans != "":
                print("\n Not A Valid Choice Try again")
    menu(items)


if __name__ == "__main__":
    main()
