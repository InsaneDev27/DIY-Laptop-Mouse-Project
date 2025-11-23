# DIY-Laptop-Mouse-Project

The Laptop Mouse Project is a DIY fix to discomfort caused by prolonged use of laptop trackpads. The LMP offers an ergonomic alternative to a typical mouse or trackpad, and secures to the sides of laptops for stability and comfort. It is mostly 3-D printable, and all electronics can be found online.

## Intro



## Required Skills

 - Familiarity with 3-D printing and Slicers
 - Cleaning up 3-D prints, removing supports, and resolving small tolerance issues
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
 - Small Files
 - Razor/Carving Tools
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
 (fitment is not universal; some post-processing and tolerance adjusting are necessary)
 (optional cap if don't want clamp)
 (print less walls on thumstick for easy installation)
 (thumbstick can use any aftermarket thumbstick, as long as it is comfortable)

 #### Post-Processing and Tolerancing:
 - Left Body
Begin by removing support material as usual. Then, use a spare 4-pin pushbutton to test fit both the left and right click button slots, and remove material as needed. After post-processing the Left Click Trigger and Right Click Trigger, test fit these and remove material from the body and the parts until they slide with minimal resistance.\
(Image HERE) (completed left body, point out areas of focus)\
NOTE: Avoid filing and removing material from anywhere visible on the completed assembly, as this will likely result in discoloration that is difficult to fix.

 - Right Body
Repeat the process explained in the left body. Pay attention to the cylindrical region of the front (left click) trigger slot, as this is often a source of resistance.\
(Image HERE) (point out trigger areas)

 - Left Click Trigger
Remove all support, file the cylindrical extrusion to remove any surface imperfections that result in drag, test fit with each side of the body, then assemble both sides and the trigger\
(Image HERE) (completed part)

 - Right Click Trigger
 When removing support, remember to not put stress on the pivot axle of the part and that the three support arms that anchor the plunger can get in the way of removing support. These support arms may not always be necessary, and can be removed if needed. After the basic support removal, file down the inside top edge of the part until all suport residue is gone, file down the plunger, then test fit.
(Image HERE) (point out points of interest, broken part if available, and finished part)

 - Scroll Wheel
 Whether or not this was printed in metal, test fit the part with the rotary encoder. If much resistance is encountered, cease insertion immediately, remove and file down. then test fit without the encoder in the Left Body, and remove material from the body as needed.

 - Clamp Body
 When removing support, be avoid putting pressure on the swivel where it connects to the body.\
(Image HERE) - broken swivel\
Once all support is removed, file down the inside face of between the top and bottom until mostly smooth.\
(Image HERE) - smooth inside face\
Then, use a lighter or heat gun to recolor this segment. Avoid severely melting or warping the part.\
(Image HERE) (using lighter, completed, and warped)\
After this, use a 3/8" - 16 or 3/8" - 24 inside tapping tool to thread the hole for the screw.\
(Image HERE) (tapping and finished images)

 - Clamp Screw
 Remove supports, file down the face under the head of the screw. Then, use a 3/8" - 16 or a 3/8" - 24 (must be same as used on clamp body) outside tapping tool to thread the screw. Use pliers to grip close to the tapping tool to prevent breaking the part. once your pliers run out of room above the tapping tool, position them below, and keep tapping. Don't worry about grooves left by the pliers, as the tapping tool will mostly fix this on the way back down.\
(Image HERE) (tapping, switched grip tapping, final position of the tap, finished part)\
Finally, use a lighter or a heat gun to recolor the screw. Use caution and quick sweeps, as this part warps very easily.
(Image HERE) (using lighter, finished part, warped part)

 - Clamp Screw Bottoms
Remove supports as usual, lightly file the pegs, add chamfer to the pegs with a file.\
(Image HERE) -lightly filed and chamfered\
On the female side, remove supports from the holes and make sure there is no residual material in the holes.\
(Image HERE) -cleared holes\
Then gently place the two halves together, making sure not to completely attach the two sides as this should be a very tight fit. Remove material from the pegs until the tips of the pegs can go into the holes. Again, the fit is intended to be tight, and not be assembled until installation with the clamp screw. Once ready, screw the Clamp Screw into the Clamp Body, then run the center peg of the male Clamp Screw Bottom through the hole at the bottom of the Clamp Screw.\
(Image HERE) - assembly with only male side\
Then line up the female side of the Clamp Screw Bottom with the male side and use pliers to press fit the sides together. If the female side starts warping excessively, gently remove and file the pegs again. Repeat until fits properly.\
(Image HERE) -completed assembly


 #### Assembly + Notes:
   
   Once all the parts are clean and free of supports, begin test-fitting each piece together. The two halves of the main body should fit easily, but some areas may require more work.
      
   The slot for the thumbstick board on the left side of the body is prone to getting clogged by supports, so be sure to adjust for that in slicer settings or attend to that in post-processing. Aside from that, once support material is removed from the slots, all the electronics should slide in fairly easily. (There may be differences in tolerance between printers, so the previous statement could only apply to my machine)
   
   After all tolerance issues are resolved, assembly can begin. To start, I normally begin with the electronics and place the right-click button first, but feel free to install in whichever order makes the most sense.
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
   
   ##### Installing the Triggers and Thumbstick Cover
   To begin the process, I normally start with the Left Click Trigger, as it is the last piece needed to attach the two halves. To install the trigger, first, double check that the space between the end of the slide limiters and the electronic button is slightly too long. In this case, just cut off material from the tip.\
   (Image HERE)\
   From there, simply place the trigger in the half with all the electronics, and attach the other side.\
   (Image HERE) (trigger in the left half, both sides connected)\
   Assuming the trigger still works as desired and slides well, you can use the 3/4" screws to secure the two halves together.\
   (Image HERE) (screwing in a screw, all screws installed)

   After both sides are attached, I transition to the Right Click Trigger. The main point of struggle with this piece is the extender for the plunger. This part prints attached to a long handle for easier filing and adjustment. Using the handle, push the plunger extender into the hole on the left side of the body.\
   (Image HERE) - using handle to push plunger into hole\
   If any resistance is encountered, stop immediately, gently remove the extender, and file it down in the areas that were causing struggle.
   (Image HERE) - filing down the extender\
   Repeat this process as needed. Once the extender is satisfactory, cut off the handle and place the extender in the hole with the center of the torus segment facing the front of the device.\
   (Image HERE) (cut off extender, placing in the hole with torus diagram, in the hole)\
   Once this is complete, simply attach the Right Click Trigger as shown previously.\
   (Image HERE) -right click attached

   Finally, it is time for the Thumbstick Cover. This part can be tricky to get right, but focus on not removing too much material from the hole in the Thumbstick Cover, else it will become wobbly during use. Align the hole of the cover with the stick of the Thumbstick, and try to press on. If this does not work, start removing material from the hole. The hole is ovular, so avoid using drills or circular options. If you printed this with less walls, the added flex of the material should assist with installation. If not, keep removing material until you are able to press the thumstick in place. Once installed, if you desire, you can add super glue to secure the cover.\
   (Image HERE) - thumbstick cover attached

   

## Final Results

## Conclusion and Final Thoughts

