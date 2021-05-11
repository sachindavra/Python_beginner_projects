"""you will have to enter length & width in the form of n & m \
you must enter m as 3 time of n. Example is given below.
n = 7
m = 21
you will have to enter both the integer in one line with space seperated.
"""

def mat(n, m):
	for i in range(1, n, 2):
		print(('.|.'*i).center(m, '-'))
	print('WELCOME'.center(m,'-'))
	for j in reversed(range(1, n, 2)):
        	print(('.|.'*j).center(m, '-'))

if __name__ == "__main__":
	n, m = map(int, input().split())
	mat(n, m)
