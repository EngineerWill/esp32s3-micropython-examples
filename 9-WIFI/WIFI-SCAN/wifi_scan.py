#---------------------------------------------------------------
# | File        :   wifi_scan.py                               
# | Author      :   Waveshare team                              
# | Function    :   wifi saan and print info
# | Info        :   wifi test code                          
#---------------------------------------------------------------
# | This version:   V1.0                                        
# | Date        :   2022-03-15                                  
# | Info        :   Basic version                               
#---------------------------------------------------------------
import network

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

authmodes = ['Open', 'WEP', 'WPA-PSK','WPA2-PSK', 'WPA/WPA2-PSK', 'WPA2_ENTERPRISE', 'WPA3_PSK', 'WPA2_WPA3_PSK', 'WAPI_PSK', 'OWE']
#sta_if.scan()
for (ssid, bssid, channel, RSSI, authmode, hidden) in sta_if.scan():
  print("* {:s}".format(ssid))
  print("   - Auth: {} {}".format(authmodes[authmode], '(hidden)' if hidden else ''))
  print("   - Channel: {}".format(channel))
  print("   - RSSI: {}".format(RSSI))
  print("   - BSSID: {:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(*bssid))
  print()
  
  