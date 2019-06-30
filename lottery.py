from random import randint

# 1) Calculate probability to win at cocody
tickets_number = 2517
winner_tickets = 0
cocody_win_chance = 0

def ticket_draw():
	"""Choose a ticket, and return if is winner or not"""
	
	return randint(0, 1)

# We'll simulate a draw of all cocody available tickets in order to know
# pobability of win a prize.

# Calculate probability to win in cocody.
for x in range(0, tickets_number):
	result = ticket_draw()

	if result == 1:
		winner_tickets += 1

cocody_win_chance = winner_tickets/tickets_number

# 2) Calculate other towns win chance

# Yopougon population have twice more chance than cocody population
# to win a prize
yopougon_win_chance = 1.5*cocody_win_chance

# Plateau population wins three times less than yopougon
plateau_win_chance = yopougon_win_chance/3

# Kumassi population wins four times more than plateau
kumassi_win_chance = 2.7*plateau_win_chance


# 3) Display probabilities
print(f'probability to win at cocody is: {cocody_win_chance}')
print(f'probability to win at yopougon is: {yopougon_win_chance}')
print(f'probability to win at plateau is: {plateau_win_chance}')
print(f'probability to win at kumassi is: {kumassi_win_chance}')
