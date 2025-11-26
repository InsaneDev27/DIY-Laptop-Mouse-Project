# DIY-Laptop-Mouse-Project

The Laptop Mouse Project (LMP) is a DIY fix to discomfort caused by prolonged use of laptop trackpads. The LMP offers an ergonomic alternative to a typical mouse or trackpad and clamps to the side of laptops for stability and comfort. It is mostly 3-D printable, and all electronics can be found online.

## Intro



## Required Skills

 - Familiarity with 3-D printing and Slicers
 - Cleaning up 3-D prints, removing supports, and resolving small tolerance issues
 - Soldering
 - Familiarity with 3-D printing companies such as PCBWay or JLCPCB (only if your printer cannot print the scroll wheel strong enough)

## Parts List

 - 1x  Raspberry Pi Pico  (example: [pico](https://www.pishop.us/product/raspberry-pi-pico/?src=raspberrypi))
 - 1x  Joystick  (designed only for: [adafruit_joystick](https://www.adafruit.com/product/512))
 - 1x  5mm Mouse Rotary Encoder  (example: [kalih_red_5mm_mouse_encoder](https://www.aliexpress.us/item/3256806292223943.html?spm=a2g0o.order_list.order_list_main.5.2ec01802nDnpCD&gatewayAdapt=glo2usa))
 - 2x  4-Pin Push Buttons 6x6x5mm  (example: [amazon_button_pack](https://www.amazon.com/Momentary-Pushbutton-Switches-Breadboard-Electronic/dp/B09R42NFGN/ref=sr_1_1?crid=1DX43WGBWLIU5&dib=eyJ2IjoiMSJ9.DXk5BbxDHSiJJjCdTGdYFrGrHSPxeZjexUARIOWPXaGuUKrpvKHrZPfwT8M7QW-z1TUlZVRWF4wJ_uTXdLjK63bFAPTz3kdr7TUs7w-htF2f5IxVfRd6xHCcEwTcIxOgQ0LaYFem3NL6vboEB6tezYn8HnUeDWYJA6VTvSZ-diyOWkA4R6y9CyrQ1ruPFiN6XdGafszn4lFCSxWVGETcAyZZC9yobfY6JQMW6vzuPOs.Mj1qsziIMg95O4oHzvB9dXVHvoZIJiEi77VNEeLWRuQ&dib_tag=se&keywords=4%2Bpin%2Bbreadboard%2Bbutton%2B6x6x5&qid=1722558613&sprefix=4%2Bpin%2Bbreadboard%2Bbutton%2B6x6x5%2Caps%2C256&sr=8-1&th=1))
 - 3x  #4 ¾” Flathead Phillips Machine Screws
 - 4x  #4 ½” Flathead Phillips Machine Screws
 - 1x  USB to Micro USB Cable (3 ft, but can order different length to fit preferences)
 - Solid Single-Core 22 AWG Wire

Estimated Total Cost (with shipping to the US and outsourcing the scroll wheel): $40 to $60

Cost Breakdown (including shipping to the US):
 - $32 - Scroll Wheel in Metal (this is for Stainless Steel SLA on PCBWay) (Resin printing may also be strong enough, and is more cost effective at ~$10 on PCBWay)
 - $12 - Adafruit Joystick
 - $4 - 5mm Rotary Encoder (possible to harvest from an old mouse)
 - $8 - Raspberry Pi Pico
 - $3 - ~136g of PLA filliment

## Tools List

 - 1x  Soldering Iron
 - 1x  Wire Stripper (22 gauge capable)
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
      
   The slot for the thumbstick board on the left side of the body is prone to getting clogged by supports, so be sure to adjust for that in slicer settings or attend to that in post-processing. Aside from that, once support material is removed from the slots, all the electronics should slide in fairly easily. (There are often differences in tolerance between printers, so the previous statement may only apply to my machine)
   
   After all tolerance issues are resolved, assembly can begin. To start, I normally begin with the electronics and place the right-click button first, but feel free to install in whichever order makes the most sense.\
   NOTE: When bending wires and installing the electronics, it is typical to break a solder joint or two. Use care when bending the wires and have a soldering iron on standby just in case.
   ##### Right Mouse Button
   I normally use my automotive picks to slot the button in place, and use another pick or an unwound paper clip to check if the button clicks as intended.
   
   ![Slotting right click button in place using automotive pick (button not highlighted)](https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Installing%20Right%20Click%20Button%20(Not%20Highlighted).jpg)
   ![Slotting right click button in place using automotive pick (button highlighted)](https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Installing%20Right%20Click%20Button%20(Highlighted).jpg)
   Checking click with a paper clip:
   ![Checking click with a paper clip](https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Checking%20Right%20Click%20Button%20With%20Paper%20Clip.jpg)
   Once in place, add super glue to where the button meets the plastic shell on the back right side of the button, making sure to avoid gluing the button open (where it refuses to depress).
   ![Gluing the right click button in place](https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Gluing%20in%20Right%20Click%20Button.jpg)
   ##### Raspberry Pi Pico
   After installing the left click, I normally slot in the Pico. Make sure that no wires are being pinched between the wall of the body and the pico, and simply slot it in. (Be sure the glue is dry if you are worried about the wires pulling the right mouse button out of place)
   (Image HERE) pico slotted
   ##### Left Mouse Button
   Before installing the left mouse button, I usually bend the thumbstick under the body to get it out of the way. 
   (Image HERE) thumbstick under body
   From there, it is a matter of bending wires and positioning the button in the slot. After this, install the thumbstick as described below, then put the two sides together and make sure the button and thumbstick align properly on both sides. If everything fits properly, you can use super glue to attach the button to the left side of the body if desired (be careful not to glue the two halves of the body together).
   ##### Thumb Stick
   Simply slide into the slots on the left side of the body. Support material often gets clogged in there, so some clearancing may be necessary.
   (Image HERE) (sliding thumbstick in)
   ##### Rotary Encoder
   Before installing, push the axle of the scroll wheel into the back side of the encoder. This should slide in easily. If it does not, immediately remove the scroll wheel and file it down before retrying.
   (Image HERE) scroll wheel in rotary encoder
   When the scroll wheel is installed, slide the assembly into the designated slot. This too should be relatively effortless once positioned correctly (which sometimes takes some time), and if it isn't, file the slot down and then retry.
   (Image HERE) assembly installed
   ##### Attaching the Cable
   After all of the electronics are installed, I typically run the cable through the clamp body, then plug it into the pico. If the head of the USB Micro end of the cable doesn't fit in the provided hole in the clamp body, then shave off some of the rubber at the head. To avoid exposing wires, give around a millimeter on all sides of the plug.
   (Image HERE) shaved head
   (Image HERE) shaved head through clamp body
   From there, I normally have to use pliers to install the cable into the Pico due to the rubber head hitting the roof of the body.
   (Image HERE) attaching cable to pico
   ##### Installing the Triggers and Thumbstick Cover
   To begin the process, I normally start with the Left Click Trigger, as it is the last piece needed to attach the two halves. To install the trigger, first, double check that the space between the end of the slide limiters and the electronic button is slightly too long. In this case, just cut off material from the tip.\
   (Image HERE) cutting off tip\
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

   Finally, it is time for the Thumbstick Cover. This part can be tricky to get right, but focus on not removing too much material from the hole in the Thumbstick Cover, else it will become wobbly during use. Align the hole of the cover with the stick of the Thumbstick, and try to press on. This takes some force, but if it will not slide on, start removing material from the hole. The hole is ovular, so avoid using drills or circular options. If you printed this with less walls, the added flex of the material should assist with installation. If not, keep removing material until you are able to press the thumstick in place. Once installed, if you desire, you can add super glue to secure the cover.\
   (Image HERE) - thumbstick cover attached

   

## Final Results

## Conclusion and Final Thoughts

