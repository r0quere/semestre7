#Yassine 09/03
#Main : 1- Interface pour établir la communication en série avec la STM32 en affichant les ports disponibles
# et les débits
# 2- 

from IHM_Master import RootGUI, ComGui
from Serial_Com_ctrl import SerialCtrl
from Data_Com_ctrl import DataMaster
# Initiate the Root class that will manage the other classes
MySerial = SerialCtrl()
MyData = DataMaster()
RootMaster = RootGUI(MySerial, MyData)
# Initiate the Communication Master class that will manage all the other GUI classes
ComMaster = ComGui(RootMaster.root, MySerial, MyData)

# Start the Graphic User Interface
RootMaster.root.mainloop()