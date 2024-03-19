from datetime import datetime

# Nhập ngày tháng năm sinh
ngay_sinh = input("Nhập ngày tháng năm sinh (yyyy-mm-dd): ")

# Tính tuổi
tuoi = datetime.now().year - datetime.strptime(ngay_sinh, '%Y-%m-%d').year

print("Tuổi của bạn là:", tuoi)

from datetime import datetime
ngay_sinh = input("Nhap ngay thang nam sinh (yyyy-mm-dd): ")
tuoi = datetime.now().year - datetime.strptime(ngay_sinh, '%Y-%m-%d').year
print("Tuoi cua ban la : ", tuoi)