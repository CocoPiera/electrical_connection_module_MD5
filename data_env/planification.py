import pandas
from infrastructure import Infrastructure
from building import Building

class Planification:
	def __init__(self, csv_path):
		pass

	def prepare_data(self):
		network_df = pandas.read_csv("self.csv_path")
		network_df = network_df[network_df["infra_type"] == "a_remplacer" ]

		dict_infra = {}
		list_building = []
		list_infra = []
  
		infra_sudfs = network_df.groupby("infra_id")
  
		for infra_id, infra_sudf in infra_sudfs:
			length = infra_sudf["length"].iloc[0]
			infra_type = infra_sudf["type"].iloc[0]
			nb_houses = (infra_sudf["nb_houses"].sum())
   
		dict_infra[infra_id] = Infrastructure(infra_id, length, infra_type, nb_houses)
  
      	building_sudfs = network_df.groupby("id_batiment")
       
       for id_building, building_sudfs["infra_id"]:
            list_infra.append(dict_infra[infra_id])
		
  
	def run_planification_algo(self):
		pass

if __name__ == "__main__":
    csv_path = "/Users/colinepiera/bureau/MD5/cours_MD5/network_df"
	planification_object = Planification()
	planification_object.prepare_data()
	planification_object.run_planification_algo()
 
 