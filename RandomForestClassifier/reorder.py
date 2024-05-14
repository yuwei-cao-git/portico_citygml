import numpy as np
import argparse

class_index = 6


def read_data(filepath):
    ''' Load a labelled point cloud from a .txt file
        Attributes:
            filepath (string)   :  Path to the .txt
        
        Return:
            X (np.array)   : Point cloud and features
            Y (np.array)   : Classes
    '''
    X, Y = [], []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            tokens = line.strip().split(' ')
            if 'nan' not in tokens:   
                X.append([float(t) for t_index, t in enumerate(tokens) if t_index != class_index])
                Y.append(int(float(tokens[class_index])))
    return np.asarray(X, dtype=np.float32), np.asarray(Y, dtype=np.float32)

def write_points(X, Y, filename):
    with open('{}.txt'.format(filename), 'w') as out:
        X = X.tolist()
        Y = Y.tolist()
        for index, x in enumerate(X):
            x_as_str = " ".join([str(i) for i in x])
            out.write('{} {}\n'.format(x_as_str, str(Y[index])))
            
def main():
    parser = argparse.ArgumentParser(description='Convert rgb to lab and save pts.')
    parser.add_argument('filepath', help='Path to the original file (.txt) [f1, ..., fn, c]')
    parser.add_argument('output_filepath', help='Name of the converted file')
    args = parser.parse_args()
   
    print("Loading data...")
    X, Y = read_data(args.filepath)
    
    write_points(X, Y, args.output_filepath)
    print('\tSaving to {}'.format(str(args.output_filepath)))
    
if __name__== '__main__':
    main()