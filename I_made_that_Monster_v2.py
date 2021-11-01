# Text game
# "I made that Monster"
# ;-)
#


from operating_functions import *
import time


equipment_taken = []
used_items = []


class Room:
    def __init__(self, name):
        self.name = name
        
    def show_room_description(self, any_used_items):
        show_description(self.name, any_used_items)

    def choose_action(self, room_num, lenght_of_room_list, any_used_items):  
        action = input('> ')
        while (action.lower() != wrong_answer(self.name).strip()) and (action.lower() != good_answer(self.name, any_used_items).strip()) and (action.lower() != 'z') and (action.lower() != 'u') and (action.lower() != 'k') and (action.lower() != 'i'):
            show_description(self.name, any_used_items)
            action = input('> ')
        else:
            if (action.lower()) == (wrong_answer(self.name).strip()):      # strip() to remove NewLine Character from
                self.you_are_trapped("trap_"+self.name, any_used_items)
                return lenght_of_room_list
            elif (action.lower()) == (good_answer(self.name, any_used_items).strip()):  # strip() to remove NewLine Character from
                room_num += 1
                return int(room_num)
            else:
                return action

    def you_are_trapped(self, trap_room_descr, any_used_items):
        clear_screen()
        show_description(trap_room_descr, any_used_items)
        time.sleep(7)
        you_loos()
        clear_screen()
      
        
class Item:

    def __init__(self, name):
        self.name = name

    def use_item(self, chapter, any_used_items):
        print("Masz do wyboru: ", end="")
        print(', '.join(equipment_taken))
        item_to_use = input("Wybierz przedmiot: ")
        permission_to_use_item = can_use_item(chapter, any_used_items)
        if item_to_use not in equipment_taken:        
            print("Przecież nie masz takiego przedmiotu w kieszeniach!")
            time.sleep(2)
        elif permission_to_use_item.strip() != item_to_use:
            print("W tym pomieszczeniu nie możesz użyć tego przedmiotu.")
            time.sleep(2)
        else:
            equipment_taken.remove(item_to_use)
            used_items.append(item_to_use)   
        
    def take_item(self):
        if self.name in equipment_taken or self.name in used_items:
            print("Nie możesz zabrać przedmiotu, który już został zabrany.")
            time.sleep(2)
        else:
            equipment_taken.append(self.name)
            print("Zabrałeś: ", self.name)
            time.sleep(2)
       
    def item_description(self, item_room_descr, any_used_items):
        clear_screen()
        show_description(item_room_descr, any_used_items)
        time.sleep(3)


def main_game():        # nadal pracuje nad ta funkcja i zaznajamiam sie z gitem
    is_used_items = len(used_items)
    title_screen()
    clear_screen() 
    show_guide()
    clear_screen() 
    show_description("FIRST_DESCRIPTION", is_used_items)
    print("\n\n Zawsze po nacisnięciu [I] pojawi się instrukcja.\n")
    input("Nacisnij [ENTER]")   
    list_of_rooms = (create_rooms_names(is_used_items))
    list_of_items = (create_list_of_equipment(is_used_items))
    rooms = {name: Room(name=name) for name in list_of_rooms}
    items = {name: Item(name=name) for name in list_of_items}
    room_number = 0
    # With that loop I can make more and more rooms in 'description.txt' file
    while room_number != (len(list_of_rooms)):
        is_used_items = len(used_items)
        room_obj = list_of_rooms[room_number]
        rooms[room_obj].show_room_description(is_used_items)
        show_menu()
        # It would be too complicated for me to read this line
        # if I used the function call instead of the variable 'room_obj'
        key_pressed = str(rooms[room_obj].choose_action(room_number, len(list_of_rooms), is_used_items))
        if key_pressed.isnumeric():
            room_number = int(key_pressed)
        else: 
            if key_pressed.lower() == "z":
                check_equipment_exist = (check_equipment_exist_in_room(rooms[room_obj].name, is_used_items)).strip()
                if check_equipment_exist in list_of_items and check_equipment_exist not in equipment_taken and check_equipment_exist not in used_items:
                    item_obj = check_equipment_exist
                    items[item_obj].take_item()
                    items[item_obj].item_description("item_"+rooms[room_obj].name, is_used_items)
                    time.sleep(3)
                else:
                    print("W tym pokoju nie ma nic do zabrania.")
                    time.sleep(2)
            elif key_pressed.lower() == "k":
                if len(equipment_taken) == 0:
                    print("Masz puste kieszenie")
                    time.sleep(2)
                else:
                    print("W kieszeniach masz: ", end="")
                    print(', '.join(equipment_taken))
                    time.sleep(4)
            elif key_pressed.lower() == "i":
                show_guide()
            elif key_pressed.lower() == 'u': 
                if len(equipment_taken) != 0:    
                    items[item_obj].use_item(rooms[room_obj].name, is_used_items)
                    time.sleep(2)
                else:
                    print("Nie możesz użyc czegoś, czego nie masz.")
                    time.sleep(2)      
    clear_screen() 
    end_game(rooms[room_obj].name, list_of_rooms, is_used_items)
   

main_game()
time.sleep(3)
