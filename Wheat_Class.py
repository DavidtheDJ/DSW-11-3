#David Justice
#11-16-16
#Wheat Override


from New_Crops import *

class Wheat(Crop):
    """A Wheat crop"""

    #construtor
    def __init__(self):
        #call the parent class constructor with default values for wheat
        #growth rate = 1; light need = 5; water need = 4
        super().__init__(1,5,4)
        self._type = "Wheat"

    #override frow method for subclass
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate + 1.25
            else:
                self._growth += self._growth_rate
        #increament day growing
        self._days_growing += 1
        #update the status
        self._update_status()

def main():
    #create a new potato crop
    wheat_crop = Wheat()
    print(wheat_crop.report())
    #manually grow the crop
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())

if __name__ == "__main__":
    main()
