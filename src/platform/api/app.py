from fastapi import FastAPI, Body

from src.platform.serving.churn_serving import ChurnServer
from src.platform.serving.invoice_fraud_serving import FraudServer
from src.platform.serving.late_payment_serving import LatePaymentServer

app = FastAPI(title="Risk ML Platform")

churn_server = ChurnServer()
fraud_server = FraudServer()
late_payment_server = LatePaymentServer()


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/predict/churn")
def churn(records: list = Body(...)):
    return churn_server.predict(records)


@app.post("/predict/invoice_fraud")
def fraud(records: list = Body(...)):
    return fraud_server.predict(records)


@app.post("/predict/late_payment")
def late_payment(records: list = Body(...)):
    return late_payment_server.predict(records)