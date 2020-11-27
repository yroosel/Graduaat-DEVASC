import unittest
import ipv4

class test_ipv4(unittest.TestCase):
    
    #Test 1
    def test_get_net_prefix(self):
         self.assertEqual(ipv4.get_net_prefix('255.255.255.0'), '/24')
         self.assertEqual(ipv4.get_net_prefix('255.255.255.192'), '/26')

    #Test 2
    def test_get_number_ip_addresses(self):
        self.assertEqual(ipv4.get_number_ip_addresses('/18'), 16384)
        self.assertEqual(ipv4.get_number_ip_addresses('/17'), 32768)

    #Test 3
    def test_get_number_ip_hosts(self):
        self.assertEqual(ipv4.get_number_ip_hosts('/18'), 16382)
        self.assertEqual(ipv4.get_number_ip_hosts('/17'), 32766)

    #Test 4
    def test_get_netmask(self):
        self.assertEqual(ipv4.get_netmask('/18'), '255.255.192.0')
        self.assertEqual(ipv4.get_netmask('/17'), '255.255.128.0')

   #Test 5
    def test_get_network_bits(self):
        self.assertEqual(ipv4.get_network_bits('255.255.192.0') , '1111 1111 1111 1111 1100 0000 0000 0000')
        self.assertEqual(ipv4.get_network_bits('255.255.128.0') , '1111 1111 1111 1111 1000 0000 0000 0000')

if __name__ == '__main__':
    unittest.main()
