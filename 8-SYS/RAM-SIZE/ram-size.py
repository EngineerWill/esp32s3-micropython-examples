#---------------------------------------------------------------
# | File        :   ram-size.py                                 
# | Author      :   Waveshare team                              
# | Function    :   get ram size                       
# | Info        :   psram test code                            
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
import gc

# Get the current garbage collector threshold
gc.threshold(0)

# Get the current available heap memory size
available_ram = gc.mem_free()

# Get the current used heap memory size
used_ram = gc.mem_alloc()

# Print the RAM size
print("Available RAM: {} bytes= {:.3f}MB".format(available_ram,available_ram/1024.0/1024.0))
print("Used RAM     : {} bytes= {:.3f}MB".format(used_ram,used_ram/1024.0/1024.0))
