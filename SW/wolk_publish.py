# External module imports
import os
import sys

# Import wolk
try:
	import wolk
except ModuleNotFoundError:
	print("Attempting to import WolkConnect from relative path")
	try:
		module_path = os.sep + ":" + os.sep + ":" + os.sep
		sys.path.append(
			os.path.dirname(os.path.realpath(__file__)) + module_path
		)
		import wolk
	except Exception as e:
		print(f"Failed to import WolkConnect: '{e}'")
		raise e

# Init wolk device and connect
device = wolk.Device(key="KILEROBIJA", password="0cdc4149-357b-4e15-911b-856fa6a955b5")
wolk_device = wolk.WolkConnect(device)
wolk_device.connect()

# Publish wolk function
def publish_wolk(tabl):
	try:
		tablica = tabl
		wolk_device.add_sensor_reading("broj_tablice", tablica)
		print(f'Broj tablice: {tablica}')
		wolk_device.publish()
	except KeyboardInterrupt:
		print("\tReceived KeybordInterrupt. Exiting script")
		wolk_device.disconnect()
		return


