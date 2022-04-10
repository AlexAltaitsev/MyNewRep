from json.tool import main


class Armour(object):
    
    def is_penetrated(self,thickness, calibr):
        if calibr * 3 > thickness:
            bool = "yes"
            return print(bool)
        else:
            bool = "no"
            return print(bool) 


q = Armour()
q = q.is_penetrated(20,5)

if main == __name__:
    print(q)