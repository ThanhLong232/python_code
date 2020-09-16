#BT5: Viết chương trình nhập 2 chữ số xuất ra hàng đơn vị và hàng chục
l=int(input("Nhập hai chữ số: "))
hc=l//10
dv=l%10
print(f"Hàng chục: {hc}\nHàng dơn vị: {dv}")