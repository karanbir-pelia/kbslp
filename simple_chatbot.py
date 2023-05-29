from os import system

import time


def q_n_a(category):
    while True:

        print("\nHow can I help you?\n")

        for i in range(len(category)):
            print(f"{i + 1}. {list(category.keys())[i]}")

        choice = input("\nEnter your choice : ")

        if choice.isdigit() and int(choice) in range(1, len(category) + 1):
            print(f"\n{category[list(category.keys())[int(choice) - 1]]}")

            while choice not in ["Y", "N"]:
                choice = input("\nDo you want to continue?\n Y or N: ").upper()

            if choice == "Y":
                break
            else:
                print("\n\nHope we were able to help you. Goodbye!\n\n")
                exit()
        else:
            system("clear")
            print("\nInvalid entry!")

    system("clear")


categories = ["Orders", "Cancellations and Returns", "Payment", "Quit"]

orders = {
    "I missed the delivery of my order today. What should I do?": "The courier service delivering your order usually tries to deliver on the next business day in case you miss a delivery.",
    "Will the delivery be tried again if I'm not able to collect my order the first time?": "Couriers make sure that the delivery is re-attempted the next working day if you can't collect your order the first time.",
    "The delivery of my order is delayed. What should I do?": "On the rare occasion that your order is delayed, a new delivery timeframe will be shared with you."
}

canc_return = {
    "If I request for a replacement, when will I get it?": "In most cases, the replacement item is delivered to you at the time of pick-up.",
    "Can items be returned after the time period mentioned in the seller's Returns Policy?": "No, sellers will not be able to accept returns after the time period mentioned in the seller's Returns Policy.",
    "I see the 'Cancel' button but I can't click on it. Why?": "A greyed out and disabled 'Cancel' button means that the item has been delivered already."
}

payment = {
    "How can I order for large quantities of the product as part of a corporate order?": "You can place a bulk order by contacting our Customer Support team.",
    "How can I pay for my order?": "You can pay for your order using any of the following payment methods:\n1. Credit Card\n2. Debit Card\n3. Net Banking\n4. UPI\n5. EMI\n6. Cash on Delivery",
    "How do we prevent card fraud?": "We use the latest technology to ensure that your card details are safe."
}

date_time = time.ctime().split()

system("clear")

proceed = True

if 6 < int(date_time[3][:2]) < 12:
    print("\nGood Morning!\nHope you are doing well today.")
elif 11 < int(date_time[3][:2]) < 18:
    print("\nGood Afternoon!\nHope you are doing well.")
elif 17 < int(date_time[3][:2]) < 21:
    print("\nGood Evening!\nHope you had a great day.")
else:
    proceed = False
    print("\n\nSorry, we don't operate during these hours.\nYou can contact us tomorrow between 7 AM and 9 PM.\n\n")

while proceed:

    print("\nI can help you with the following things:\n\nSelect a category:")

    for i in range(len(categories)):
        print(f"{i + 1}. {categories[i]}")

    choice = input("\nEnter your choice : ")

    if choice.isdigit() and int(choice) in range(1, len(categories) + 1):
        system("clear")

        if choice == "1":
            q_n_a(orders)

        elif choice == "2":
            q_n_a(canc_return)

        elif choice == "3":
            q_n_a(payment)

        elif choice == "4":
            print("\n\nHope we were able to help you. Goodbye!\n\n")
            break

    else:
        system("clear")
        print("\nInvalid entry!")
