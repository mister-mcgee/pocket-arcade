# pocket-arcade
Welcome to the Pocket Arcade project!


# Parts
| Part # | Description |
|--------|-------------|
| [3800](https://www.adafruit.com/product/3800) | Adafruit ItsyBitsy M4 Express featuring ATSAMD51 |
| [2088](https://www.adafruit.com/product/2088) | Adafruit 1.44" Color TFT LCD Display with MicroSD Card breakout - ST7735R |
| [2124](https://www.adafruit.com/product/2124) | Adafruit LiIon/LiPoly Backpack Add-On for Pro Trinket/ItsyBitsy |
| [1317](https://www.adafruit.com/product/1317) | Lithium Ion Polymer Battery - 3.7v 150mAh |
| [1009](https://www.adafruit.com/product/1009) | Colorful Round Tactile Button Switch |
| [805 ](https://www.adafruit.com/product/805 ) | Breadboard-friendly SPDT Slide Switch |


### A Note on Buttons
While the Pocket Arcade is compatible with Adafruit's [Colorful Round Tactile Button Switch](https://www.adafruit.com/product/1009), there are additional model files included for 3D printing low-profile button caps.

# Getting Started with Software

### Updating the Boot Loader
Begin by downloading the correct boot loader from the official CircuitPython website [here]([https://](https://circuitpython.org/board/itsybitsy_m4_express/)).

After downloading the correct firmware and plugging the Itsy Bitsy M4 Express into a computer via USB, double-tap the `reset` button located on the back of the ItsyBitsy. This will cause the board to appear as a special `BOOT` drive in your computer's file system.

Dragging and dropping the new firmware into the `BOOT` drive will cause the board to update the boot loader and restart.

### Updating CircuitPython
Begin by downloading the correct CircuitPython image from the official website [here]([https://](https://circuitpython.org/board/itsybitsy_m4_express/)).

After downloading the correct firmware and plugging the Itsy Bitsy M4 Express into a computer via USB, double-tap the `reset` button located on the back of the ItsyBitsy. This will cause the board to appear as a special `BOOT` drive in your computer's file system.

Dragging and dropping the new image into the `BOOT` drive will cause the board to update the current version of CircuitPython and restart.

### Installing the Pocket Arcade software
Begin by downloading the contents of this repository and unzipping the archive.

After [Updating the Boot Loader](#updating-the-boot-loader) and [Updating CircuitPython](#updating-circuitpython) the board should now appear as a special `CIRCUITPY` drive in your computer's file system. Delete all pre-existing files inside of `CIRCUITPY` and copy the unzipped contents of the repository into the top level directory.

While plugged into a computer via USB, the Pocket Arcade will boot into `readonly` mode. This is indicated by a special icon that appears during the boot sequence. In `readonly` mode scripts scripts will be unable to write to the on-board file system; however, you can still create, edit, or delete files on the board from your computer just like you would a typical drive.