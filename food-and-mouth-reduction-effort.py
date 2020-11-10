# import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

#Observation Dataframe - hard file not provided from Codecademy
observations = pd.read_csv('observations.csv')
print(observations.head())

#In Search of Sheep Species
species['is_sheep'] = species.common_names.apply(lambda x: True if 'Sheep' in x else False)
species_is_sheep = species[species.is_sheep] == True
print(species_is_sheep)

#Filtering Sheep Mammals because previous results included plants species
sheep_species = species[(species.is_sheep == True) & (species.category == 'Mammal')]
print(sheep_species)

sheep_observations = pd.merge(sheep_species, observations)
print(sheep_observations.head())

obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
print(obs_by_park)


#Plotting Sheep Sightings 
plt.figure(figsize=(16,4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park.park_name)), obs_by_park.observations)
ax.set_xticks(range(len(obs_by_park)))
ax.set_xticklabels(obs_by_park.park_name)
plt.xlabel('Park Names')
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')
plt.show()

#Food and Mouth Reduction Effort - Sample Size Determination
baseline = 15
minimum_detectable_effect = 100 * 5 / 15
#print(minimum_detectable_effect)

sample_size_per_variant = 890
yellowstone_weeks_observing = 890 / 507.0 #1.755 weeks
# print(yellowstone_weeks_observing)

bryce_weeks_observing = 890 / 250.0 #3.56 weeks
# print(bryce_weeks_observing)