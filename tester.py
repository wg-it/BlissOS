from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = MonkeyRunner.waitForConnection()

device.installPackage('/system/priv-app/com.perpetualtv.android/com.perpetualtv.android.apk')

device.startActivity(component='com.perpetualtv.android/.MainActivity')

device.touch(200, 400, 'DOWN_AND_UP')
device.type('Hello')

result = device.takeSnapshot()
result.writeToFile('screenshot.png', 'png')