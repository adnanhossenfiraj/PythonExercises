# Problem 38 — শব্দ উল্টানো একটি string-এর character উল্টাও এবং আলাদাভাবে বাক্যের word-এর ক্রম উল্টাও।


string = "Learning Python is Fun! Today is Saturday, and we are coding together."
splite = string.split()

# invart_char = ""
# for i in splite:
#     invartWord = i[::-1]
#     invart_char += (invartWord + " ")

# print(invart_char)



invart_char = string[::-1]
print(invart_char)


invart_word = splite[::-1]
print(" ".join(invart_word))