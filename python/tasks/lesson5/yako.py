## Wanted to make the assignments in Lesson 5 into something fun
## This program is the start of perhaps a roguelike game that utilizes
## functions necessary for the completion of the tasks
## Means that there may be some unnecessary steps/prints
## or unorthodox practices

import random

## Use a die roll to affect how many properties are fetched for the run?
## Have classes for like weapons, scenery, entities
## Let user set a name for self and entities

## Part of assignment to show run settings - export to JSON?

## Have a standard Journey to embark on??


## Class to ensure that the assignments are fulfilled
class Assignment():
  def __init__(self):
    pass

  ## Kap6Uppg1
  ## Have a list of professions that are died for and put in front of the name

  class Person():
    def __init__(self, name="", age=0, gender="XX/XY"):
      self.name = name
      self.age = age
      self.gender = gender

    def set_age(self, inage):
      self.age = inage - 20
      if self.age < 8:
        self.age = 8

    def set_name(self, name):
      epithets_XX = ["Taddle Toddler", "Demonic Witchborn", "Googly Eyes", "Aristocrat", "Ectoplastic Fantastic",
                     "Dreamwork", "Simple", "Mean", "Tender Loin", "Eatwell", "Wizzy Lizzy Red Hot", "Lunatic",
                     "Cracklepop"]
      epithets_XY = ["Gizzard Gizzard", "Softwimp", "Barbarian", "Sad", "Aristocrat", "Eatwell", "Bigmouth",
                     "Lonely", "Creepy", "Loathsome", "Heroic Haired", "Coffin Pusher", "Wizkid"]

      if self.gender == "XX":
        self.name = f'{epithets_XX[roll_die12()]} {name}'

      else:
        self.name = f'{epithets_XY[roll_die12()]} {name}'

    def set_gender(self, ingender="XY"):
      self.gender = ingender

    def get_gender(self):
      return self.gender

    def get_name(self):
      return self.name

    def get_age(self):
      return self.age

    def print_person(self):
      print(f'Name: {self.name}\n Age: {self.age}\n Gender: {self.gender}')

  ## Kap5Uppg2
  def boss_ultimate_blast(self):
    magnitude = roll_die6()

    def blast_damage():
      dmg_list = []  ## Inits and ensures dmg_list clear on function call
                     ## for non-stacking dmg
      for i in range(6):
        dmg_list.append(roll_die6())

      return dmg_list

    damage = sum(filter(lambda x: x > magnitude, map(lambda x: x*x, blast_damage())))
    return damage

  ## Kap6Uppg2 - Can be used to calculate the boss arena
  class Rectangle:
    def __init__(self, width=0, height=0):
      self.x = width
      self.y = height

    def set_width(self, inval):
      self.x = inval

    def set_height(self, inval):
      self.y = inval

    def get_width(self):
        return self.x

    def get_height(self):
        return self.y

    def circumference(self):
      return 2 * self.x + 2 * self.y

    def area(self):
      return self.x * self.y


def roll_die6():
  return random.randint(1,6)

def roll_die12():
  return random.randint(1,12)

class Entity:
  def __init__(self):
    pass

class Menu:
  def __init__(self):
    self.options = [
      "0. Input user information",
      "1. Configure run settings",
      "2. Show current run settings",
      "3. Embark on the Journey",
      "4. Quit"
    ] ## 1 - Enable multiusers further on?

  def display_menu(self):
      for option in self.options:
        print(option)

  def get_choice(self):
      choice = input("")
      return choice

class SubMenu(Menu):
  def __init__(self):
      Menu.__init__(self)  ## super??
      self.options = [
        "1. Create your list of items and equipments",
        "2. Create your list of entities and characters",
        "3. Create your list of scenery and universe",
        "4. Clear all settings",
        "5. Go back"
      ] ## 3 - Have the Assignment Rectangle here to calc boss area

  def print_stored_settings(self):
    pass

class ItemNEquipMenu(SubMenu):
  def __init__(self):
    SubMenu.__init__(self)
    self.options = [
      "Dual Daggers",
      "Weird looking stick",
      "Distasteful Madness",
      "Minor Delirium",  # If both deliriums are picked, you become ultradeliric
      # and you lose the ability to pick any other items.
      # The universe will automatically be set to a chronic
      # reality-shifted dreamworld.
      "Major Delirium",
      "Flashlight from the future",
      "Latent trait",
      "Portable portal",  # Comes with a portable entrance and portable exit.
      # Lose any and weird things will happen.
      "Whatever weapon"  # Just as it says. Die6/12 in combat. Can change spontaneously.
    ]


    self.equipment_list = []

  ## Kap5Uppg1
  def set_equipment_list(self, *args, **kwargs):
    for item in args:
      item_properties = kwargs.get(item, {})
      self.equipment_list.append({
        'name': item,
        'properties': item_properties
      })

  def print_equipment_list(self):
    return print(self.equipment_list)

  def get_equipment_list(self):
    return self.equipment_list

  def set_madness(self):
    self.equipment_list = ["Minor Delirium", "Major Delirium"]

  def display_menu(self):
      for index, option in enumerate(self.options, start=1):
        print(f'{index}: {option}')

## Object declarations

def main():
  SubMenu1 = SubMenu()
  MainMenu = Menu()

  while True:
    print("\n**** Game Menu ****")
    MainMenu.display_menu()

    while True:
      menu_choice = MainMenu.get_choice()
      if menu_choice.isdigit() and 0 <= int(menu_choice) < 5:
        break
      print("Invalid choice.")

    ## Kap6Uppg1
    if menu_choice == '0':

      while True:
        try:
          playergender = input("Input your gender, XX/XY: ").upper()
          if playergender not in ["XX", "XY"]:
            raise ValueError
          break  # Exit loop if input is correct
        except ValueError:
          print("Don't you know your own gender?")

      while True:
        try:
          playername = input("Enter your player name: ")
          break
        except:
          print("Error in input, try again")

      while True:
        try:
          playerage = int(input("Enter your age: "))
          break
        except ValueError:
          print("Use integers fool...")

      PlayerTitle = Assignment.Person()
      PlayerTitle.set_gender(playergender)
      PlayerTitle.set_name(playername)
      PlayerTitle.set_age(playerage)
      print(f"\nYour ASAB gender is: {PlayerTitle.get_gender()}\nLucky.\nIn this world gender is only a construct and you may change it later through Alchemy\n")
      print(f"Your birthname in this world is: {PlayerTitle.get_name()}\n")
      print(f'Your age is: {PlayerTitle.get_age()}\nReal nightmares start when you are young.')
      input("Press enter to continue...")

      ## Necessary for Kap6Uppg1
      print(f"Whole object is: {vars(PlayerTitle)}")

    if menu_choice == '1':
      while True:
        SubMenu1.display_menu()
        submenu_choice = SubMenu1.get_choice()
        if submenu_choice.isdigit() and 0 < int(submenu_choice) < 6:
          break
        input("Invalid choice.")

      if submenu_choice == '1':
        ### Use sets??
        start_items_set = set()
        start_item_description_set = set()
        JourneyEquipments = ItemNEquipMenu()
        number_of_repeats = 0
        while number_of_repeats < 3:
          while True:
            JourneyEquipments.display_menu()
            item_choice = JourneyEquipments.get_choice()
            if item_choice.isdigit() and 0 < int(item_choice) < 10:
              number_of_repeats += 1
              break
            input("Invalid choice.")

            ## If both option Minor Delirium and Major Delirium are picked they will be the only in the
            ## store_equipments and they will act as split personalities with different
            ## traits


          # Check if both 'Minor Delirium' and 'Major Delirium' are in the equipment list
          equipment_names = [item['name'] for item in JourneyEquipments.get_equipment_list()]
          if 'Minor Delirium' in equipment_names and 'Major Delirium' in equipment_names:
            print("Enter here to break")
            JourneyEquipments.set_madness()
            break

              ## Defining Weapons
              ## Dual Daggers - Damage and speed may be adjusted later
          if int(item_choice) == 1 or int(item_choice) == 2:
            while True:
              try:
                weapon_damage = int(input("Assign Weapon Damage: "))
                if weapon_damage > 12:
                  weapon_damage = 12
                elif weapon_damage == 0:
                  weapon_damage = 1
                break
              except ValueError:
                print("Integers only")

            while True:
              try:
                weapon_speed = int(input("Assign Weapon Speed: "))
                if weapon_speed > 3:
                  weapon_speed = 3
                elif weapon_speed == 0:
                  weapon_speed = 1
                break
              except ValueError:
                print("Integers only")

            if int(item_choice) == 1:
              weapon_damage = weapon_damage // 2
              weapon_speed = weapon_speed * 3

            weapon_name = JourneyEquipments.options[int(item_choice)-1]
            JourneyEquipments.set_equipment_list(
              weapon_name,
              **{weapon_name: {'damage': weapon_damage, 'speed': weapon_speed}}
            )  ## Unpacking dictionary into keyword weapon_name for dynamic passing of
               ## properties to the kwargs in method set_equipment_list(self, *args, **kwargs)

            JourneyEquipments.print_equipment_list()
            input("")


      ## List of scenery and universe
      if submenu_choice == '3':
        while True:
          print("""1. Universes
2. Kingdoms
3. Dungeons
4. Boss Arenas - Smaller for increased difficulty""")
          scene_choice = input("")
          if scene_choice.isdigit() and 0 < int(scene_choice) < 6:
            break
          print("Invalid choice.")

        if scene_choice == '4':
          while True:
            print("""<<>> Pick you arena <<>>:
1. Pit of Fire
2. Square of Self Sacrifice
3. Rectangled Recklessness
4. Tough Love Triangle""") # If the player sets too high of measures to have it too easy
                 # we have to code a reversal effect as punishment, setting it to
                 # the smallest arenas instead.

            arena_choice = input("")
            if arena_choice.isdigit() and 0 < int(arena_choice) < 5:
              break
            print("Invalid choice.")

          ## Kap6Uppg2
          if arena_choice == '3':
              print("""Darkness envelops around your feet and breathing becomes harder...
Sight gets blurry and you feel dizzy - Are your eyes really open?
Stuck, and walled in, with creatures coming from every direction, lurkers from the dark.
Every day you flee and fight but they keep coming for more.
Take you to the realm of nothingness:

How did your existence become this meaningless.
Why did everyone you once trust and held close leave? 
You start to realize that your past is just a pitiful, ugly, disgusting animal.

Former achievements are only as good as the dust in the face of disappointment.
Intrusive thoughts conceive and enter your mind.
It's the empty gray matter you can't stand.    
    
It reeks, it stinks. 
Perfect presentation of your fears, doubts, insecurities and cowardism:
Were you ever good enough?
               
Declare the width and height of your human reach and prepare for the battle 
against your own Recklessness""")

              RecRec = Assignment.Rectangle()

              while True:
                try:
                  recwidth = int(input("Rectangle width: "))
                  recheight = int(input("Rectangle height: "))
                  break
                except ValueError:
                  print("Are you foolish? Enter integers...")

              RecRec.set_width(int(recwidth))
              RecRec.set_height(int(recheight))

              print(f'Rectangled Recklessness Area = {RecRec.area()}')
              print(f'Rectangled Recklessness Circumference = {RecRec.circumference()}')

              satisfied = input("Are you satisfied with your choice, Y/N?\n")
              if not satisfied.lower() == 'Y':
                input("Too bad. Accept your path.")
              else:
                input("Let's hope that you are right.")


    if menu_choice == '4':
      for object_name in ['PlayerTitle', 'RecRec', 'JourneyEquipments']:
        if object_name in globals():
          del globals()[object_name]
      del MainMenu
      del SubMenu1
      exit()

if __name__ == '__main__':
  main()