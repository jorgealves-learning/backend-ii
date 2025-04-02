from typing import Protocol

class PaymentService(Protocol):
    """
    This class represents a Protocol (like an Interface in JS)
    that can be used to create new PaymentServices (representing different ways to 'pay')
    """
    def process(*args,**kwargs):
        """
        This 'raise NotImplementedError' tell us that is required to implement in subclass
        """
        raise NotImplementedError
    
class GPayService(PaymentService):
    def foo():
        """
        Wen can also implement other methods and logic if needed
        """
        pass

    def process(*args, **kwargs):
        """
        The logic for Google Pay service goes here
        """
        ...

class PayPalService(PaymentService):
    def process(*args, **kwargs):
        return "Paypal"

class ApplePayService(PaymentService):
    def process(*args, **kwargs):
        return "Apple Pay"
