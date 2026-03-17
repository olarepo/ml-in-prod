from fastapi import FastAPI, Body

from src.platform.serving.churn_serving import predict_churn
from src.platform.serving.invoice_fraud_serving import predict_invoice_fraud
from src.platform.serving.late_payment_serving import predict_late_payment


app = FastAPI(title="Risk ML Platform")


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/predict/churn")
def churn_predict(records: list = Body(...), version: int | None = None):
    return predict_churn(records, version=version)


@app.post("/predict/invoice_fraud")
def fraud_predict(records: list = Body(...), version: int | None = None):
    return predict_invoice_fraud(records, version=version)


@app.post("/predict/late_payment")
def late_payment_predict(records: list = Body(...), version: int | None = None):
    return predict_late_payment(records, version=version)