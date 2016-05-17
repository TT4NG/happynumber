def main():
	print("welcome to happy numbers, we will now begin generating happy numbers from 0-10,000")
	digit = 0
	while digit <= 1000:
		new = str(digit)
		iteration(new)
		digit += 1

def iteration(new):
	num = new
	check = set()
	while 1:
		if num == 1:
			print (new, "Happy Number!")
			break
		num = sum(int(c)**2 for c in str(num))
		if num in check:
			break
		check.add(num)
		
main()