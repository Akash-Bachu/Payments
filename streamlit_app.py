import streamlit as st

pip install stripe 

import stripe
# Set your Stripe API keys
stripe.api_key = "sk_test_51OEYvDSA1BIlFWR0UQFp5kbMzNB88pEN4tuQj33CRFAVjHQClTdpMcI7TRVMm08w3N4pSw311MU6F4eOyhkaNpag00zBL9KBFb"

def upi_payment():
    st.subheader("UPI Payment")
    upi_id = st.text_input("Enter UPI ID")
    if st.button("Make UPI Payment"):
        payment_result = process_upi_payment(upi_id)
        st.write(f"Payment Result: {payment_result}")

def net_banking_payment():
    st.subheader("Net Banking Payment")
    bank_name = st.selectbox("Select Bank", ["Bank A", "Bank B", "Bank C"])
    account_number = st.text_input("Enter Account Number")
    if st.button("Make Net Banking Payment"):
        payment_result = process_net_banking_payment(bank_name, account_number)
        st.write(f"Payment Result: {payment_result}")

def debit_card_payment():
    st.subheader("Debit Card Payment")
    card_number = st.text_input("Enter Card Number")
    expiration_date = st.text_input("Expiration Date (MM/YY)")
    cvv = st.text_input("CVV")
    if st.button("Make Debit Card Payment"):
        payment_result = process_stripe_debit_card_payment(card_number, expiration_date, cvv)
        st.write(f"Payment Result: {payment_result}")

def process_upi_payment(upi_id):
    # Simulate UPI payment processing
    if upi_id:
        return "UPI Payment successful!"
    else:
        return "UPI Payment failed. Please check your information."

def process_net_banking_payment(bank_name, account_number):
    # Simulate net banking payment processing
    if bank_name and account_number:
        return "Net Banking Payment successful!"
    else:
        return "Net Banking Payment failed. Please check your information."

def process_stripe_debit_card_payment(card_number, expiration_date, cvv):
    # Use the Stripe API to process debit card payment
    try:
        charge = stripe.Charge.create(
            amount=1000,  # Amount in cents
            currency="usd",
            source=stripe.Token.create(
                card={
                    "number": card_number,
                    "exp_month": expiration_date.split("/")[0],
                    "exp_year": expiration_date.split("/")[1],
                    "cvc": cvv,
                }
            ),
            description="Debit Card Payment",
        )
        return "Debit Card Payment successful! Charge ID: {}".format(charge.id)
    except stripe.error.CardError as e:
        return f"Error: {e.error.message}"
    except stripe.error.StripeError as e:
        return f"Error: {e.error.message}"

def payment_form():
    st.title("EasyPay")

    payment_method = st.selectbox("Select Payment Method", ["UPI", "Net Banking", "Debit Card"])

    if payment_method == "UPI":
        upi_payment()
    elif payment_method == "Net Banking":
        net_banking_payment()
    elif payment_method == "Debit Card":
        debit_card_payment()

if __name__ == "__main__":
    payment_form()

