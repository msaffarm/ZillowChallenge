import os
import sys
import pandas as pd

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = CURRENT_DIR + "/../data/"
DATA_FILE = DATA_DIR + "data.csv"
RAW_DATA_FILE = DATA_DIR + "train_2016.csv"
METADATA_FILE = DATA_DIR + "properties_2016.csv" 

# consts
RANDOM_STATE = 100
TEST_TRAIN_RATIO = 0.3

class DataProvider(object):

	def __init__(self):
		pass


	def extract_training_records(self):
		"""
		Extract trainig data from raw data (train_2016.csv).
		Args: 
			None
		Returns: 
			None
		"""
		if not os.path.exists(DATA_FILE):
			print("Extracting records from train_2016")
			meta_data = pd.read_csv(METADATA_FILE)
			raw_data = pd.read_csv(RAW_DATA_FILE)
			data = pd.merge(raw_data,meta_data,on="parcelid",how="left")
			data.to_csv(DATA_FILE,index=False)
		else:
			print("Data is already extracted!")


	def get_test_train_data(self):
		pass







def main():
	dp = DataProvider()
	dp.extract_training_records()


if __name__ == '__main__':
	main()


