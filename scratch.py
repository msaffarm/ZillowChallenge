import sys
import os
import pandas as pd
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = CURRENT_DIR + "/data/"


def main():
	data = pd.read_csv(DATA_DIR + "properties_2016.csv")
	print(data[data["parcelid"]==11016594])


if __name__ == '__main__':
	main()