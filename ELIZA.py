from os import close
import time
import random
import re

print('''

$$$$$$$$\ $$\       $$$$$$\ $$$$$$$$\  $$$$$$\  
$$  _____|$$ |      \_$$  _|\____$$  |$$  __$$\ 
$$ |      $$ |        $$ |      $$  / $$ /  $$ |
$$$$$\    $$ |        $$ |     $$  /  $$$$$$$$ |
$$  __|   $$ |        $$ |    $$  /   $$  __$$ |
$$ |      $$ |        $$ |   $$  /    $$ |  $$ |
$$$$$$$$\ $$$$$$$$\ $$$$$$\ $$$$$$$$\ $$ |  $$ |
\________|\________|\______|\________|\__|  \__|
                                                
(Rogerian Psychotherapist)                                              
''')

reponses = {
    'hello': 'Bonjour. Comment puis-je vous aider aujourd\'hui ?',
    'goodbye': 'Au revoir. J\'espère que vous avez une belle journée.',
    'thank you': 'De rien.',
    'j\'ai besoin (.*)': 'Pourquoi avez-vous besoin de {}?',
    'je veux (.*)': 'Que cela signifierait-il pour vous si vous obteniez {}?',
    'je (.*)': 'Pourquoi {}?',
    'comment (.*)':"Pourquoi voulez vous savoir cela ?",
    '.*': 'Désolé, je ne comprends pas ce que vous voulez dire.'
}

def reponse_eliza(message):
    for pattern, response in reponses.items():
        match = re.search(pattern, message)
        if match:
            if '{}' in response:
                phrase = match.group(1)
                return response.format(phrase)
            else:
                return response

# Interaction avec l'utilisateur
while True:
    message = input("> ")
    if message.lower() == "exit":
        print(reponse_eliza("goodbye"))
        break
    else:
        print(reponse_eliza(message))
