import os
import csv


def generate_log():

    # Create folder for results if it does not exist.
    if not os.path.exists('../logs'):
        os.makedirs('../logs')

    # Check if register file exists
    if not os.path.isfile('../logs/register.csv'):

        # If if doesn't, create it and create header.
        with open('../logs/register.csv', 'w') as csvfile:
            header_writer = csv.writer(csvfile, delimiter=',')
            header_writer.writerow(['Date and time', 'ID', 'Operation'])

