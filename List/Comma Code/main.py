def commaCode(lst):
	ans = ""
	for i in range(len(lst)):
		ans += str(lst[i])
		if i == len(lst) - 2:
			ans += " and "
		elif i < len(lst) - 2:
			ans += ", "
	return ans

print(commaCode(["ga", 1, 2]))