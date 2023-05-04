import json
import time
import csv
from MRTD import HardwareScanner, decode

records_encoded_file = open('records_encoded.json','r')

records_encoded_file = json.load(records_encoded_file)

f = open('decode_execution_time.csv', 'w')
writer = csv.writer(f)
writer.writerow(["No. of Lines", " Execution Time without test"])

counter = 0
step_thousand = 0
start_time = time.perf_counter()
for i in records_encoded_file['records_encoded']:
	HardwareScanner.MRZ = i
	counter+=1
	print(decode())
	if(counter==100):
		end_time = time.perf_counter()
		# print(f"Total time consumed to decode {counter} records is {end_time-start_time:0.8f} seconds")
		writer.writerow([str(counter), str(end_time-start_time)])

	if(counter==1000*(step_thousand+1)):
		end_time = time.perf_counter()
		step_thousand+=1
		# print(f"Total time consumed to decode {counter} records is {end_time-start_time:0.8f} seconds")
		writer.writerow([str(counter), str(end_time-start_time)])