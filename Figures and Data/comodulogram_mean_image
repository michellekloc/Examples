#  This simple descriptive analysis was designed to generate mean 2-D heatmaps of comodulation data for representative figures for visualization of the mean data. This was broken down into means for each structure recorded during session recorded from each individual animal subject. This is important to determine how the phenomenon of comodulation changes throughout the regions of the brain we are recording from across groups and sessions. These images were also be used as representative figures for the published manuscript. This is not 100% PEP8 compliant, but is a reasonable example of my daily work.

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#need to make sure all data was generated


def check_comodulogram_files(top_folder):
    expected_files = [f'Comodulogram_{i}.csv' for i in range(1, 33)]

    complete_dataset = []
    incomplete_dataset = [] # should be empty, if it has any folders this must be carefully investigated. All data is analyzed iteratively. This analysis was generated using pre-written code by Adriano Tort, I did not write the comodulogram code. 

    for subfol in os.listdir(top_folder):
        folder_path = os.path.join(top_folder, subfol)
        if os.path.isdir(folder_path):
            missing_files = [file for file in expected_files if not os.path.exists(os.path.join(folder_path, file))]
            if not missing_files:
                complete_dataset.append(folder_path)
            else:
                incomplete_dataset.append(folder_path)

    return complete_dataset, incomplete_dataset

top_folder_path = "PATH"
complete_dataset, incomplete_dataset = check_comodulogram_files(top_folder_path)

if incomplete_dataset:
    raise ValueError("Warning, check your data! There are folders in the incomplete list.")

# This is designed to iterate over 100s of folders, which I autogenerate as a list above. All analysis is done iteratively so this should all be the same

OFC_left = [f'Comodulogram_{x}.csv' for x in range(1, 9)]
DMS_left=[f'Comodulogram_{x}.csv' for x in range(9, 17)]
OFC_right=[f'Comodulogram_{x}.csv' for x in range(17, 25)]
DMS_right=[f'Comodulogram_{x}.csv' for x in range(25, 33)]

structure_list = [OFC_left, DMS_left, OFC_right, DMS_right]

Sep = "\\"

for folder in complete_dataset:
    for structure in structure_list: 
        for file in structure:
            df_list = []
            df = pd.DataFrame()
            if os.path.isfile(folder + Sep + file) and os.path.exists(folder + Sep + file):
                print(folder + Sep + file)
                df1 = pd.read_csv(folder + Sep + file, header = None)
                # print(df)
                df2 = df1.mean(axis = 0)
                # print(df2)
            df_list.append(df2)
            df = pd.concat(df_list)
            df.to_excel("C:\\Users\\Administrator\\Desktop\\OFCleft_Mean.xlsx", header = False, index = False)
        
            plt.figure(figsize=(8, 6))
            x_axis_labels = list(range(1, 27))
            y_axis_labels = list(range(25, 201, 25))
            # call seasborn to generate heatmap
            sns.heatmap(df, annot=True, fmt = 'd', cmap = 'jet', linewidths=.5, cbar_kws = {'label': 'R.U.'}, xticklabels = x_axis_labels, yticklabels = y_axis_labels)
            plt.xlabel('Amplitude Vector')
            plt.ylabel('Frequency Vector')
            Title = 'Mean Comodulogram OFC Left #' + file.split('_')[1].split('.')[0]
            plt.title(Title)

            plt.savefig(Title + '.png')
