
loanamount = int(input ('Loan Amount'))
numberofyears = int (input('Number Of Years:'))
numberofmonths = numberofyears * 12
interestrate  = int(input('Interest Rate:'))
typeofloan = input ('Fixed(F) or Variable(V)')
interestratebymonth = (interestrate / 1200) 

if (typeofloan == 'F'):
	discountfactor = (((1 +interestratebymonth) ** numberofmonths ) - 1) / (interestratebymonth * (( 1 + interestratebymonth ) ** numberofmonths))	
	loanpayment = loanamount / discountfactor
else:
	
print('Loan Payment: {}'.format(loanpayment))