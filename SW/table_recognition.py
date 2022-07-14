# External module imports
from time import sleep

# Internal module imports
from irsensor import *
from camera import *
#from wolk_publish import *
from servo import *
from image_processing import *

# Function for table check
def check_table(table_str):
	table1_1 = "BG"
	table1_2 = "901"
	table1_3 = "BD"
	table2_1 = "NS"
	table2_2 = "659"
	table2_3 = "RR"
	if( (table1_1 in table_str) and (table1_2 in table_str) and (table1_3 in table_str) ):
		return True;
	if( (table2_1 in table_str) and (table2_2 in table_str) and (table2_3 in table_str) ):
		return True
	return False

# Program
try:
	while 1:
		print("Wait for IR...")
		wait_for_IR()                                                                                                   
		print("IR detected!")
		print("Take a picture:")
		take_a_picture()
		print("Picture is ready!")
		table = process_image()
		print("Tablica", table)
		table_correct = check_table(table)
		if(table_correct):
			open_door()
			print("Opened door")
			sleep(5)
			close_door()
#			publish_wolk(table)
#			print("Table is published")
		else:
			print("Incorrect table")
		sleep(1)
#		break
except KeyboardInterrupt:
	print("Program STOP")


