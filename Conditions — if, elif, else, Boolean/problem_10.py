# Problem 20 — তিনটি শর্ত একসঙ্গে একটি সংখ্যা ৩ ও ৫ উভয় দিয়ে বিভাজ্য, শুধু একটির দিয়ে বিভাজ্য, নাকি কোনোটির দিয়েই নয় তা দেখাও।

number = int(input("Enter number: "))

if number % 3 == 0 and number % 5 == 0:
    print("2 tah diyei bivajjo")

elif number % 3 == 0 or number % 5 == 0:
    print("1 tah diye bivajjo")

else:
    print("akta diyeo bivajjo nah")