def int32_to_ip(int32):
    int32 = bin(int32)[2:].rjust(32, '0')
    result = f"{int(int32[:8], 2)}.{int(int32[8:16], 2)}.{int(int32[16:24], 2)}.{int(int32[24:], 2)}"
    return result

  
assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"

