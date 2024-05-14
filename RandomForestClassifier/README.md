# **Random Forest 4 Point Cloud Classification - RF4PCC**
The following code has been developed, starting from the scikit-learn libraries, in order to supervisly classify 3D point clouds. 

## **Dependencies**
Python3 and Scikit-learn

## **Requirements** 
1.  **Training file:** a portion of your point cloud with associated geometric and/or radiometric features and a class index (coming after the manual annotation)
2. **Evaluation file:** another portion of the point cloud with the same features in the same order and again the manually annotated class index (the classifier will use this file to evaluate the performance of the classification).
3.  **Test file:** the rest of your dataset with the same features, in the same order
4.  **Feature and class index file:** create a two-lines file, the first line is dedicated to the column index of the features that you are using, the second line is for the column which contain the class index.

   For example, considering the following distribution of the point cloud columns 

   **x y z r g b f1 f2 f3 class_index**
   **if you want to use f1 f2 f3 as features the txt file will be :**
   **Line_1: 6 7 8**
  
   **Line_2: 9**

All the files have to be save in **.txt** format, and **without header** (Training, Evaluation and Test set) 

## **Classes**
**1:Floor 2:Facade 3:Column 4:Arch 5:Vault 6:Openings 7:Staris**

## **How to run** 
After you have prepared the aforementioned files, collect them in a folder together with the train.py and classify.py files. 

At a command prompt run:

>$ python train.py feature_path training_path evaluation_path n_core file_to_save_name

This should result in the creation of:
-  your classifier model **.pkl**. The name of this file will be related to the number of random trees that performed the best classification (i.e. ne50none.pkl). 
- a new .txt file containing the evaluation dataset with a new column with the predicted classes 

To extend the classification to the test dataset at a command prompt run:

> $ python classify.py feature_path classifier_path test_path file_to_save_name

This should result in the creation of your test file classified (the predicted classes are saved as the last column after the features)
