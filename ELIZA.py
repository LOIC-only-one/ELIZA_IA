#coding:utf-8;
# ELIZA is an IA, wich simulated Rogerian Psychotherapist
# Rogerian argument = recherche de terrain d'entente
from os import close
import time
import random
jeu = 0

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
import re

# Réponses prédéfinies
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
    # Recherche de correspondances
    for pattern, response in reponses.items():
        match = re.search(pattern, message)
        if match:
            # remplacement de (.*) avec la chaine capturée
            if '{}' in response:
                phrase = match.group(1)
                return response.format(phrase)
            else:
                return response

# Test de la fonction
print(reponse_eliza("hello"))
