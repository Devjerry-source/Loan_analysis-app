#Loan--Analysis--Application
from time import sleep
import pandas as pd
import calendar
import numpy


status = False
choice = False
admin_name, admin_password, user_input, user_name, password, confirm_password, gmail, user_name1, password1 = "", "", 0, "", "", "", "", "", ""
user_details, read_more, bank_name, go_back = {}, "", "", ""
exit_kinds = ("exit", "Exit", "EXIT", "cancel", "Cancel", "CANCEL")
data = {} #this contains the table info

'''The user_details stores the User name, password and gmail provided by the User while signing up in a dictionary format
'''
'''Banks current General Loan rate as at last published
This App provides data for Eight(8) banks
'''

banks_interest_rate = {
    "FIRST BANK": 20.00 ,
    "ZENITH BANK": 15.05,
    "UBA": 24.00,
    "FIDELITY BANK": 19.00,
    "ACCESS BANK": 14.00,
    "STERLING BANK": 21.00,
    "GTB": 12.00,
    "ECOBANK": 18.00
}

def admin():
	'''this saves the admins default user name, gmail and password in the App database(User_details)
	'''
	global admin_name, admin_password, admin_gmail
	
	admin_name = "Jeremiah"
	
	admin_gmail = "ajohjerry@gmail.com"
	
	admin_password = "Jerryibk999120"
	# populating user_details
	user_details["Admin user name"] = admin_name
	user_details["Admin gmail"] = admin_gmail
	user_details["Admin Password"] = admin_password

admin( )

def my_decorator(my_func):
	def exit_wrapper():
		my_func()
		 
		if user_name in exit_kinds or password in exit_kinds or confirm_password in exit_kinds or gmail in exit_kinds or read_more in exit_kinds or user_name1 in exit_kinds or password1 in exit_kinds or read_more in exit_kinds or bank_name in exit_kinds or go_back in exit_kinds:
			exit()
	return exit_wrapper

@my_decorator #this actually decorates user_name below
def user_name_prompt( ):
	global user_name
	
	user_name = input("Username: ").title( )
	
	if user_name not in exit_kinds:
		while user_name.isalpha( ) == False or len(user_name) < 2:
			print( )
			
			print("Invalid input!", "User name should contain only alphabets and it should have more than two characters.", sep = "\n")
			
			print( )
			
			user_name = input("Username: ").title( )
						
@my_decorator #this actually decorates password below
def user_password():
	global password
	
	password= input("Password: ")
		
@my_decorator #this actually decorates confirm_password below
def confirm_password_prompt():
	global confirm_password
	
	confirm_password = input("Confirm password: ")

@my_decorator #this actually decorates gmail below
def user_gmail():
	global gmail
	
	gmail = input("G-mail Address: ").lower( )

@my_decorator #this actually decorates user_name1 below
def user_name_login():
	global user_name1
	
	user_name1 = input("User name: ").title( )
		
@my_decorator #this actually decorates password1 below
def password_login():
	global password1
	
	password1 = input("Password: ")
		
@my_decorator #this actually decorates bank_name below
def bank_name_prompt():
	global bank_name
	
	bank_name = input("Enter the name of the Bank: ").upper( )	
	
@my_decorator #this actually decorates read_more prompt below
def read_more_prompt( ):
	'''this function displays more articles when invoked by the user
	'''
	global read_more, status
	
	read_more = input("To Continue reading enter a or A or go back by entering b or B: ").lower( )
	
	if read_more not in exit_kinds:
		while read_more != "a" and read_more != "b":
			print( )
			
			print("Invalid input!", "Enter a or A", sep = "\n")
			
			print( )
			
			read_more = input("To Continue reading enter a or A: ").lower( )
			
	print(".." * 30 )
	
	if read_more == "b":
		status = False
		main()
		
		
@my_decorator
def back_to_menu( ):
	'''this alllows the user to go back to menu
	'''
	global go_back, status, choice
	
	go_back = input("To return to Menu list Enter b or B: ").lower( )
	if go_back not in exit_kinds:
		while go_back != "b":
			print( )
			
			print("Invalid input!", "Enter either b or B", sep = "\n")
			
			print( )
			
			go_back = input("To return to Menu list Enter b or B: ").lower( )
		
		print(".." * 30 )
		
		print()
	
	if go_back == "b":
		status = False
		choice = False
		main( )	
	
def total_payment( ):
	'''this calculates the simple interest on the Loan specified and returns the total amount to be paid at the end of the period
	'''
	global simple_int, principal, time, rate
	
	principal = int(loan_amount)
	
	time = int(duration)
	
	simple_int = (principal * rate * time)/ (100 * 12)
	
	total_payment = principal + simple_int
	
	print("Total Interest Paid: ", simple_int)
	
	print( )
	
	print("Total Payment: ", total_payment)

def analysis():
	'''this provides a monthly analysis of amount to be paid after loan collection and the remaining balaance unpaid in a tabular format
	'''
	global months, balance, principal, simple_int, monthly_pay, t, b, ms, mpr, mi, mp, tp, mb
		
	#time is represented by t
	t= time
	#ms represents a for loop of the numbers of months specified
	ms=(list(month for month in calendar.month_name[1: t+1]))
	#monthly principal is represented by mpr
	mpr = round(principal / t, 2)
	#monthly interest is represented by mi
	mi = round(simple_int /t, 2)
	#monthly payment of the sum of principal and interest is represented by mp
	mp = mpr + mi
	#total payment is represented by tp
	tp = principal + simple_int
	#monthly balance after deduction is represented by mp
	mb = round(tp / t, 2)
	#st represents the best after first payment
	st = round(tp - mp, 2)
	#balance is represented by b
	b = (list(y for y in numpy.arange(st, -1, -(mb))))
	
	data = {'Months':ms, "Interest": mi, "Principal":mpr,  "Balance":b}
	
	df = pd.DataFrame(data)
	
	print( )
	
	print("\tThis Table evaluates Your monthly payment starting from a default twelve months Calendar Year.\n\tThe following analysis depict a Fixed rate of Interest and Principal in practice in Banks.")
	print()
	
	print(df)	
	
def app_info( ):
	'''This function displays a background information about the Application
	'''
	print("Loan-Analysis-Application".upper().center(60,"*"))
	
	print("L.A.A.P".center(55, " "))
	
	print("Welcome to Loan Analysis Network.We are here to provide you with Informations about retail loan and other kinds of loan with a built-in Calculator and Analytical Table,to help you plan for your Loan.This App functions under the directives and requirement of the Central Bank of Nigeria(C.B.N).", "NOTE: To exit this program kindly enter 'exit' or 'Exit'. Thanks for your cooperation", sep = "\n\n")
	
	print( )
	print( )

def sign_up( ):
	'''this collects data from the user which serves as the user access to the App features
	'''
	global user_name, password, confirm_password, gmail, user_details
	
	app_info( )
	
	print("Sign-up to Create an Account")
	
	print()
	
	user_name_prompt()
		
	user_password()
	# this checks for the user's password strength
	if password not in exit_kinds:
		while len(password) < 8 or password.isalpha() == True or password.isnumeric() == True or password.islower() ==True:
			
			print("Enter a more secure password please.","Hint: Password must start with a capital letter, it must not be less than 8 characters, it must contain numbers.",sep="\n")
			
			print( )
			
			user_password()
		
	confirm_password_prompt( )
	#this checks if the passwords tally
	if confirm_password not in exit_kinds:
		while confirm_password != password:
			print( )
			
			print("Invalid input!", "Password does not match.")
			
			print( )
			
			confirm_password_prompt( )
			
	user_gmail()
	#this validates the gmail address provided
	if gmail not in exit_kinds:
		while gmail.endswith("@gmail.com") == False or len(gmail) <= len("@gmail.com"):
			print( )
			
			print("Invalid input!", "Enter a valid gmail address.", sep = "\n")
			
			print( )
			
			user_gmail()
	
	print( )
				
	print("Saved successfully", "." * 41)
	
	print("Redirecting to login site in 3secs>>>")
	#this delays the program for 3 secs
	sleep(3)
	
	print( )
	#populating user_details
	user_details["User name"] = user_name
	user_details["Email_address"] = gmail
	user_details["Password"] = password 
	
def login( ):
	'''this accepts users log in details
	'''
	global user_name1, password1, name, user_password, admin_name, admin_password, exit_kinds
	
	app_info( )
	
	print("Log into Your Account")
	
	print( )
	
	user_name_login()
	
	name= (user_details["User name"])
	
	admin_name = (user_details["Admin user name"])
	#this checks if user_name exist in user_details
	if user_name1 not in exit_kinds:
		while user_name1 != name and user_name1 != admin_name:
			
			print("Invalid User name!")
			
			print( )
			
			user_name_login()
	
	password_login()
	
	user_password = (user_details["Password"])
	admin_password = (user_details["Admin Password"])
	#this checks if password exist in user details
	if password1 not in exit_kinds:
		while password1 != user_password and password1 != admin_password:
			
			print("Invalid password!")
			
			print( )
			
			password_login()

def exist_in_data_base( ):
	'''this checks if the user has already created an account
	'''
	global user_details
	
	if len(user_details) < 6:	
	
		sign_up( )

		print( )
		
		login( )
		
		print( )
		
	elif len(user_details) == 6:
		
		login( )
		
		print( )

def main( ):
	#this provides the main features of the App
	global loan_amount, duration, rate, start_date, user_input, read_more, bank_name, status, choice, go_back
	
	print("Choose an Option below",
	    "1) CBN Lending Policy",
	    "2) Loan Calculator/Analysis",
	    sep = "\n" )
	
	print( )
	#this handles ValueError for user_input
	while status == False:
		try:
			user_input = int(input("Please Enter either 1 or 2 to select from above: "))
			if user_input == 1 or user_input == 2:
				status = True
			else:
				raise ValueError 
		except:
			print()
			
			print("invalid input!")
			
			print()
		
	if user_input == 1 :
		print( )
		
		print("Loans and access to credit facilities".upper( ))
		
		print( )
		
		print("All you need to know about Loan".title(),"\n01.Introduction\n\nA loan is usually an amount of money given to an individual or an institution on the condition that it will be repaid on a later date, with or without interest.Other assets such as land,machinery and buildings can also be given out as loans.\nIn most loan arrangements,the following are involved:\ni.Principal -The amount of money loaned or borrowed.\n\nii.Interest Rate -A rate charged or paid for the use of money borrowed.An interest rate is usually expressed as an annual percentage of the principal.It is calculated by multiplying the rate of interest by the principal.For example, if a lender (such as a bank) charges a customer 20% interest in a year (per annum) on a loan of N1,000,000 then the interest to be paid would be N1,000,000 X 20/100 X 1year = N200,000 (per annum)\n\niii.Date of Repayment -The date on which the principal and interest must be returned.\nHowever,there are financial institutions that offer non-interest loans.But they share in the profit of the business for which the loan is granted.\n\nThings to consider when taking a loan:\n\nAn individual or company should consider:\n•The purpose for the loan\n•The loan amount required.\n•The ability to pay principal and interest over the repayment period.\n•The financial institution to approach.\n•The collateral (guarantee) for the loan\n•The Terms and Conditions of the loan.", sep = "\n")
		print( )
		
		read_more_prompt( )
		
		print( )
		
		print("02. Types of Loan\n\nThere are two major types of loan:\na)Secured Loan\n\nA Secured Loan is a loan in which the borrower pledges assets (eg property, movable assets, etc) as collateral (guarantee) for the loan. The assets are always worth more than the amount of the loan, and can be claimed by the lender if the borrower does not pay back the money according to agreed terms and conditions.\nSecured Loans include:\n•Term Loan - This is a loan granted by banks and other financial institutions for a specific amount and repayment terms, as well as a fixed or fluctuating interest rate.\n\n•Mortgage Loan-This is a loan granted by banks and other financial institutions for the purchase of real estate (property) usually with specified interest rate and repayment period.It is secured by the property itself.Ownership of the property is transferred to the borrower after full repayment and meeting other obligations.A default will lead to foreclosure(seizing of the property).\n\nb)Unsecured Loan\n\nAn Unsecured Loan Saloon In which the borrower does not pledge an asset as collateral (guarantee) for the loan.This type of loan has more risks for lenders, hence the interest rates are usually higher than secured loans.\nUnsecured Loans include:\n•Credit Card Loan -An electronic card,usually issued by banks and other financial institutions, which allows the holder to spend an amount above his account balance,but up to an agreed limit Regular checks and reconciliations are carried out at intervals to balance the account and claim interests,charges and principal according to the terms and conditions.\n\n•Personal Loan -This is a loan granted to an individual for household or other personal use.Banks and other financial institutions give out these loans based on the borrower's credit history and ability to repay the loan from personal income.It is also referred to as consumer loan.\n\n03.Banks and Other Financial Institutions\n\nBanks and other financial institutions are licensed by the Central Bank of Nigeria to grant loans. Customers of these institutions can have access to these facilities.\n\nCo-operative Societies:A Co-operative Society is a group of people who pool funds together to provide loans to their members under certain terms and conditions.\n\nTerms and Conditions for Assessing a Loan\nThese are general and specific requirements that form important parts of a loan agreement. Whatever the type of loan, Terms and Conditions are very important.\nBorrowers must fully understand these Terms and Conditions before signing up for the loan.The Central Bank of Nigeria sets guidelines and policies to regulate lending by banks and other financial institutions. Always refer to the CBN's Guide to Bank Charges (GBC) and Monetary Policy Circular\n\n04. Types of Collateral\n\nCollaterals can be classified into conventional and movable\nConventional Collaterals:These are the traditional assets accepted by banks and other financial institutions as collateral (guarantees) for loans.\nThese include:\n•Landed Property\n•Plant and Machinery\n•Stocks and Bonds\n\nMovable Collaterals:With the introduction of the Collateral Registry Regulations by the Central Bank of Nigeria in September 2014.Movable assets are now accepted as securities for loans\nThese include:\n•Auto\n•Livestock\n•Inventory\n•Farm Produce")
		
		print( )
		
		read_more_prompt( )
		
		print( )
		
		print("05.Eligibility for Loans\n\nTo be considered eligible for loans, the borrower must:\n\n•Have a bank account\n\n•Be mentally fit\n\n•Be of legal age\n\n•Be credible\n\n•Have good credit rating\n\n•Meet Know Your Customer (KYC) requirement\n\n•Be able to repay\n\n06.Repayment of Loans, Defaults and Consequences\nRepayment Of Loans: \n\nWhen a borrower fulfils all the requirements of the loan agreement and repays the principal,interest and all charges on the loan,the borrower is said to be discharged of all liabilities and the loan is considered repaid.For secured loans, all collaterals pledged would be released to the borrower.Naturally, such smooth and peaceful relationship will make the lender want to do business again with that borrower.\n\nOn the other hand,if a borrower is unable to meet the repayment obligation, the borrower can request for the loan to be restructured.The loan agreement can run under the adjusted terms.\n\nDefaults and Consequences:\nWhere a borrower fails to meet the terms and conditions of the loan, the following are consequences of the default:\n\n•Loss of collateral\n\n•Naming and shaming\n\n•Poor credit rating\n\n•Prosecution under the law\n\n•Loss of business. etc")
		
		print( )
		
		back_to_menu( )
		
					
	if user_input == 2:
		
		print("\tWelcome to Loan Calculator & Analysis", "The Bank Rates available are First Bank, Zenith Bank, UBA, GTB, Access Bank, Fidelity Bank, Ecobank and Sterling Bank. ", "\nNote: The Calculation is based on a Fixed rate of interest and Analysis is restricted to 12 month period.", sep= "\n")
		
		print( )
		
		bank_name_prompt()
		
		while bank_name not in banks_interest_rate:
			print( )
			
			print("Input result Not Found.")
			
			print( )
			
			bank_name_prompt()
		
		print( )
		
		loan_amount = input("Loan amount : ")
		
		while loan_amount.isalpha( ) ==  True or loan_amount.isnumeric() == False:
			print( )
			
			print("Invalid value!", "Hint: Values must be in figures", sep = "\n")
			
			print( )
			
			loan_amount = input("Loan amount : ")
		
		rate = banks_interest_rate[bank_name]
		
		print("Int.Rate (Yearly): ", rate)
		#this handles ValueError for duration
		while choice == False:
			try:
				duration = int(input("Duration (Month): "))
				if duration <= 12:
					choice = True
				else:
					raise ValueError
			except:
				print( )
				
				print("Invalid input!", "Enter a duration of Twelve (12) months or below.", sep = "\n")
				
				print( )
				
		total_payment( )
		
		analysis()
		
		print()
		
		back_to_menu()

'''MAIN FUNCTION INVOCATION
'''
exist_in_data_base( )
main( )