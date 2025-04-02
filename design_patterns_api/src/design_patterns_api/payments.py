

from design_patterns_api.services import ApplePayService, GPayService, PayPalService, PaymentService


class PaymentGateway:
    """
    Class responsible for returning the proper PaymentService
    """

    # This registry represents the PaymentServices extended for each payment method
    registry = {
        "paypal": PayPalService,
        "applepay": ApplePayService,
        "gpay": GPayService,
    }

    @classmethod
    def build(cls, method:str)-> PaymentService:
        """
        Returns the proper instanciated class selected by the provided 'method' argument
        """
        return cls.registry.get(method,None)()