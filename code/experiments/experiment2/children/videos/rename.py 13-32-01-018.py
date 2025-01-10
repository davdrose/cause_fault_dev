# add 'exp2' to the beginning of all the files in the directory
import os

def rename_images(directory):
    # for all the files in the directory
    for filename in os.listdir(directory):
        # if the file is a file
        if os.path.isfile(os.path.join(directory, filename)):
            # add 'exp2' to the beginning of the file
            new_filename = f'exp2_{filename}'
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == '__main__':
    directory = '/Users/hou/GitHub/causal_verbs_responsibility/code/experiments/experiment2/children/videos/warmup_materials'
    rename_images(directory)
