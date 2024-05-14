from skimage import color
import numpy as np
import argparse

''' script example
    python rgb2lab.py '.\Dataset\feature_extraction\mantova_X70.las.section.rotated.txt' '.\Dataset\feature_extraction\mantova_X70.las.section.rotated.colors'
'''
    
def read_data(filepath):
    X = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            tokens = line.strip().split(' ')
            if 'nan' not in tokens:   
                X.append([float(t) for t_index, t in enumerate(tokens)])
    return np.asarray(X, dtype=np.float32)

def rgb2lab(X):
    X_lab = color.rgb2lab(X[:, 3:6])
    b_lab = X_lab[:, -1].reshape((-1,1))
    rgb_composition = ((X[:,3]+X[:,4]+X[:,5])/3).reshape((-1,1))
    return np.concatenate((b_lab, rgb_composition), axis=1)

def write_points(X, Y, filename):
    with open('{}.txt'.format(filename), 'w') as out:
        X = X.tolist()
        Y = Y.tolist()
        for index, (x, y) in enumerate(zip(X, Y)):
            x_as_str = " ".join([str(i) for i in x])
            y_as_str = " ".join([str(j) for j in y])
            out.write('{} {}\n'.format(x_as_str, y_as_str))

def main():
    parser = argparse.ArgumentParser(description='Convert rgb to lab and save pts.')
    parser.add_argument('filepath', help='Path to the original file (.txt) [f1, ..., fn, c]')
    parser.add_argument('output_filepath', help='Name of the converted file')
    args = parser.parse_args()
   
    print("Loading data...")
    X = read_data(args.filepath)
    b_lab = rgb2lab(X)
    print('\tInput samples: {}'.format(len(X)))
            
    write_points(X, b_lab, args.output_filepath)
    print('\tSaving to {}'.format(str(args.output_filepath)))
    
if __name__== '__main__':
    main()