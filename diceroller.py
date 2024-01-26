import random
import math

l_a = {
    'attacks': 4,
    'models': 10,
    'weapon_skill': 3,
    'strength': 4,
    'ap': 1
}

l_b = {
    'models': 10,
    'toughness': 3,
    'save': 5
}

dice = 6

attack_sequence = l_a['attacks'] * l_a['models']
hit_success = l_a['weapon_skill']
wound_success = 0
if l_a['strength'] > l_b['toughness'] & l_a['strength'] < l_b['toughness'] * 2:
    wound_success = 3
save_success = l_b['save'] + l_a['ap']
unit_size = l_b['models']


runs = int(input('Enter number of simulations to run: '))
hit_total = 0
wound_total = 0
hit_mean = 0
wound_mean = 0
destroy_mean = 0
destroy_count = 0
destroy_full_count = 0

# print('Dice roll results: ')
for j in range(runs):
    for i in range(attack_sequence):
        hit_roll = random.randint(1, dice)
        if not hit_roll >= hit_success:
            continue
        wound_roll = random.randint(1, dice)
        if not wound_roll >= wound_success:
            continue
        save_roll = random.randint(1, dice)
        if not save_roll < save_success:
            continue
        destroy_count += 1
        if destroy_count == unit_size:
            destroy_full_count += 1
            # break
    destroy_mean += destroy_count
    destroy_count = 0

mean = math.floor(destroy_mean / runs)

print()
print(runs)
print(destroy_full_count)
if not destroy_full_count == 0:
    print('Chance to fully destroy unit:', 100 / (runs / destroy_full_count))
print('Mean kills: ', mean)
print('Range:', math.floor(mean/1.5), '-', math.floor(mean*1.33))
