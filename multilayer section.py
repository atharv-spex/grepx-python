# --- 1. DATA (5 Rows, 3 Columns) ---
# Columns: Item Name, Quantity, Price
i1, q1, p1 = "Apples", 5, 0.60
i2, q2, p2 = "Bread", 2, 2.50
i3, q3, p3 = "Milk", 1, 1.80
i4, q4, p4 = "Eggs", 1, 3.20
i5, q5, p5 = "Rice", 2, 4.00

# --- 2. CALCULATION ---
total = (q1*p1) + (q2*p2) + (q3*p3) + (q4*p4) + (q5*p5)

# --- 3. THE REPORT ---

# SECTION 1: HEADER
print("=" * 35)
print("       SUPERMARKET RECEIPT       ")
print(f" Date: 05-April-2026")
print("=" * 35)

# SECTION 2: BODY TABLE
# We use :< to add padding (spacing) to the right of the text
print(f"{'ITEM':<15} {'QTY':<8} {'PRICE':<10}") 
print("-" * 35)
print(f"{i1:<15} {q1:<8} ${p1:.2f}")
print(f"{i2:<15} {q2:<8} ${p2:.2f}")
print(f"{i3:<15} {q3:<8} ${p3:.2f}")
print(f"{i4:<15} {q4:<8} ${p4:.2f}")
print(f"{i5:<15} {q5:<8} ${p5:.2f}")

# SECTION 3: FOOTER
print("-" * 35)
print(f"{'TOTAL AMOUNT:':<23} ${total:.2f}")
print("=" * 35)
print("    THANK YOU FOR SHOPPING!    ")