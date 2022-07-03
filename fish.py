class Fish:
    def __init__(self, first_name, last_name = "Fish", skeleton = "bone", eyelids = False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim (self):
        print("The fish is swimming")

    def swim_backwards(self):
        print("The fish can swim backwards")
    
#Child classes
class Trout(Fish):
    def __init__(self, water="freshwater"):
        self.water = water
        super().__init__(self)

class ClownFish(Fish):
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone")

#Overriding parent class
class Shark(Fish):
    def __init__(self, first_name, last_name="Shark", skeleton="cartilage", eyelids=True):
        super().__init__(first_name, last_name, skeleton, eyelids)

        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        #return super().swim_backwards()
        print("The shark cannot swim backwards, but can sink backwards")
    

#Multiple inheritance
class Coral:
    def community(self):
        print("Coral lives in a communitiy")

class Anemone:
    def protect_clownfish(self):
        print("The anemone is protecting the clownfish")

class CoralReef(Coral, Anemone):
    pass


fish1 = Fish("Fish1")
print(fish1.first_name)
fish1.swim()

terry = Trout()
terry.first_name = "Terry"
print(terry.first_name)

sammy = Shark("Sammy")
print(f"{sammy.first_name} {sammy.last_name}")
sammy.swim()
sammy.swim_backwards()

great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()
