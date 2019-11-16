import numpy as np
import random
import time
import argparse

debug = ''
characters = "abcdefghijklmnopqrsutvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+1234567890-=~`<>,.?/"
key = ''
seed = 0
parser = argparse.ArgumentParser()

def main():
	
	# set a secret message
	print('Secret you want to encode:')
	start = time.time()
	secret = input()
	
	key = init_key(len(secret))
	seed = init_seed(secret, key)
	new_key = finalize_key(secret, key, seed)
	end = time.time()
	print('Key: \'{}\''.format(new_key))
	print('Length of Key: {}'.format(len(new_key)))
	print('Seed: {}'.format(seed))
	print('Length of secret: {}'.format(len(secret)))
	print('Total time taken: {:.3f}s'.format(end-start))
	
def init_key(length):

	key = ''
	for i in range(round(length**1.3)):
		key += random.choice(characters)
		
	return key
		
def generate_seed():
	seed = random.randint(0, 2**32 - 1)
	return seed
	
def init_seed(secret, key):
	good_seed = False
	count = 0
	attempted_seeds = []
	while not good_seed:
		
		print('{}: Attempting to generate a good seed...'.format(count))
		seed = generate_seed()
		if seed not in attempted_seeds:
			attempted_seeds.append(seed)
			np.random.seed(seed)
			list = []
			compare = []
			for it in range(len(secret)):
				list.append(np.random.randint(len(key)))
				
			for it in list:
				if it not in compare:
					compare.append(it)
					
			if len(list) == len(compare):
				return seed
			count += 1
def finalize_key(secret, key, seed):
	key_list = list(key)
	np.random.seed(seed)
	for it in secret:
		key_list[np.random.randint(len(key))] = it
	return ''.join(key_list)
	
def init_test():
	print('Input seed: ')
	seed = int(input())
	print('Input length of hidden message: ')
	length = int(input())
	print('Input key: ')
	key = input()
	test(seed, key, length)

def test(seed, key, length):
	np.random.seed(seed)

	print('Decoded message: ', end='')
	for i in range(length):
		index = np.random.randint(len(key))
		print(key[index], end='')
		
parser.add_argument('-cs', action='store_true', default=False, dest='create_seed')
parser.add_argument('-test', action='store_true', default=False, dest='test')
do = parser.parse_args()

if do.create_seed:
	main()
elif do.test:
	init_test()