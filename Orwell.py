""" Orwell The Game: Text Based Version by JHawks """
print ("""Welcome to the Orwell Security System Headquarters of The Nation located in the capital of Baton.
You have been selected out of many canidates as the new investigator. Pay close attention to the cameras and the cases you are working.
To get started setup your Orwell account with your name and Orwell ID""")

player_name = input('Please type in your name')
player_id = input ('Now type in your orwell id. - Only three numbers ex. 007')

print (f""" Initializing Account...
Completing Setup...
Welcome to Orwell {player_name}""")

# List for suspects
persons_of_interest = []

# Classes for the main players

# Player Class
class Player(object):
    """ Class with main player functions"""
    def __init__(self,name,ID):
        self.name = player_name
        self.ID = player_id

# Supervisor Class
class Supervisor(object):
    """ Class for supervisor character and basic phrases """
    def __init__(self,name):
        self.name = 'Symes'

    def intro(self):
        print (f"""Person: Well Hello There. You must be the newbie,I'm {self.name} your supervisor. From now on I will be assigning you cases and you will report to me the important things you find.
        Do well and maybe you'll be in my position one day. ~ dry condescending laughter ~ Anyway I'll get back to you with a case in a while for now just get acqauinted with the system""")

    def new_case(self):
        print (f"{self.name}: There you are, I assume you heard the news already. This is a major problem so we will need your best work here. Well what are you still doing here get to work newbie!")

    def turn_in(self):
        print (f"""{self.name}: Remember that we take reports from investigators very seriously here, make sure that certain before you turn in your work. I don't want to look like a fool...
        Now if you're sure submit you're conclusions to Orwell""")

# Orwell Security System Class
class Orwell(object):
    """ Class for the orwell security system basic phrases"""
    def __init__(self,name):
        self.name = 'Orwell Security System'

    def new_info(self):
        """ New Info From Orwell Alert """
        print (f"{self.name}: A new file has appeared in association with the current suspect")

    def person_of_interest(self,person):
        """ New Suspect From Orwell Alert """
        self.person = person
        persons_of_interest.append(person)
        print(f"{self.name}: A new person of interest has been added to this case. They are now an option for being reported in your conclusion.")

    def conclude(self):
        """ Conclude Game Phrase """
        print(f"{self.name}: It is time to submit your report and close the case. The person you choose effects many lives, think hard and good work")

# Symes
symes = Supervisor('name')

# Orwell Security System
orwell = Orwell('name')