import qrcode
line='www.google.com'
test=qrcode.make(line)
test.save('test1.png')