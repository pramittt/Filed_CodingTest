import requests

testCases = [
    {
        'TestCase' : 'Valid Check',
        'CreditCardNumber' : '379354508162306',
        'CardHolder' : 'Steve Smith',
        'ExpirationDate' : '2022-12-09',
        'Amount' : 20.0,
        'SecurityCode' : '123' 
    },
    {
        'TestCase' : 'Credit Card Check',
        'CreditCardNumber' : '4388576018402626',
        'CardHolder' : 'Tom',
        'ExpirationDate' : '2025-12-16',
        'Amount' : 20.0,
        'SecurityCode' : '123' 
    },
    {
        'TestCase' : 'Amount Check',
        'CreditCardNumber' : '4539774507799684',
        'CardHolder' : 'Andre',
        'ExpirationDate' : '2022-12-21',
        'Amount' : -20.0,
        'SecurityCode' : '123' 
    },
    {
        'TestCase' : 'Old Expiry Date Check',
        'CreditCardNumber' : '4539774507799684',
        'CardHolder' : 'John',
        'ExpirationDate' : '2020-01-18',
        'Amount' : 20.0,
        'SecurityCode' : '123' 
    },
    {
        'TestCase' : 'Security Code extra number Check',
        'CreditCardNumber' : '4539774507799684',
        'CardHolder' : 'John',
        'ExpirationDate' : '2022-12-20',
        'Amount' : 20.0,
        'SecurityCode' : '1234' 
    },
    {
        'TestCase' : 'Security Code alphanumeric Check',
        'CreditCardNumber' : '4539774507799684',
        'CardHolder' : 'John',
        'ExpirationDate' : '2022-12-15',
        'Amount' : 20.0,
        'SecurityCode' : '12a' 
    },
    {
        'TestCase' : 'Date value given as string Check',
        'CreditCardNumber' : '4539774507799684',
        'CardHolder' : 'John',
        'ExpirationDate' : 'date',
        'Amount' : 20.0,
        'SecurityCode' : '123' 
    },
    {
        'TestCase' : 'Processing gateway based on Amount Check',
        'CreditCardNumber' : '4539774507799684',
        'CardHolder' : 'John',
        'ExpirationDate' : '2019-02-21',
        'Amount' : 500.0,
        'SecurityCode' : '123' 
    },
    {
        'TestCase' : 'Card holder name Check',
        'CreditCardNumber' : '4539774507799684',
        'CardHolder' : '122424',
        'ExpirationDate' : '2019-02-18',
        'Amount' : 500.0,
        'SecurityCode' : 'a12' 
    },
    {
        'TestCase' : 'Card holder name Check with non letters',
        'CreditCardNumber' : '4539774507799684',
        'CardHolder' : '$%^&',
        'ExpirationDate' : '2019-02-10',
        'Amount' : 500.0,
        'SecurityCode' : 'a12' 
    },
    {
        'TestCase' : 'Zero Amount Check',
        'CreditCardNumber' : '4539774507799684',
        'CardHolder' : 'John',
        'ExpirationDate' : '2019-02-10',
        'Amount' : 00.0,
        'SecurityCode' : '123' 
    },
    {
        'TestCase' : 'Retry Payment Check',
        'CreditCardNumber' : '4539774507799684',
        'CardHolder' : 'John',
        'ExpirationDate' : '2025-02-10',
        'Amount' : 1500.0,
        'SecurityCode' : '123' 
    }

]

def ExecuteTestCases():
	for TestCase in testCases:
		response = requests.post('http://127.0.0.1:5000/payment', data=TestCase)
		print("TestCase :",TestCase['TestCase'],"\n| Status Code -", response.status_code,"\n")
	return

if __name__ == "__main__":
	ExecuteTestCases()