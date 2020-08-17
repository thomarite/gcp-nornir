
for i in range(1,10):
    my_text = \
    "interface Loopback1\n\
     description CORE Loopback\n\
     ip address 10.0.0.{index}/32\n\
     node-segment ipv4 index {index}\n\
     isis enable CORE\n\
     isis metric 1\n\
    router isis CORE\n\
     net 49.0000.0001.0010.0000.0000.000{index}.00\n\
     is-type level-2\n\
     log-adjacency-changes\n\
     set-overload-bit on-startup wait-for-bgp\n\
     address-family ipv4 unicast\n\
      bfd all-interfaces\n\
     segment-routing mpls\n\
      router-id 10.0.0.{index}\n\
      no shutdown\n".format(index=str(i))
    print(my_text)
