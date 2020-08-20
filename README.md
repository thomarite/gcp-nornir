In GCP I have a EVE-NG environment where I can build bigger labs. So here I am adding scripts I am creating in the way while testing things.

So far, all python is developed under pyenv 3.7.3

Some interesting ones:

show-frr.py -- run show commands in EOS to get info about TI-LFA using netmiko (slow!)

show-frr-napalm.py -- run show commands in EOS to get info about TI-LFA using nornir-napalm (quick! because it uses eAPI!)
