import time
""" Orwell The Game: Text Based Version by JHawks """
print ("""Welcome to the Orwell Security System Headquarters of The Nation located in the capital of Baton.
You have been selected out of many canidates as the new investigator. Pay close attention to the cameras and the cases you are working.
To get started setup your Orwell account with your name and Orwell ID""")

player_name = input('Please type in your name')
player_id = input ('Now type in your orwell id. - Only three numbers ex. 007')

print (f""" Initializing Account...
Completing Setup...
Welcome to Orwell {player_name}""")

# Wait 5 secs between next line of words in simulation
time.sleep(5)

# List for suspects
persons_of_interest = []

# Classes for the automated players #

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

    def check_point1(self):
        print (f"{self.name}:This is a very interesting piece of evidence, keep working with it to see where is goes.")

    def check_point2(self):
        print(f"{self.name}: Strange isn't not sure how it all connects but something doesn't completely check out.")

    def check_point3(self):
        print(f"{self.name}: Seems like thats all the info the Orwell picked up. Time to put it all together now.")

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

# First Day on the Job
symes.intro()
print("""Game Info: If at any time you wish to report you're conclusions type report_conclusion().Until then, follow the simulations instructions""")

time.sleep(10)

# Function to report conclusion and get results
def report_conclusion():
    accused = input("You have decided you are ready to report a suspect. Who have you chosen to report.")
    if accused == 'kaylee':
        print(f"Suspect Kaylee has been taken in and closely examined. There is irrefutable proof that she has commited the crime. Good work Agent {player_id} or should i say {player_name}")
        print("Game Over")
    else:
        print(f"Suspect {accused} was taken in and closely examined. After hours of interrogation, they have maintained complete innocence. Unfortunately the criminal is still rampant and the Nation has made a new enemy")
        print("Game Over")

# All possible suspects and dictionaries of their info
suspect1 = {'Name':'Ray Arayza', 'Occupation':'Unknown','Last Seen':'Walking around Freedom Park', 'Extra':'Former patient at Pleasant Waters Mental Health Inistitute'}
suspect2 = {'Name':'Rena Evilini', 'Occupation':'Unemployed','Last Seen':'Boarding trolley at Freedom Park station', 'Extra':'Has criminal record'}
suspect3 = {'Name':'Kaylee Moral', 'Occupation':'Journalist', 'Last Seen': 'Ceaser Industry Labs', 'Extra':'Friend of Rena Evillini'}

# Functions to give all current info on a suspect
def suspect1_info():
    """Gives all info on suspect 1"""
    for k,v in suspect1.items():
        print(f'{k} : {v}')

def suspect2_info():
    """Gives all info on suspect 2"""
    for k,v in suspect2.items():
        print(f'{k} : {v}')

def suspect3_info():
    """Gives all info on suspect 3"""
    for k,v in suspect3.items():
        print(f'{k} : {v}')

# The Crime Sequence
print (""" --- BREAKING NEWS --- BREAKING NEWS ---
The "Empress Nik" statue at the center of Freedom Park, Baton was bombed minutes ago by an unknown person. Three people are dead, Five are injured, two of which are in critical condition.
The Orwell has detected several persons of interest and the area is under investigation. General Stevie from the Bureau of Investigation has placed the entire city of Baton on high alert.
--- BREAKING NEWS --- BREAKING NEWS ---""")

time.sleep(5)

# Stage One
print("Stage One: Initial Data")

# Gives case prompt
symes.new_case()

# First person of interest
orwell.person_of_interest('Ray')
suspect1_info()

time.sleep(5)

# Things picked up by Orwell on suspect 1
orwell.new_info()
print("Ray's YSpace Account - Recent Status Update - \" Explosions are fun and games until someone gets hurt.\"")
time.sleep(2)
print(("Ray's YSpace Account - Recent Status Update - \" I thought the Nation wanted to protect us, seems they have failed\""))
time.sleep(2)
print("Ray's YSpace Account - Recent Status Update - \" What an unfortunate series of events, Wish it was me instead\"")

time.sleep(5)

symes.check_point1()

time.sleep(15)

proceed = input("Would you like to move on to next suspect?")
if proceed == 'no':
    orwell.new_info()
    print ("""File - Patient: Arayza, Ray
    Ray Arayza was admitted on 7 September 2013 with paranoia and several other mental illnesses
    Ray Arayza was released 20 April 2014
    2016 was a rough year for Ray Arayza, she proved to be a danger to herself and others and was admitted once again on 4 May 2016.
    Her most recent release was on 30 November 2017 after serious examining and testing""")
    time.sleep(15)
else:
    time.sleep(2)

# Second person of interest
orwell.person_of_interest('Rena')
suspect2_info()

#Things picked up Orwell on suspect 2
orwell.new_info()
print("Call opening between Rena and Unknown")
print(""" Unknown: Hey, you okay? - Rena: For now, my trolley left before the explosion.
Unknown:Thats good, I know you take the trolley there everyday - Rena: Yea and I've been concerned ever since the incident
Rena: I got in so much hot water with the protest thing - Unkown: Sorry I dragged you into that, I didnt expect that response from the police
Rena: No, it was my own fault Kaylee. But its best i lay low, expecially after this - Unknown: Good Luck with that... """)
print("End Call")
proceed = input("Would you like to move on to next suspect?")
if proceed == 'no':
    orwell.new_info()
    print (""" The Nation Herald \'Protest in Freedom Park\' dated two months ago -- Protests in Freedom Park last night resulted in many arrests.
    Protestors gathered there in Freedom Park,Baton in protest of increased surveillance announced by the Intelligance Agency. Most notably several
    protestors were arrested for assualt of police peace keepers. A crazed young lady threw her shoes off at the head of a police officer giving him
    a concussion, the young lady proceeded to stomp about in the fountain and yell about freedom until she was detained. """)
    time.sleep(15)
else:
    time.sleep(2)

print("End Stage One")

