from fastapi.testclient import TestClient
from main import app

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/hackathon_group_8")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"hackathon group 8": "go through it"}


# test to check if Iris Virginica is classified correctly
def test_credit_score():
    # defining a sample payload for the testcase
    payload = {
      "Duration_in_month": 0,
      "Credit_amount": 0,
      "Installment_rate_in_percentage_of_disposable_income": 0,
      "Present_residence_since": 0,
      "Age_in_years": 0,
      "Number_of_existing_credits_at_this_bank": 0,
      "Number_of_people_being_liable_to_provide_maintenance_for": 0
    }
    with TestClient(app) as client:
        response = client.post("/credit_score", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        
