class SieuNhan():
    def __init__ (self, ten , vuKhi, mauSac):
        self.ten = ten
        self.vuKhi = vuKhi
        self.mauSac = mauSac
        
    def in4(self):
        print(f"Name: {self.ten}")
        print(f"Weapon: {self.vuKhi}")
        print(f"Color: {self.mauSac}")


sieu_nhan_A = SieuNhan("A", "Kiếm" , "Đỏ")
sieu_nhan_B = SieuNhan("B", "Khiên" , "Xanh")
