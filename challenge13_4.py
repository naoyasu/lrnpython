class Horse():
    def __init__(self, name, bleed, rider):
        self.name = name
        self.bleed = bleed
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

tak = Rider("M demooro")
hor = Horse("operao", "kingmanbo", tak)
print(hor.rider.name)
