
import serial                    # import pySerial module

data = ComPort.readline()        # Wait and read data


class ComPort:
    def __init__(self, selectedPort, baudrate, bytesize, parity, stopbits):

    	self.selectedPort = selectedPort
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits



    def showPorts(str):
   		print(serial.tools.list_ports)
   		return

 
	def serialTest(self):
	   selectedPort = serial.Serial(int(input('please select the communication port you would like to use')))
	   baudrate = int(input('please select the Baud Rate you would like to use'))
	   bytesize = int(input('please select the byte size you would like to use'))
	   stopbits = int(input('please select the stop bits you would like to use'))
	   print("the parameters you selected are as follows: {}.".format(self.selectedPort, self.baudrate, self.bytesize, self.stopbits))
	   return


showPorts()
serialTest()
print(data)
self.close(selectedPort)




def Example2():
    ser = serial.Serial(selectedPort, baudrate, timeOut)
    x = ser.read()          # read one byte
    print( "x = ", x )
    s = ser.read(10)        # read up to ten bytes (timeout)
    print( "s = ", s )
    line = ser.readline()   # read a '\n' terminated line
    ser.close()
    print( "line = ", line )


    '''
    Open Communication Port
    Detect Dialog Prompt
    pass return
    detect asterisks
    write 'RS232BEGIN'
    pass return
    400ms delay
    detect string "C01"
    read data stream
    write data stream to a txt file
    end when detect second "C01"
    pass value of M to equal 2 to set to night mode
    






