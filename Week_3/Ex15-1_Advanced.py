class Nhanvien:
    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.__tenNhanVien = tenNhanVien
        self.__luongCoBan = luongCoBan
        self.__heSoLuong = heSoLuong
    LUONG_MAX = 20000000
    
    def tinhLuong(self):
        return self.__luongCoBan * self.__heSoLuong
    
    def tangLuong(self, luongTang):
        luongMoi = self.tinhLuong() + luongTang
        if luongMoi > Nhanvien.LUONG_MAX:
            return False
        self.__luongCoBan += luongTang
        return True
    
    def inTTin(self):
        print(f"Tên: {self.tennhanvien}")
        print(f"Tăng lương: {self.tangluong}")
        print(f"Lương cơ bản: {self.__luongCoBan}")
        print(f"Hệ số lương: {self.__heSoLuong}")
        print(f"Lương: {self.tinhLuong()}")
        
    def getName(self):
        return self.__tenNhanVien
    
    def getSalary(self):
        return self.__luongCoBan
    
    def getSC(self):
        return self.__heSoLuong
    
    
    def setName(self, name):
        self.__tenNhanVien = name
        
    def setSalary(self, salary):
        self.__luongCoBan = salary
    
    def setSC(self, SC):
        self.__heSoLuong = SC