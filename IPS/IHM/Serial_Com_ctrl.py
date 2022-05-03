import serial.tools.list_ports  # pip install pyserial
import time


class SerialCtrl():
    def __init__(self):
        '''
        Initializing the main varialbles for the serial data
        '''
        self.sync_cnt = 200

    def getCOMList(self):
        '''
        Method that get the lost of available coms in the system
        '''
        ports = serial.tools.list_ports.comports()
        self.com_list = [com[0] for com in ports]
        self.com_list.insert(0, "-")

    def SerialOpen(self, ComGUI):
        '''
        Method to setup the serial connection and make sure to go for the next only 
        if the connection is done properly
        '''

        try:
            self.ser.is_open
        except:
            PORT = ComGUI.clicked_com.get()
            BAUD = ComGUI.clicked_bd.get()
            self.ser = serial.Serial()
            self.ser.baudrate = BAUD
            self.ser.port = PORT
            self.ser.timeout = 0.1

        try:
            if self.ser.is_open:
                print("Already Open")
                self.ser.status = True
            else:
                PORT = ComGUI.clicked_com.get()
                BAUD = ComGUI.clicked_bd.get()
                self.ser = serial.Serial()
                self.ser.baudrate = BAUD
                self.ser.port = PORT
                self.ser.timeout = 0.01
                self.ser.open()
                self.ser.status = True
        except:
            self.ser.status = False

    def SerialClose(self, gui):
        '''
        Method used to close the UART communication
        '''
        try:
            self.ser.is_open
            self.ser.write(gui.data.StopStream.encode())
            self.ser.close()
            self.ser.status = False
        except:
            self.ser.status = False

    def SerialSync(self, gui):
        '''
        Method to make sure that the MCU is using the same synchronizing protocol
        then establish the communication
        This method will show if the Sync is ok or failed + shows the number of available channels
        '''
        self.threading = True

        time.sleep(0.2)
        cnt = 0
        while self.threading:
            try:
                self.ser.write(gui.data.sync.encode())
                gui.conn.sync_status["text"] = "..Sync.."
                gui.conn.sync_status["fg"] = "orange"
                gui.data.RowMsg = self.ser.readline()
                gui.data.DecodeMsg()
                if gui.data.sync_ok in gui.data.msg[0]:
                    if int(gui.data.msg[1]) > 0:
                        gui.conn.btn_start_stream["state"] = "active"
                        gui.conn.btn_add_chart["state"] = "active"
                        gui.conn.btn_kill_chart["state"] = "active"
                        gui.conn.save_check["state"] = "active"
                        gui.conn.sync_status["text"] = "OK"
                        gui.conn.sync_status["fg"] = "green"
                        gui.conn.ch_status["fg"] = "green"
                        gui.conn.ch_status["text"] = gui.data.msg[1]
                        gui.data.SynchChannel = int(gui.data.msg[1])
                        gui.data.GenChannels()
                        gui.data.buildYdata()
                        self.threading = False
                        break
            except Exception as e:
                print(e)
            cnt += 1

            if self.threading == False:
                break
            if cnt > self.sync_cnt:
                gui.conn.sync_status["text"] = "failed"
                gui.conn.sync_status["fg"] = "red"
                time.sleep(0.5)
                cnt = 0
                if self.threading == False:
                    break


if __name__ == "__main__":
    SerialCtrl()