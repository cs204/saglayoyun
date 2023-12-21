otv = input("Приветствие: ")
if otv == "здравствуйте":
    print("$0")
elif otv.lower().startswith("з"):
    print("$20")
else:
    print("$100")