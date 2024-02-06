import drinks_payment

def test_check_record():
    rfid_id = 123456789

    result = drinks_payment.check_record(rfid_id)
    test = "account created"

    assert (result == test)
