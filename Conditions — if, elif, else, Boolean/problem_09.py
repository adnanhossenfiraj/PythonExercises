# Problem 19 — Login যাচাই একটি demo username ও password-এর সঙ্গে input তুলনা করে login success/failure দেখাও। বাস্তব password কখনো code-এ hardcode করার ঝুঁকি নোট করো।


demoUsername = "user"
demoPass = "1234"   # demo

username = input("Enter your username: ").strip()
password = input("Enter your password: ")


if demoUsername.lower() == username.lower() and demoPass == password:
    print("Login success")
else:
    print("Login failure: invalid username or password")



# কেন ঝুঁকিপূর্ণ:

#     Source code / Git repo-তে password পড়ে যায় → যে কেউ দেখে ফেলতে পারে

#     Password পরিবর্তন করতে হলে কোড edit + redeploy করতে হয়

#     একই password সব environment-এ থেকে যায়

# সঠিক পদ্ধতি (real-world):

#     Password database-এ hash করে রাখুন (bcrypt, argon2, PBKDF2)

#     Secret environment variable বা secret manager-এ রাখুন (.env, AWS Secrets Manager, Vault)

#     কখনো plaintext-এ password compare করবেন না — hash compare করুন