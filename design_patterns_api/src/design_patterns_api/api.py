from fastapi import FastAPI
from design_patterns_api.payments import PaymentService, PaymentGateway

api = FastAPI()


@api.get("/")
def index():
    return "Hello"

@api.post("/pay")
def process_payment(method:str):
    # the goal here is to return the proper PaymentService 
    # accordingly with the provided method
    payment_service: PaymentService = PaymentGateway.build(method=method)
    # Then we call 'process' method (which is common in all PaymentServices extended objects)
    return payment_service.process()
            