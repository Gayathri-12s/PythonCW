has_account = True
email_verified = False
can_login = has_account and email_verified

user_email = "g@example.com"
print("@" in user_email)

is_email_valid = True

user_age = 17
is_age_valid= (user_age >= 18)


can_login_final = has_account and email_verified and is_email_valid and is_age_valid 

print(can_login)
print(is_email_valid)
print(can_login_final)
print(is_age_valid)
print(can_login_final)

print(has_account is True)