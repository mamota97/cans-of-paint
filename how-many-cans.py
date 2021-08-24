'''Make a program for a paint shop. The program should ask for the size in square meters
of the area to be painted. Consider that the ink coverage is 1 liter for each
3 square meters and that the paint is sold in 18 liter cans, which cost R$ 80.00.
Inform the user of the quantities of paint cans to be purchased and the total price.'''

one_liter = 3 #1liter for each 3m²
one_can = 18 #18 liters in one can
meters = float(input("how many square meters are you going to paint? "))
how_many_cans = meters / (one_liter * one_can)
if how_many_cans > 1:
    how_many_cans +=1
    print("You'll need %d cans, total price: R$%.2f"%(how_many_cans, how_many_cans*80))
else:
    print("You'll need 1 can, total price R$80.00")

