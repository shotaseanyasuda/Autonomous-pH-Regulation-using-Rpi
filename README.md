# Autonomous-pH-Regulation-using-Raspberry Pi

The goal of this project is to create an automated pH regulation system on a miniature Hydroponic garden(Nutrient Film Technique/Deep Water Culture hybrid system) using a pH probe, two dosing pumps, a touchscreen display, and a Raspberry Pi 4. 

The pH probe will be inserted into the reservoir and it will take and display constant readings of the water's pH. If the Raspbery Pi detects that the reservoir's pH level rises above or falls below a certain threshold programmed by the user, the dosing pumps will dispense small amounts of pH up(base) or pH down(acid) solution in between intervals of pH readings until pH is back within the desired range.

Touchscreen Display will display the current pH readings as well as the user-determined upper and lower limits for pH. The display also features buttons that allow the user to manually dispense acid and base on command.

<img width="1218" alt="Cardboard" src="https://user-images.githubusercontent.com/77286593/141531614-a85b695a-9c0c-41de-b8d8-51960e496095.png">

### Materials Used
- Foodsafe Storage container
- 3" PVC pipe
- 3" PVC end caps
- 10 gallon pump
- 5/8in tubing
- 2" net cups
- Breadboard
- GPIO Ribbon Cable
- MCP3008 chip https://www.adafruit.com/product/856
- Raspberrypi 4 https://www.raspberrypi.org/products/raspberry-pi-4-model-b/
- Element14 Touchscreen Display 7" https://www.element14.com/community/docs/DOC-78156/l/raspberry-pi-7-touchscreen-display
- Atlas Scientific Analog pH probe https://atlas-scientific.com/gravity-analog-ph-kit/
- Atlas Scientific EZO-PMP™ Embedded Dosing Pump https://atlas-scientific.com/ezo-pmp/
- Maxigrow Hydroponic plant food https://www.amazon.com/General-Hydroponics-MaxiGro-Gardening-2-2-Pound/dp/B00NQANQAC
### Tools Needed
- Power Drill
- 2" hole saw drill bit
- Keyboard
- Mouse
- 3D Printer + filament

### Spring 2021
Gathered Food Safe Tote box, 10G pump, tubing, PVC pipe with end caps, net cups.
Drilled 4 2" holes into PVC pipe using power drill and 2" hole saw drill bit.
Put end caps on PVC pipe. Drilled holes in end caps for 5/8" tubing for water flow.

![Hydroponic basic equipment](https://user-images.githubusercontent.com/77286593/156471523-5c7fa6c4-7510-448b-899f-bedcc575a15d.png)

Installed Raspbian onto SD card for the Raspberrypi
