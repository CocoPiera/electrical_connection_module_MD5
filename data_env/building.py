class Building:
    def __init__(self, id_building, lst_infras ) :
        self.id_building = id_building
        self.lst_infras = lst_infras

    def get_building_difficulty(self):
        return sum(self.lst_infras)
    
    def _lt_ (self, other_building) :
        return self.get_building_difficulty() < other_building.get_building_difficulty()