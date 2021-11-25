#!python3
import time

def bar(N=50):
	for i in range(N+1):
		print("\r\033[K" + "[{2:{1}}] {0}/{1}".format(i, N, '#'*i), end='', flush=True)
		time.sleep(0.1) # do something
	else:
		print()


def bar_percent(N=50, length_bar=None, item_icon='#'):
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


if __name__ == '__main__':
	bar(42)
	bar_percent(100)
	bar_percent(100, length_bar=80)
