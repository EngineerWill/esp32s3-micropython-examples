#---------------------------------------------------------------
# | File        :   flash-size.py                               
# | Author      :   Waveshare team                              
# | Function    :   get free flash size                       
# | Info        :   flash test code                            
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
import uos

# Get the total and free space on the flash
fs_stat = uos.statvfs('/')

free_flash_bytes=fs_stat[0]*fs_stat[3]
# Print the results
print('')
print('Free space   : {} bytes = {:.3f}MB'.format(free_flash_bytes,free_flash_bytes/1024/1024))