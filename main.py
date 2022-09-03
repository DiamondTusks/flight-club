import requests

sheety_post_endpoint = "https://api.sheety.co/225f0ec4563dbb435c97abff230d4e64/flightDeals/users"
sheety_post_api = ""

print("Welcome to the Diamond Tusks Flight Club")
print("We find the best flight deals and email them to you!")

email_verified = False
while not email_verified:
  first_name = input("Enter your first name: ").title()
  last_name = input("Enter you lastname: ").title()
  email = input("Enter your email: ")
  email_verify = input("Enter you email again to verify: ")
  if email == email_verify:
    email_verified = True
  else:
    print("Email doesnt match. Try again.")

new_user = {
  "user": {
    "firstName": first_name,
    "lastName": last_name,
    "email": email,
  }
}
  

sheet_headers = {"Authorization": "Bearer fhgt475fhdhs383djd"}
sheet_response = requests.post(url=sheety_post_endpoint, json=new_user, headers=sheet_headers)
print(f"Welcome to the club {first_name}! Look forward to some flight deals.")