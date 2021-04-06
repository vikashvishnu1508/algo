class company1:
    cars_manuf = 100
    def x(self):
        company1.cars_manuf = 150

class company2(company1):
    cars_manuf = 1000
    def x(self):
        print(company2.cars_manuf * company1.cars_manuf)

class company3(company1):
    def x(self):
        cars_manuf = 10

class Partner(company2, company3):
    def x(self):
        partner_car_val = company2.cars_manuf / company3.cars_manuf
        return partner_car_val

obj = Partner()
a = obj.x()
print(a)

