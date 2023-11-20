import streamlit as st
import os

stripe_publishable_key = os.environ.get("STRIPE_KEY")

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

