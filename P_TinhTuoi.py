from datetime import datetime

# Nhập ngày tháng năm sinh
ngay_sinh = input("Nhập ngày tháng năm sinh (yyyy-mm-dd): ")

# Tính tuổi
tuoi = datetime.now().year - datetime.strptime(ngay_sinh, '%Y-%m-%d').year

print("Tuổi của bạn là:", tuoi)
