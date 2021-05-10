from typing import Callable, List


def factorial(n: int) -> int:
	if n < 0:
		raise ValueError("Factorial() doesn't work for values less than 1.")
	if n == 0:
        	return 1
	return n * factorial(n-1)


def map_fun_list(func: Callable, l: List[int]) -> List[int]:
	return[func(value) for value in l]


print(map_fun_list(factorial, [1,2,3,4,5]))
