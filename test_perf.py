import os
from evaluate import evaluate_on_dataset

def test():

	accuracy = evaluate_on_dataset("galaxy_test.h5")
	threshold = 0.55

	print("Your accuracy: {}".format(accuracy))

	assert accuracy > threshold, "Accuracy needs to be less than {}".format(threshold)
