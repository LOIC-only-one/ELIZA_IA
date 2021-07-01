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
user_name = input(str("What's yout name ? "))
print("\n")
eliza_welcome = "Hello "+user_name+" I'm ELIZA, I'm here to help yu!\nWhat's wrong ?\n"
print(eliza_welcome)

li_0 = ['sorry','Sorry', 'homesick', 'gloomy', 'sad', 'unhappy', 'sob', 'hurt', 'depressed', 'depressing', 'upset', 'pain', 'sadness', 'sarrow', 'grief']
str0 = " ".join(li_0)
li_1 = ['french', 'france', 'francais', 'français', 'Paris', 'paris', 'english', 'anglais']

while jeu == 0:
	file = open('user_data.txt', "w") 
	user_answer = input(user_name+": ")
	user_answer == str
	file.write(user_answer)

	if user_answer == 'c':
		print('\nELIZA: Goodbye '+user_name)
		time.sleep(2)
		quit()

	if li_0[0] in user_answer:
		user_answer1 = user_answer
		liste_sro = ["\nELIZA: It's not cool to repeat the same thing over and over again\n",'\nELIZA: Why are you repeating '+user_answer+'\n']
		ok = random.choice(liste_sro)
		print(ok)

	
	#if li_0[2] or li_0[3] in user_answer:
		#print("\nOh no, I'm going to get a coffee and you explain to me afterwards\n") or print("\nIm going to get something to drink\n")


	#if user_answer not in str0:
		#els = ["\nELIA: This is not the subject\n","\nELIZA: I do not understand\n"]
		#elsee = random.choice(els)
		#print(elsee)
	
	file.close()