def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	if len(a) == len(b):
		vec_sum = [0, 0, 0]
		for i in range(len(a)):
			vec_sum[i] = a[i] + b[i]
	else:
		return -1

	return vec_sum