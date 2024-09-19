class Pet:
     all = []
PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
def __init__(self,name,pet_type,owner=None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        Pet.all.append(self)
        self.pet_type = pet_type
        self.owner = owner
        


class Owner:
  def __init__(self,name):
        self.name = name
  def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
  def add_pet(self,value):
        if isinstance(value,Pet):
            value.owner = self
        else:
            raise Exception
        
  def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda x:x.name)