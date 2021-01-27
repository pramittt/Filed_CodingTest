# PremiumPaymentGateway
def PremiumPaymentGateway(data):
    try:
        return {
            "success": True,
            "message": 'Payment Details Sent Successfully'
        }
    except:
        return {
            "success": False,
            "message": 'Payment Unsuccessful'
        }


# ExpensivePaymentGateway
def ExpensivePaymentGateway(data):
    try:
        return {
            "success": True,
            "message": 'Payment Details Sent Successfully'
        }
    except:
        return {
            "success": False,
            "message": 'Payment Unsuccessful'
        }


# CheapPaymentGateway
def CheapPaymentGateway(data):
    try:
        return {
            "success": True,
            "message": 'Payment Details Sent Successfully'
        }
    except:
        return {
            "success": False,
            "message": 'Payment Unsuccessful'
        }
