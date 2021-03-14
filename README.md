# ax50channelswitcher

Simple Python3 unittest script that uses selenium to log into TP-Link Archer AX50 and check whether the router has defaulted to channel 36. If so, it'll try to switch to one of the 2 desired channels. 
Change:

* URLTOYOURROUTER="http://192.168.0.1/"
* YOUR_ROUTER_PASSWORD="P4SSW0RD#" 
* DESIREDCHANNELS=[40,44]

to whatever your settings are.
