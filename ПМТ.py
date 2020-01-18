"""Return material microhardness

The user enters the readings of the "PMT-3 hardness tester" 
and receives the readings converted into micrometers 
and the hardness of the measured sample in megapascals

"""

weight=input("""
    Введите массу грузика в эксперементе в граммах (целое число)
    
""")
readings=input("""
    Введите диагонали отпечатков в делениях прибора через пробел
    В качестве десятичного разделителя используйте точку (.)
    
""")
r=readings.split( )
for i in r:
    #diagonal in microns
    print(float(i)*0.3)
    #microhardness of the sample
    print(18540*float(weight)/((float(i)*0.3)**2))
