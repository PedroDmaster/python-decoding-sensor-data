import os
import glob
import csv

def load_sensor_data():
    sensor_date = []
    sendor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
    