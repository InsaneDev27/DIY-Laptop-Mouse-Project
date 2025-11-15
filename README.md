# DIY-Laptop-Mouse-Project

The Laptop Mouse Project is a DIY fix to discomfort caused by prolonged use of laptop trackpads. The LMP offers an ergonomic alternative to a typical mouse or trackpad, and secures to the sides of laptops for stability and comfort. It is mostly 3-D printable, and all electronics can be found online.

## Intro



## Required Skills

 - Familiarity with 3-D printing and Slicers
 - Cleaning up 3-D prints, removing supports, and resolving small fitment issues
 - Soldering
 - Familiarity with 3-D printing companies such as PCBWay or JLCPCB (only if your printer cannot print the scroll wheel strong enough)

## Parts List

 - 1x  Raspberry Pi Pico  (example: pico)
 - 1x  Joystick  (designed only for: adafruit_joystick)
 - 1x  5mm Mouse Rotary Encoder  (example: kalih_red_5mm_mouse_encoder)
 - 2x  4-Pin Push Buttons 6x6x5mm  (example: amazon_button_pack)
 - 3x  #4 ¾” Flathead Phillips Machine Screws
 - 4x  #4 ½” Flathead Phillips Machine Screws
 - 1x  USB to Micro USB Cable (3 ft, but can order different length to fit preferences)
 - Solid Single-Core 22 AWG Wire

## Tools List

 - 1x  Soldering Iron
 - 1x  Wire Stripper (22 gauge)
 - 1x  Needle-Nose Pliers
 - 1x  Thread-Tap (must include ⅜” - 16 or ⅜” - 24 outside and inside tap)
 - 1x  Phillips Screw Driver
 - Small Files/Razor/Fitment-Adjusting Tools
 - Automotive Picks (recommended for removing supports in tight places)

## Assembly

### Electronics

#### Wire Lengths:

 - 1x  RMB  1.25”
 - 1x  LMB  1.75”
 - 2x  Button Ground  2.50”
 - 3x  Rotary Encoder  3.00”
 - 5x  Joystick  5.50”

#### Pinout Diagram:

#### Final Soldered Mock-up:

### Code

#### Configuring Raspberry Pi Pico:

#### Code Files:
(notes on scroll wheel)
(make sure to reference the libraries and circuit-python)
(comment/explain code clearly)

### 3-D Printing

#### 3-D Printing Files:
(maybe outsource to thingiverse?)

#### 3-D Printing Notes:
(settings / fuzzy skin)
(SCREW MUST BE PRINTED SOLID)
(Scroll-Wheel troubles with FDM, what I did to work around this)
(fitment is not universal; some post-processing and fitment adjusting are necessary)

#### Assembly + Notes:

Once all the parts are clean and free of supports, begin test-fitting each piece together. The two halves of the main body should fit easily, but some areas may require more work.\
   
The slot for the thumbstick board on the left side of the body is prone to getting clogged by supports, so be sure to adjust for that in slicer settings or attend to that in post-processing. Aside from that, once support material is removed from the slots, all the electronics should slide in fairly easily. (There may be differences in tolerance between printers, so the previous statement could only apply to my machine)\

\After all fitment issues are resolved, assembly can begin. To start, I normally begin with the electronics and place the right-click button first, but feel free to install in whichever order makes the most sense.
##### Right Mouse Button
This is sometimes a tight fit, so I would recommend using an unused 4-pin push button to double-check tolerance before attempting to install the soldered right-click button. From there, I normally use my automotive picks to slot the button in place, and use another pick or an unwound paper clip to check if the button clicks as intended. Once in place, add super glue to where the button meets the plastic shell on the back right side of the button, making sure to avoid gluing the button open (where it refuses to depress).
##### Raspberry Pi Pico
After installing the left click, I normally slot in the Pico. Make sure that no wires are being pinched between the wall of the body and the pico, and simply slot it in. (Be sure the glue is dry if you are worried about the wires pulling the right mouse button out of place)
##### Left Mouse Button
Before installing the left mouse button, I usually bend the thumbstick under the body to get it out of the way. From there, it is a matter of bending wires and positioning the button in the slot. Again, if a secondary 4-pin push button is available, I would recommend using it to ensure that the tolerance is correct. After this, complete the next step, then put the two sides together and make sure that everything fits well, if it does, you can use super glue to attach the button to the left side of the body.
##### Thumb Stick
Simply slide into the slots on the left side of the body. Support material often gets clogged in there, so some clearancing may be necessary.
##### Rotary Encoder
Before installing, push the axle of the scroll wheel into the back side of the encoder. This should slide in easily. If it does not, immediately remove the scroll wheel and file it down before retrying. When the scroll wheel is installed, slide the assembly into the designated slot. This too should be relatively effortless once positioned correctly (which sometimes takes some time), and if it isn't, file it down and then retry.
##### Attaching the Cable
After all of the electronics are installed, I typically run the cable through the clamp body, then plug it into the pico. If the head of the USB Micro end of the cable doesn't fit in the provided hole in the clamp body, then shave off some of the rubber at the head. To avoid exposing wires, give around a millimeter on all sides of the plug. From there, I normally have to use pliers to install the cable into the Pico due to the rubber head hitting the roof of the body.
##### Tapping the Clamp Screw

## Final Results

## Conclusion and Final Thoughts

