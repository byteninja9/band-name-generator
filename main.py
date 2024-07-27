#1. Create a greeting for my program
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show the their band name.

from colorama import Fore, init as colorama_init


colorama_init(autoreset=True)

print(f"""{Fore.CYAN}
      
\    /_ | _ _ ._ _  _   | _  |_) _.._  _| |\ | _.._ _  _
 \/\/(/_|(_(_)| | |(/_  |(_) |_)(_|| |(_| | \|(_|| | |(/_
                    \n\t\t  Generator (V 0.1)
                    \n\t\t  Created By: Byte Ninja                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                             
      """)

city = input("What's name of the city you grew up in?\n")
pets = input("What's your pet's name?\n")

print(f"Your band name could be {city} {pets}")