#!python3
# -*- coding: utf-8 -*-
import time

dict_fill = {
	'square_filled': '█',
	'hashtag': '#'
}

def bar(N=50):
	for i in range(N+1):
		print("\r\033[K" + "|{2:{1}}| {0}/{1}".format(i, N, dict_fill['hashtag'] * i), end='', flush=True)
		time.sleep(0.1) # do something
	else:
		print()


def bar_percent(N=50, length_bar=None, item_icon=dict_fill['square_filled']):
	hashtag_i_multiplier = length_bar or N # to have the good number of item_icon in the progress bar
	length_bar = length_bar or N
	for i in range(N+1):
		print("\r\033[K" + "[{2:{1}}] {0:5.1f} %".format(	i * 100 / N, 
															length_bar,
															item_icon * int(i * hashtag_i_multiplier / N)
														), end='', flush=True)
		time.sleep(0.05) # do something
	else:
		print()

class ProgressBar:
	""""""

	def __init__(self, 
				max_iteration, 
				prefix = '',
				suffix = '',
				decimals = 1,
				fixed = True,
				length = 80,
				fill = '█'):
		"""Create a progressbar object and print the initial bar
		@params:
			max_iteration   - Required[int] : total iterations
			prefix          - Optional[str] : prefix string
			suffix          - Optional[str] : suffix string
			decimals        - Optional[int] : positive number of decimals in percent complete
			fixed           - Optional[bool]: booleen that indicate if the length depend of max_iteration
			length          - Optional[int] : character length of bar
			fill            - Optional[str] : bar fill character
		"""
		self.iteration = 0
		self.max_iteration = max_iteration
		self.prefix = prefix + ' ' if prefix else prefix
		self.suffix = suffix
		self.decimals = decimals
		self.length = length if fixed else max_iteration
		self.fill = fill
		self.update()
		time.sleep(0.1)

	def update(self, increment = 1):
		"""Update and print the progressbar
		@params:
		    increment   - Optional[str] : the number of iteration to skip
		"""
		bar_prefix = "\r\033[K"
		bar = self.fill * int(self.iteration * self.length / self.max_iteration)
		counter = self.iteration * 100 / self.max_iteration
		print(bar_prefix + f"{self.prefix}|{bar:{self.length}}| {counter:5.{self.decimals}f}% {self.suffix}", end='', flush=True)
		if self.iteration == self.max_iteration:
			print()
		self.iteration += increment

	def finish(self):
		"""Lint the progressbar if it ends earlier than expected"""
		print()



if __name__ == '__main__':
	print("EXAMPLE:")

	test_nb = 0b00000111

	if test_nb & (1 << 1):
		N = 42
		print(f"\nbar({N})")
		bar(N)

	if test_nb & (1 << 2):
		N = 100
		print(f"\nbar_percent({N})")
		bar_percent(100)

		print(f"\nbar_percent({N}), length_bar=80, item_icon='-'")
		bar_percent(100, length_bar=80, item_icon='-')

	if test_nb & (1 << 3):
		N = 100
		prefix = 'Progress:'
		suffix = 'Complete'
		print(f"\nProgressBar({N}, prefix='{prefix}', suffix='{suffix}')")
		bar = ProgressBar(N, prefix=prefix, suffix=suffix)
		for i in range(N):
			time.sleep(0.1)  # DO SOMETHING
			bar.update()

	print("\nFINISH")
