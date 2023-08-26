from datetime import datetime

def mortgage_calculator(cur_date='2023-07-09', last_date='2053-03-20', remain_amt=3659101.0, interest_rate=0.0465, payment_method='a', pre_repay_amt=500000.0):
	cur_date = datetime.strptime(cur_date, '%Y-%m-%d')
	last_date = datetime.strptime(last_date, '%Y-%m-%d')
	begin_year, end_year = cur_date.year, last_date.year
	begin_month, end_month = cur_date.month, last_date.month
	if begin_year == end_year:
		remain_month = end_month - begin_month 
	else:
		remain_month = (end_year - begin_year) * 12 + end_month - begin_month
	remain_month = float(remain_month)
	interest_rate_mth = interest_rate/12
	
	if payment_method == 'a':

		origin_monthly_pay = (remain_amt*interest_rate_mth*((1+interest_rate_mth)**remain_month))/((1+interest_rate_mth)**remain_month-1)
		origin_monthly_pay = round(origin_monthly_pay, 2)

		new_monthly_pay = ((remain_amt-pre_repay_amt)*interest_rate_mth*((1+interest_rate_mth)**remain_month))/((1+interest_rate_mth)**remain_month-1)
		new_monthly_pay = round(new_monthly_pay, 2)

	else:
		raise NotImplementError

	return remain_month, origin_monthly_pay, new_monthly_pay

remain_month, origin_monthly_pay, new_monthly_pay = mortgage_calculator(pre_repay_amt=400000)
print(remain_month)
print(origin_monthly_pay)
print(new_monthly_pay)
