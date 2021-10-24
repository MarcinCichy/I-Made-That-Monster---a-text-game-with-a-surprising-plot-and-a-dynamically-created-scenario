import os
import time
from art import *
from termcolor import colored, cprint


def clear_screen():
    """ Clear the screen in depends of operation system (Windows, Linux or iOS).
        It was copied from internet,  I will find out how it works in future (_=system is unknow for me) :)"""
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def show_guide():
    clear_screen()
    print ('\n INSTRUKCJA:')
    print (' --------------------------------------------------------------')
    print (' Wybierz jedną ze wskazanych opcji lub:')
    print (' Naciśnij - [I], zobaczysz tą instrukcję.')
    print (' Naciśnij - [Z], zabierzesz znaleziony przedmiot.')
    print (' Naciśnij - [K], zobaczysz co masz w kieszeni.')
    print (' Naciśnij - [U], użyjesz znaleziony przedmiot. \n')
    time.sleep(4)


def title_screen():
    clear_screen()
    tprint ('I Made That Monster', 'ghoulish')
    time.sleep(5)


def read_file(any_used_items):
    path_name = os.getcwd()     
    if int(any_used_items) != 0:        
        file_path = path_name + "\\alternative_descriptions.txt"
    else:
        file_path = path_name + "\\descriptions.txt"
    with open(file_path, encoding = "utf-8") as file:
        return file.readlines()


def show_description(chapter, any_used_items):
    clear_screen()
    chapter = chapter.upper()
    file_content = read_file(any_used_items)
    for num, line in enumerate(file_content):
        if  ("START_"+chapter) in line:
            start_count_line = num + 4
        if  ("END_"+chapter) in line:
            end_count_line = num - 2
    print (end="".join(file_content[start_count_line:end_count_line]))
    

def wrong_answer(chapter):
    chapter = chapter.upper()
    file_content = read_file(0)
    for num, line in enumerate(file_content):
        if  ("START_"+chapter) in line:
            wrong_answer_line = num + 2
            return file_content[wrong_answer_line]


def good_answer(chapter, any_used_items):
    chapter = chapter.upper()
    file_content = read_file(any_used_items)
    for num, line in enumerate(file_content):
        if ("START_"+chapter) in line:
            good_answer_line = num + 3
            return file_content[good_answer_line]


def can_use_item(chapter, any_used_items):
    file_content = read_file(any_used_items)
    for num, line in enumerate(file_content):
        if ("END_"+chapter) in line:
            permission = num - 1
            return file_content[permission]


def create_rooms_names(any_used_items):  
    list_of_rooms = []
    file_content = read_file(any_used_items)
    for num, line in enumerate(file_content):
        if ("START" in line) and ("ROOM" in line) and (not "TRAP" in line) and (not "ITEM" in line):
            list_of_rooms.append(line[6:].strip())
    return list_of_rooms


def create_list_of_equipment(any_used_items):
    list_of_all_equipment = []
    file_content = read_file(any_used_items)
    for num, line in enumerate(file_content):
        if ("START") and ("ROOM" in line) and (not "TRAP" in line) and (not "ITEM" in line):
            if file_content[num+1].strip() != "#" and file_content[num+1].strip() != "":
                list_of_all_equipment.append(file_content[num+1].strip())
    return list_of_all_equipment


def check_equipment_exist_in_room(chapter, any_used_items):
    chapter = chapter.upper()
    file_content = read_file(any_used_items)
    for num, line in enumerate(file_content):
        if ("START_"+chapter) in line:
            equipment_line = num + 1
            if file_content[equipment_line] != '#':
                return file_content[equipment_line]
            else:
                return None


def show_room(room_numb):
        room_obj = list_of_rooms[room_number]
        rooms[room_obj].show_room_description() 


def show_menu():
    # print ("\nWybierz: ")
    # print ("[Z] - zabierz przedmiot")
    # print ("[K] - zawartość kieszeni")
    # print ("[U] - użyj przedmiot")
    print ("\n[I] - instrukcja\n")


def you_loos():
    clear_screen()
    tprint ("PRZEGRALES !!!", "ghost")
    time.sleep (4)


def end_game():
    clear_screen()
    tprint ("TO JEST KONIEC GRY" )
    tprint ("Tak,  to  ty  stworzyles  tego  Potwora!" )
    time.sleep(3)
    answer = input("\nCzy chcesz zagrać jeszcze raz [T]ak/[N]ie ? \n")
    if answer.lower() == "n":
        clear_screen()
        pass
    elif answer.lower() == "t":
       return "t"



