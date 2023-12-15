#Remove all folders in a specific sub-directory that are empty

import os
from os import path
import shutil

folders = []
path = ""
Sep = "\\"

for folder in folders: 
	print(folder)
	for fname in os.listdir(folder):
		if fname.endswith('.ncs'):
			print(folder + 'has data')
			pass
		else:
			os.rmdir(folder)
	#os.remove(folder + Sep + "eeglist_coherence.xlsx")
	#shutil.rmtree(folder + Sep + "Coherence_SLMref_081222")
			print('Files deleted!')
