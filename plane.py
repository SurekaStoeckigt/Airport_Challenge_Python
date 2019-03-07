class Plane():

    def __init__(self):
        self.isFlying = True

#giving Plane class plane attribute
    def setUp(self):
        self.plane = Plane()
        # self.airport = ""

    def land(self):
        self.isFlying = False
        # self.airport = airport
    #
    def take_off(self):
        if self.isFlying == True:
            raise Exception('Plane cannot takeoff while flying')
        else:
            self.isFlying = True
    # def is_at_airport(self):
    #     return self.__at_airport
