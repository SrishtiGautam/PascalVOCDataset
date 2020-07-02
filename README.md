# PascalVOCDataset

Having trouble like me to find a simple code to create classification folders for PASCAL VOC dataset?
Here you go!

Note:
It is mentioned in the document that for classification only the "non-difficult" samples are considered, where

There are three ground truth labels:
-1: Negative: The image contains no objects of the class of interest. A classifier should give a ‘negative’ output.
1: Positive: The image contains at least one object of the class of interest. A classifier should give a ‘positive’ output.
0: “Difficult”: The image contains only objects of the class of interest marked as ‘difficult’.
