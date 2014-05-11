#!/usr/bin/env python
'''
用法：
16进制数按位范围截取：
第一个参数是16进制数，第二个是要截取的MSB，第三个是LSB
'''
import sys
bin_s=bin(long(sys.argv[1],16))[2:]
if(int(sys.argv[2],10) < int(sys.argv[3],10)):
    print 'argument error:2nd is MSB,3rd is LSB,check'
elif(int(sys.argv[3],10) >= len(bin_s)):
    print 'input['+sys.argv[2]+':'+sys.argv[3]+']=0'
else:
    if(int(sys.argv[2],10) >= len(bin_s)):
        start=0
    else:
        start=len(bin_s)-int(sys.argv[2],10)-1
    end=len(bin_s)-int(sys.argv[3],10)
    print 'input['+sys.argv[2]+':'+sys.argv[3]+']='+hex(int(bin_s[start:end],2))
