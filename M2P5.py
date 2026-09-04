print("What is the original price?")
price = float(input())
print("Enter the percentage in decimal form (for example, 0.10 for 10%) ")
discountPercent = float(input())
discountAmount = price * discountPercent
discountedPrice = price - discountAmount
print("The Discount Amount in dollars is " + str(discountAmount))
print("The Discounted Price in dollars is " + str(discountedPrice))
