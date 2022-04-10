class Armour(object):
    
    def is_penetrated(Self, thickness, calibr):
        if calibr * 3 > thickness:
            bool = "yes"
            return print(bool)
        else:
            bool = "no"
            return print(bool) 

class HArmour(object):
    
    def is_penetrated(Self, thickness, calibr, type_ammo):
        if type_ammo == "fugas":
            if calibr * 3 > thickness * 1.2:
                bool = "yes"
                return bool
        if type_ammo == "cum":
            if calibr * 3 > thickness:
                bool = "yes"
                return bool
        if type_ammo == "subcaliber":
            if calibr * 3 > thickness * 0.7:
                bool = "yes"
                return bool
        else:
            bool = "no"
            return bool

type_in = int(input())
thickness = int(input())
calibr = int(input())
type_ammo = str(input())

def main(type_in, thickness, calibr, type_ammo):
    if type_in == 1: 
        q = Armour()
        q.is_penetrated(thickness, calibr)
        print(q)
    if type_in == 2:
        m = HArmour()
        m = m.is_penetrated(thickness, calibr, type_ammo)
        print(m)
    else:
        print("неправильные данные")

if __name__ == "__main__":
    main(type_in, thickness, calibr, type_ammo)


