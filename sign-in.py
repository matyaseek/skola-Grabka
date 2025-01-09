authorized_user = "matesgrabka"

while True:
  user_name = input("Přihlašovací jméno:", )
  if user_name == authorized_user:
    break
else:
  print("přístup odepřen, zkuste znovu")


user_password = input("Heslo:", )
authorized_pass = "1234"
if user_password == authorized_pass:
  print("výtejte v systému")
else:
  print("přístup odepřen, zkuste znovu")
 