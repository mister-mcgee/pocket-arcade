import storage
import microcontroller

if microcontroller.nvm[0:3] == b"usb":
  storage.remount("/", readonly=True )
else:
  storage.remount("/", readonly=False)