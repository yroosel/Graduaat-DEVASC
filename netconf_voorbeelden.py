#!/usr/bin/env python
# coding: utf-8

# In[2]:


#### don't forget to check the IP address of the virtual router
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
####
"""
connect(self, host, port, timeout, unknown_host_cb, username, password, key_filename
      , allow_agent, hostkey_verify, hostkey_b64, look_for_keys, ssh_config, sock_fd, bind_addr)
"""
from ncclient import manager
print('------1-------')
print('Starting  -- netconfig')
print('Connecting to virtual router')
m = manager.connect(
        host="192.168.56.107",
        port="830",
        username="cisco",
        password="cisco123!",
        hostkey_verify=False
        )
print('------2-------')
print(dir(m))


# In[3]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Retrieving get-config from virtual router')
netconfig_reply = m.get_config(source="running")
print('------1-------')
print(type(netconfig_reply))
print('------2-------')
#print(netconfig_reply)
print("=> Output provided in the next cell")


# In[4]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('------1-------')
print('Parsing and printing XML')
import xml.dom.minidom
print(xml.dom.minidom.parseString(netconfig_reply.xml).toprettyxml())


# In[5]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
import xml.dom.minidom
print('------1-------')
print('Creating netconf filter')
print('Only retrieve portion of running config => Native YANG Model')
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
print('------2-------')
print(netconf_filter)
netconf_reply = m.get_config(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconfig_reply.xml).toprettyxml())


# In[9]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('------1-------')
print('Updating config with netconf -- changing hostname')
import xml.dom.minidom
netconf_data = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>CSR1Kv</hostname>
    </native>
</config>
"""
print("netconf_data:")
print(netconf_data)
print('------2-------')
netconf_reply = m.edit_config(target="running", config=netconf_data)
#print(dir(netconf_reply))
print("Type netconf_reply: ")
print(type(netconf_reply))
print('------3-------')
netconf_parsed = xml.dom.minidom.parseString(netconf_reply.xml)
print("Type netconf_parsed: ")
print(type(netconf_parsed))
#print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
print("Printed XML: ")
print(netconf_parsed.toprettyxml())


# In[3]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('------1-------')
print('Updating config with netconf -- creating loopback interface')
netconf_data = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>10111</name>
                <description>NETCONF loopback 10111</description>
                <ip>
                    <address>
                        <primary>
                            <address>10.1.1.1</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""
print('------1-------')
print("netconf_data:")
print(netconf_data)
netconf_reply = m.edit_config(target="running", config=netconf_data)
print("Type netconf_reply: ")
print(type(netconf_reply))
print('------2-------')
netconf_parsed = xml.dom.minidom.parseString(netconf_reply.xml)
print("Type netconf_parsed: ")
print(type(netconf_parsed))
print('------3-------')
#print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
print("Printed XML: ")
print(netconf_parsed.toprettyxml())

