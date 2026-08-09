score = int(input("กรุณาป้อนเกรดของคุณ: "))

if score >= 80 and score <= 100:
    print("คุณได้เกรด: A")
elif score >= 70 and score <= 79:
    print("คุณได้เกรด: B")
elif score >= 0 and score <= 69:
    print("คุณได้เกรด: F")
else:
    print("กรุณาป้อนข้อมูลใหม่ให้ถูกต้อง")