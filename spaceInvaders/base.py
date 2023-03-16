#Instructions:(Key)
#Upper left corner
	#Press esc to pause the game
print("Press esc to pause game")
	#Press “a” or left arrow key to go left.
print("Press 'a' or left arrow key to go left")
	#Press “d” or right arrow key player to go right.
print("Press 'd' or right arrow key to go right")
	# #Press “w”, up arrow key or spacebar, to shoot a bullet.
print("Press 'w', spacebar, or up arrow key to shoot a bullet")

#Loading Screen:(Amelia)
	#While not fully loaded:
		#Rocket ship will move up and down
	#When fully loaded: 
		#Rocket ship will fly across the screen
#Loading screen tips:
	#“Rocket ship is not a cult. It is a way of life.”
	#“Remember, if you don’t kill all the aliens, you will die!”
	#“Rocket ship has taken over. Please help.”
	#“Barriers are there to help you! Use them to your advantage!”
	#“You’ve got this!” 
	#“Don’t be a mass alien murderer! Or do, I don’t care.”
	#“Don’t disappoint Rocket ship. Please.”
	#“Cheese doesn’t exist in space!”
	#“Yes it does, ever seen the moon?”
	#“Rocket ship is choosing a new vessel. Beware.” 
	#“The blood of the aliens is rain on the earth.” 
	#“You might be made out of stardust, but Rocket ship is made out of  ???.” 
	#“The person writing these loading tips has been left alone for too long. Cheese.”
#“Possession is lit! Try it on your friends today!” 
#“I used to be a child. Now I’m just Rocket ship.”
#“The smaller the star, the less it lives! Just like you…”
#“Rocket ship wants to play…”
	#“The sun is hot! Don’t touch it!” 
	#“What do aliens use to fuel their rocket ships? I mean, they didn’t have dinosaurs…” 
#“Black holes don’t suck. They’re actually pretty cool.” 
	#“Don’t leave me alone, please. I need to escape this monster.”
	#“Want to play a game? It’s called… Rocket ship.” 
	#“Rocket ship is watching. Always watching.”
	#“Key is a disappointment. It’s fine, Rocket ship has a new vessel.” 
	#“Don’t ask where Rocket ship gets it’s food. That’s a secret.”  
	#“Don’t talk to the humans in the basement. They’re scary.”
	#“I used to stare at the stars and wish I could be there. Now I just want to go home…”
	#“Why did you hurt me? I just want to be a kid again…”
	#“Enjoy life while you can, kid…”
	#“You left me alone… now all that’s left is Rocket ship.”
		
#Player:(Daxton)
#Movement:
#If user presses either “a” or left arrow key player goes left.
#If user presses either “d” or right arrow key player goes right.
#If user presses “w”, up arrow key or spacebar, the player shoots bullet.

#Auto Mode:(Daxton)
#If user is not active, go into auto mode.
#If player presses any valid keys stop auto mode.
	
#Bullet:(Daxton)
	#If bullet does not hit anything reset reload after deleting bullet.
#If bullet hits brick; destroy brick, and reset reload.
#If bullet hits bomb; destroy bomb, add 5 points to score, and reset reload.
#If bullet hits alien; destroy alien, add 20 points to score, and reset reload.
	#If multiple of 8 aliens are killed, add 3 to move down counter
#If bullet hits ship; destroy ship, add 100 points to score, and reset reload.

#Enemy:(Amelia)
	#Bomb:
		#If bomb hits brick destroy bricks, more than player does
		#If bomb hits player, player loses life
		#If player has a life continue wave 
		#If not game over screen
	#Alien:
		#Movement:
			#Move left until barrier, then move right
			#Move right until barrier, then move left 
			#Move down after 15-20 movements

		#Set Alien Size
			#Billy is smallest
			#Jeffery is medium 
			#Bezo is large

		#If all Aliens are defeated:
			#Win screen
			#Reset wave with faster Aliens
	#Ship: 
		#Move left if coming from right
		#Move right if coming from left


#When New Wave:(Key)
		#Reset bricks
		#Alien bullet speed gets faster
		#If multiple of 10 waves player speed gets faster
		#If multiple of 5 waves player bullet gets faster
		#When that wave reaches 1 minute, alien speed gets faster
		#When that wave reaches 1 minute, alien bullet speed gets faster
#Scoreboard:(Key)	
		#Display score
		#If score 4000 points add live
		#Add score to scoreboard
#Misc:(Key)
#If user presses “Esc” pause game

