
def debit(c_account):
	# check if account funds exists
	# if exists, proceed
	# debit amount from account
	# else return error
	


def stock(c_input):
	required_mny = 0
	index = -1
	for v in v_stock:
		for c in c_stock:
			if v == c:
				print(f"{c} exists"}
				index = int(v_stock[v])
				count = c_stock.count(c)
				required_mny = v_price[index] * count
				# get required_mny for c_input
				# as input to debit
	debit(c_account, required_mny)
						
			
		
			




c_account = 100
c_input = ['cola','7up','cola']
v_stock = ['cola','sprite','7up']
v_price = [20,20,10]

stock()