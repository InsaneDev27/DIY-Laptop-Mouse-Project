# DIY-Laptop-Mouse-Project

The Laptop Mouse Project (LMP) is a DIY fix to discomfort caused by prolonged use of laptop trackpads. The LMP offers an ergonomic alternative to a typical mouse or trackpad and clamps to the side of laptops for stability and comfort. It is mostly 3-D printable, and all electronics can be found online.

## Intro

I began this project because I have always been extremely disatisfied with laptop trackpads. Trackpads cause my wrist discomfort after prolonged use, especially when I am using my laptop on my lap. I realized that I am not the only one that feels this way, and set out to design a suitable alternative that would fix this discomfort. I hope that my solution will work for you as well.

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
 - $10 - Resin Printed Scroll Wheel (this is for resin printing on PCBWay, and includes shipping to the US) (I ordered Stainless Steel SLA on PCBWay for added strength and visual appeal, which cost $32)
 - $12 - Adafruit Joystick
 - $4 - 5mm Rotary Encoder (possible to harvest from an old mouse)
 - $8 - Raspberry Pi Pico
 - $5 - ~200g of PLA filliment

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

<img alt="Project Pinout" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Pi%20Pico%20Pinout%20for%20LMP.jpg" width="700">

NOTE: On the rotary encoder, there should be 2 legs on the sides that attach to the frame, but are not electrical. For these, simply cut them off, as they will interfere with assembly later, and will only cause confusion in the soldering stage.

<img alt="Rotary encoder pins to cut off" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Rotary%20Encoder%20diagram%20to%20cut%20off%20extra%20legs.jpg" width="200">

NOTE: The ground wires from the left mouse button (LMB) and right mouse button (RMB) are connected in my diagrams. I have done this by simply soldering the LMB ground to the pico, then the RMB ground to the LMB ground. I connected the two wires in this way to consolodate the wire spead and, in a previous design, other ground ports were blocked. However, if you would like to avoid having to connect the two wires, there is another ground pin on the pico 13 pins down on the left where you can route a longer ground wire to from one of the buttons.

<img alt="Secondary ground location" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Alternative%20Ground%20Position%20on%20Pico.png" width="700">
 
 #### Final Soldered Assembly:

 <img alt="Final Soldered Assembly 1" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Final%20Soldered%20Assembly%201.jpg" width="700">

 <img alt="Final Soldered Assembly 2" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Final%20Soldered%20Assembly%202.jpg" width="200">

### Code
   
 #### Configuring Raspberry Pi Pico:

 After everything is soldered to the Raspberry Pi Pico, connect the Pico to your computer. Navigate to the Pico in File Explorer, and drag and drop this file to the pico: [adafruit-circuitpython-raspberry_pi_pico-en_US-9.1.1.uf2](https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/Code/adafruit-circuitpython-raspberry_pi_pico-en_US-9.1.1.uf2). This will initiate the installation CircuitPython onto the Pico, enabling the use of the Adafruit HID library ([more information on the Adafruit HID library](https://docs.circuitpython.org/projects/hid/en/latest/)) that is the backbone of the code.

 \
 <img alt="Code zip file" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Code%20zip%20file.png" width="500">
 <img alt="CircuitPython download file" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/CircuitPython%20download%20file.png" width="500">
 <img alt="Installing CircuitPython on Pico" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Moving%20the%20CircuitPython%20download%20file%20to%20the%20Pico.png" width="500">
 <img alt="New CircuitPython device" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/New%20CircuitPython%20device.png" width="500">

 Once CircuitPython is installed, drag and drop the contents of the code folder onto the pico, making sure that main.py is not buried in a folder on the Pico: [code](https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/tree/main/Code/code).

 \
 <img alt="code folder" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/code%20folder.png" width="500">
 <img alt="Code files to copy" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/code%20files%20to%20copy%20to%20the%20Pico.png" width="500">
 <img alt="Copying code files to Pico" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/copying%20code%20files%20to%20Pico.png" width="500">

 Now, simply eject the pico, disconnect and reconnect the device. Make sure that all the electronics function properly and interface with your computer. Most of the code should be plug-and-play, but you may want to adjust the scroll wheel sensitivity and settings, or change/configure commands (RMB+LMB => your function).
 To do this, open the "main" file on your Pico. Most of the variables and code related to the Scroll Wheel is to implement a sort of psuedo-fast-scrolling, which is supposed to detect when the user scrolls in rapid succession and boost the effect of each scroll similarly to touchscreen scrolling. You can simply delete or comment out all of this code if you do not want this functionality, and tune the sensitivity manually. If you would like to investigate the psuedo-fast-scrolling, however, start by uncommenting the print file.

 <img alt="Uncommenting print" src="" width="600">

  In the output, numOfIncrementsRecently corresponds to the amount of physical clicks when the rotary encoder detects rotation. It is reset every time sensitivity is increased, and it is used to determine the amount of clicks that pass between each increase in speed. `if([numOfIncrementsRecently > 1] && [timeSinceLastFast <= maxTimeBetweenFastScroll]) {//increase sensitivity}`. lastTime refers to the last time the rotary encoder detected rotation (physical click). lastTimeFast is the last time that criteria was met to scroll fast. lastTimeSet tracks the last time fast scrolling was initiated. This is used as a secondary check to determine inelegibilty for scrolling fast. `if([(lastTimeFast > maxTimeSinceLastFast) && (lastTimeSet > 1)] || [scroll direction changed]) {//ineligble to go fast}`. Finally, encoderFactor is the sensitivity of the scroll wheel. Using these outputs, you can adjust maxTimeBetweenFastScroll, maxTimeSinceLastFast, encoderFactorBaseValue, the horsepower boost value (originally set to +=1), and how the encoderFactor gets increased. My settings work for my hand and my scroll speed, but they might not work for everyone. Additionally, the way I chose to implement pseudo-fast-scrolling may not be the best or most efficient way to accomplish this, and you can rewrite the whole system if you so desire.
  
  Lastly, the commands can be customized. Originally I have it set so that when all three buttons are pressed simutaneuosly (LMB+RMB+CMB), thumbstick sensitivity (similar to DPI) is cycled, and when only left and right click are pressed together, sensitivity is set to low to make fine motion easier. However, these commands can be altered or removed, and are located towards the bottom of the main function.

  <img alt="Code for special commands" src="" width="600">

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
 **Left Body**

Begin by removing support material as usual. Then, use a spare 4-pin pushbutton to test fit both the left and right click button slots, and remove material as needed. Pay attention to the thumbstick base slot, as this often gets clogged with support material. Finally, test fit with thumbstick if possible.

<img alt="Test fitting left and right click 4-pin push buttons with Left Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Test%20Fitting%204-Pin%20Buttons%20with%20Left%20Body.jpg" width="400">

<img alt="Cleaning out thumbstick base slot on Left Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Removing%20Supports%20from%20Thumbstick%20Slot%20on%20Left%20Body.jpg" width="600">

<img alt="Test fitting thumbstick with Left Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Test%20Fitting%20Thumbstick%20with%20Left%20Body.jpg" width="400">

Completed Left Body:\
<img alt="Completed Left Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Finished%20Left%20Body.jpg" width="600">

NOTE: Avoid filing and removing material from anywhere that will be visible on the completed assembly, as this will likely result in discoloration that is difficult to fix.

**Right Body**

Repeat the process explained for the Left Body. Pay attention to the cylindrical region of the front (left click) trigger slot, as this is often a source of resistance. If needed, this can be filed square on both the Right Body and the Left Body.

<img alt="Filing Left Click Trigger slot square" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Pointing%20Out%20Cylindrical%20Slot%20for%20Left%20Click%20Trigger%20on%20Right%20Body.jpg" width="400">

Completed Right Body:\
<img alt="Completed Right Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Completed%20Right%20Body.jpg" width="600">

<img alt="Test fitting with Left Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Test%20Fitting%20both%20Bodies.jpg" width="400">

**Left Click Trigger**

Remove all support, file the cylindrical extrusion to remove any surface imperfections that result in drag. Test fit with each side of the body checking for resistance. Additionally, the wings of the trigger (the extrusions that stop the trigger from falling out) can be too long. Be sure thst these allow the trigger to slide long enough, and do not cause interference.

<img alt="Adjusting wing on Left Click Trigger" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Adjusting%20the%20Wings%20on%20Left%20Click%20Trigger.jpg" width="400">

Finally, assemble both sides, sanwiching the trigger, and make sure there is no new interference.

Completed Left Click Trigger:\
<img alt="Left Trigger done" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Finished%20Left%20Click%20Trigger.jpg" width="400">

**Right Click Trigger**

 When removing support, remember to not put stress on the pivot axle of the part and that the three small arms that anchor the plunger can get in the way of removing support. These support arms may not always be necessary, and can be removed if needed.

Look out for:\
<img alt="Point out swivel arm on Right Click Trigger" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Swivel%20Axle%20of%20Right%20Click%20Trigger.jpg" width="400">
<img alt="Point out swivel arm on Right Click Trigger (supports removed)" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Pointing%20Out%20the%20Swivel%20Arm%20of%20Right%20Click%20Trigger%20with%20Supports%20Removed.jpg" width="400">

The small arms:\
<img alt="The three small arms" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Pointing%20Out%20one%20of%20the%20Supporting%20Arms%20on%20Right%20Click%20Trigger.jpg" width="400">
<img alt="Mock-removal of one small arm with knife" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Removing%20Supporting%20Arms%20from%20Right%20Click%20Trigger.jpg" width="400">

After the basic support removal, file down the inside top edge of the part until all suport residue is gone, file down the plunger, then test fit with the Left Body, and remove material from both parts as needed.

Completed Right Click Trigger:\
<img alt="Finished Right Click Trigger" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Finished%20Right%20Click%20Trigger.jpg" width="600">

\
<img alt="Removing material from the Left Body on the top of the right click trigger slot" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Adjusting%20Right%20Click%20Trigger%20Slot%20on%20Left%20Body.jpg" width="400">
<img alt="Test fitting with the Left Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Test%20Fitting%20Right%20Click%20Trigger%20with%20Left%20Click.jpg" width="400">

**Scroll Wheel**

 Whether or not this was printed in metal, start by filing down the cylinder that supports the side opposite the hexagonal axle.

<img alt="Filing down the cylinder opposite the hex axle" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Filing%20Cylinder%20Opposite%20Hex%20Axle.jpg" width="400">

From there, test fit with the Left Body. If the part does not fit easily in the slot, start removing material from the Left Body. By the end, the Scroll Wheel should be able to spin in the slot with zero resistance from the Left Body.

<img alt="Removing material from scroll wheel slot" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Adjusting%20Scroll%20Wheel%20Slot.jpg" width="400">

Then test fit the part with the rotary encoder. If much resistance is encountered, cease insertion immediately, remove and file down the indivual sides of the hex axle, trying to make sure material is removed from each side equally.

\
<img alt="Filing down scroll wheel axle" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Filing%20Scroll%20Wheel%20Hex%20Axle.jpg" width="400">
<img alt="Test fitting with rotary encoder" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Test%20Fitting%20Scroll%20Wheel%20with%20Rotary%20Encoder.jpg" width="400">

Test fitting upside down just to check fitment:\
<img alt="Test fitting scroll wheel assembly with Left Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Test%20Fitting%20Scroll%20Wheel%20Assembly%20and%20Left%20Body%20(during%20post-processing).jpg" width="400">

Finished Scroll Wheel:\
<img alt="Finished Scroll Wheel" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Finished%20Scroll%20Wheel.jpg" width="400">

**Clamp Body**

 When removing support, avoid putting pressure on the swivel where it connects to the body.

<img alt="Broken swivel" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Broken%20Clamp%20Body%20Swivel.jpg" width="400">

Once all support is removed, file down the inside face of between the top and bottom until mostly smooth.

<img alt="Smooth inside face" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Filed%20Smooth%20Clamp%20Body.jpg" width="400">

Then, use a lighter or heat gun to recolor this segment. Avoid severely melting or warping the part.

\
<img alt="Using lighter to recolor Clamp Body 1" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Using%20Fire%20to%20Recolor%20Clamp%20Body.jpg" width="400">
<img alt="Using lighter to recolor Clamp Body 2" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Using%20Fire%20to%20Recolor%20Clamp%20Body%20(progress).jpg" width="400">
\
<img alt="Successfully recolored 1" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Successfully%20Recolored%20Clamp%20Body%201.jpg" width="400">
<img alt="Successfully recolored 2" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Successfully%20Recolored%20Clamp%20Body%202.jpg" width="400">

<img alt="Warped Clamp Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Warped%20Recolor%20Attempt.jpg" width="400">

After this, use a 3/8" - 16 or 3/8" - 24 inside tapping tool to thread the hole for the screw

\
<img alt="Tapping Clamp Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Tapping%20Clamp%20Body.jpg" width="400">
<img alt="Completed Clamp Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Finished%20Clamp%20Body.jpg" width="400">

**Clamp Screw**

 Remove supports, file down the face under the head of the screw. Then, use a 3/8" - 16 or a 3/8" - 24 (must be same as used on clamp body) outside tapping tool to thread the screw. Use pliers to grip close to the tapping tool to prevent breaking the part. once your pliers run out of room above the tapping tool, position them below, and keep tapping. Don't worry about grooves left by the pliers, as the tapping tool will mostly fix this on the way back down.

<img alt="Tapping with pliers close to tap" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Pliers%20Close%20to%20Tapping%20Device%20on%20Clamp%20Screw.jpg" width="400">

I cannot tap with the pliers on top anymore\
<img alt="Reason for switched grip" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Reason%20for%20Switched%20Grip.jpg" width="400">

Switched to pliers under (switch-grip):\
<img alt="Switched grip tapping" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Final%20Position%20of%20Tapping%20Device%20Clamp%20Screw.jpg" width="400">

Tapping device at final position:\
<img alt="Final position of the tapping device" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Final%20Position%20of%20Tapping%20Device.jpg" width="400">

Completed Tap:\
<img alt="Finished tap" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Finished%20Clamp%20Screw.jpg" width="400">

Clearing the hole:\
<img alt="Clearing material from peg hole on Clamp Screw" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Removing%20Material%20from%20Peg%20Slot%20on%20Clamp%20Screw.jpg" width="400">

Finally, use a lighter or a heat gun to recolor the screw. Use caution and quick sweeps, as this part warps very easily.

<img alt="Recoloring Clamp Screw" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Recoloring%20Clamp%20Screw.jpg" width="400">

You can now screw the Clamp Screw into the Clamp Body

<img alt="Clamp screw and clamp body connected" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Clamp%20Screw%20and%20Clamp%20Body%20together.jpg" width="400">

**Clamp Screw Bottoms**

Remove supports as usual, lightly file the pegs to remove roughness and add chamfer to the pegs.

<img alt="Lightly filed and chamfered pegs" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Chamfered%20Pegs%20on%20Clamp%20Screw%20Bottom%20-%20Male.jpg" width="400">

On the female side, remove supports and make sure there is no residual material in the holes.

<img alt="Finished Clamp Screw Bottom - F" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Finished%20Clamp%20Screw%20Bottom%20-%20Female.jpg" width="400">

Then gently place the two halves together, making sure not to completely attach the two sides as they should only go together with a lot of force. Remove material from the pegs until the first quarter of the pegs can go into the holes. Again, the fit is intended to be tight, and not be assembled until the final installation with the clamp screw. Once ready, screw the Clamp Screw into the Clamp Body, then run the center peg of the male Clamp Screw Bottom through the hole at the bottom of the Clamp Screw.

<img alt="Clamp assembly with only Clamp Bottom - Male" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Clamp%20Assembly%20with%20only%20Male%20Bottom.jpg" width="400">

Then line up the female side of the Clamp Screw Bottom with the male side and use pliers to press fit the sides together. If the female side starts warping excessively, gently remove using a knife or wedge to separate the parts, then file the pegs again. Repeat until fits properly.

\
<img alt="Assembling the bottoms with Clamp Screw and Clamp Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Assembling%20Clamp%20Screw%20Bottoms%20with%20Clamp%20Screw.jpg" width="400">
<img alt="Completed Clamp Body assembly" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Completed%20Clamp%20Body%20Assembly.jpg" width="400">

 ### Assembly + Notes:
   
   Once all the parts are clean and free of supports, begin test-fitting each piece together. The two halves of the main body should fit easily, but some areas may require more work.
      
   The slot for the thumbstick board on the left side of the body is prone to getting clogged by supports, so be sure to adjust for that in slicer settings or attend to that in post-processing. Aside from that, once support material is removed from the slots, all the electronics should slide in fairly easily. (There are often differences in tolerance between printers, so the previous statement may only apply to my machine)
   
   After all tolerance issues are resolved, assembly can begin. To start, I normally begin with the electronics and place the right-click button first, but feel free to install in whichever order makes the most sense.\
   NOTE: When bending wires and installing the electronics, it is typical to break a solder joint or two. Use care when bending the wires and have a soldering iron on standby just in case.
   #### Right Mouse Button
   I normally use my automotive picks to slot the button in place, and use another pick or an unwound paper clip to check if the button clicks as intended.

   \
   <img alt="Slotting right click button in place using automotive pick (button not highlighted)" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Installing%20Right%20Click%20Button%20(Not%20Highlighted).jpg" width="400">
   <img alt="Slotting right click button in place using automotive pick (button highlighted)" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Installing%20Right%20Click%20Button%20(Highlighted).jpg" width="400">
   
   Checking click with a paper clip:\
   <img alt="Checking click with a paper clip" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Checking%20Right%20Click%20Button%20With%20Paper%20Clip.jpg" width="400">
   
   Once in place, add super glue to where the button meets the plastic shell on the back right side of the button, making sure to avoid gluing the button open (where it refuses to depress).
   
   <img alt="Gluing the right click button in place" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Gluing%20in%20Right%20Click%20Button.jpg" width="400">
   
   #### Raspberry Pi Pico
   
   After installing the left click, I normally slot in the Pico. Make sure that no wires are being pinched between the wall of the body and the pico, and simply slot it in. (Be sure the glue is dry if you are worried about the wires pulling the right mouse button out of place)
   
   <img alt="Pico slotted in place" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Pico%20Slotted.jpg" width="400">
   
   #### Left Mouse Button
   Before installing the left mouse button, I usually bend the thumbstick under the body to get it out of the way. 
   
   <img alt="Thumbstick bent under the body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Bending%20Thumbstick%20Under%20Body.jpg" width="400">
   
   From there, it is a matter of bending wires and positioning the button in the slot. After this, install the thumbstick as described below, then put the two sides together and make sure the button and thumbstick align properly on both sides. If everything fits properly, you can use super glue to attach the button to the left side of the body if desired (be careful not to glue the two halves of the body together).

   <img alt="Left click button installed" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Left%20Click%20Button%20Installed.jpg" width="400">

  #### Rotary Encoder
   
   Slide the scroll wheel assembly from earlier into the designated slot. This too should be relatively effortless once positioned correctly (which sometimes takes some time), and if it isn't, file the encoder slot in the Left Body down and then retry.

   \
   <img alt="Scroll Wheel assembly being installed" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Installing%20Scroll%20Wheel%20Assembly.jpg" width="400">
   <img alt="Scroll Wheel assembly fully installed" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Scroll%20Wheel%20Assembly%20Installed.jpg" width="400">
   
   #### Thumb Stick
   
   Simply slide into the slots on the left side of the body. Support material often gets clogged in there, so some clearancing may be necessary.
   
   <img alt="Attaching the Thumbstick to the Left Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Thumbstick%20Base%20Installed%20in%20Left%20Body.jpg" width="400">

   After this, try attaching the Right Body to check the fit of the left click button and the Thumbstick. The wires going to the Thumbstick board may need to be bent out of the way. When bending these wires, be sure to separate the power wire from the others. When this wire gets squeezed against the x and y axis wires it can sometimes cause interference that causes the cursor to behave erratically and uncontrollably.

   \
   <img alt="Arranging wires before fitting together" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Arranging%20Wires%20After%20Electronics%20Installed.jpg" width="400">
   <img alt="Attaching the two sides" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Two%20Sides%20Fit%20Check%20With%20LMB%20and%20Thumbstick.jpg" width="400">
   
   #### Attaching the Cable
   
   After all of the electronics are installed, I typically run the cable through the clamp body, then plug it into the pico. If the head of the USB Micro end of the cable doesn't fit in the provided hole in the clamp body, then shave off some of the rubber at the head. To avoid exposing wires, give around a millimeter on all sides of the plug.

   The cable head doesn't fit through the Clamp Body:\
   <img alt="Cable head does not fit" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Cable%20Head%20Does%20Not%20Fit.jpg" width="400">

   \
   <img alt="Shaving the cable head" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Shaving%20Head.jpg" width="400">
   <img alt="Shaved head" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Shaved%20Head.jpg" width="400">
   <img alt="Shaved head through Clamp Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Shaved%20Head%20Through%20Clamp%20Body.jpg" width="400">
   
   From there, I normally have to use pliers to install the cable into the Pico due to the rubber head hitting the roof of the body.
   
   <img alt="Attaching the cable head to the Pico with pliers" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Attaching%20Cable%20to%20Pico%20with%20Pliers.jpg" width="400">

   Finally, I route the wires and attach the Clamp Body to the Left Body, securing it with the Clamp Port Cap.

   \
   <img alt="Routing the cable" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Cable%20Routing.jpg" width="400">
   <img alt="Attaching Clamp Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Cable%20Routed%20and%20Clamp%20Body%20Attached.jpg" width="400">
   <img alt="Secure with Clamp Port Cap" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Clamp%20Port%20Cap%20Installed%20Not%20Filed.jpg" width="400">

   File down the Clamp Port Cap so that it will sit flush:\
   <img alt="File down Clamp Port Cap so it sits flush" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Clamp%20Port%20Cap%20Filed%20and%20Installed.jpg" width="400">
   
   #### Installing the Triggers and Thumbstick Cover
   
   To begin the process, I normally start with the Left Click Trigger, as it is the last piece needed to attach the two halves. To install the trigger, first, double check that the space between the end of the slide limiters and the electronic button is slightly too long. In this case, just cut off material from the tip.

   The tip of the Left Click Trigger is slightly too long\
   <img alt="Why I needed to cut off the tip of the Left Click Trigger" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Why%20Left%20Click%20Trigger%20Tip%20Needs%20Cutting.jpg" width="400">

   \
   <img alt="Cutting off tip of Left Click Trigger" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Cutting%20Tip%20Off%20Left%20Click%20Trigger.jpg" width="400">
   <img alt="Severed tip of Left Click Trigger" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Severed%20Left%20Click%20Trigger%20Tip.jpg" width="400">
   <img alt="Corrected fit of Left Click Trigger with Left Body" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Left%20Click%20Trigger%20Properly%20Fitted.jpg" width="400">
   
   From there, simply place the trigger in the half with all the electronics, and attach the other side.

   \
   <img alt="Preparing to connect the two sides" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Installing%20Left%20Click%20Trigger.jpg" width="400">
   <img alt="Two halves connected" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Left%20Click%20Trigger%20Installed%20Fit%20Check.jpg" width="400">
   
   Assuming the trigger still works as desired and slides well, you can use the 3/4" screws to secure the two halves together.

   \
   <img alt="Installing first screw" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Screwing%20in%20%234%20-%203_4_%20Machine%20Screw.jpg" width="400">
   <img alt="All screws installed" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/All%20Screws%20Attached.jpg" width="400">

   

   After both sides are attached, transition to the Right Click Trigger. The main point of struggle with this piece is the extender for the plunger. This part prints attached to a long handle for easier filing and adjustment. Using the handle, push the Plunger Extender into the hole on the left side of the body.
   
   <img alt="Original Plunger Extender fit check using handle" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Initial%20Fit%20Check%20of%20Plunger%20Extender.jpg" width="400">
   
   If any resistance is encountered, stop immediately, gently remove the extender and file down in the areas that were causing struggle.

   \
   <img alt="Filing down Plunger Extender" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Filing%20Plunger%20Extender.jpg" width="400">
   <img alt="Re-checking Plunger Extender fit after filing" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Re-Checking%20Plunger%20Extender%20Fit%20Using%20Handle.jpg" width="400">
   
   Repeat this process as needed. Once the extender is satisfactory, cut off the handle and place the extender in the hole with the center of the torus segment facing the front of the device.

\
   <img alt="Severing the handle from the Plunger Extender" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Cutting%20Handle%20off%20Plunger%20Extender.jpg" width="400">
   <img alt="Installing the Plunger Extender in the hole with the torus diagram" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Installing%20Plunger%20Extender%20with%20Torus%20Diagram.jpg" width="400">
   <img alt="Plunger Extender fully installed" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Plunger%20Extender%20Installed.jpg" width="400">
   
   Once this is complete, simply attach the Right Click Trigger as shown previously.

   \
   <img alt="Installing Right Click Trigger" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Installing%20Right%20Click%20Trigger.jpg" width="400">
   <img alt="Right Click Trigger installed" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Right%20Click%20Trigger%20Installed.jpg" width="400">



   Finally, it is time for the Thumbstick Cover. This part can be tricky to get right, but focus on not removing too much material from the hole in the Thumbstick Cover, else it will become wobbly during use. Align the hole of the cover with the stick of the Thumbstick, and try to press on. This takes some force, but if it will not attach, start removing material from the hole. The hole is ovular, so avoid using drills.

   <img alt="Adjusting Thumbstick Cover" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Adjusting%20Thumbstick%20Hole.jpg" width="400">
   
   If you printed this with less walls, the added flex of the material should assist with installation. If not, keep removing material until you are able to press the thumstick in place. Once installed, if you desire, you can add super glue to secure the cover.
   
   <img alt="Thumbstick Cover fully installed" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Thumbstick%20Cap%20Installed.jpg" width="400">

   #### Top Cover
   The final step is to attach the Top Cover. Simply align the screw holes with those on the body, and insert the screws. Before packing up your tools, make sure that the thumbstick moves with the desired freedom, the scroll wheel scrolls easily, and everything works correctly when plugged in to your computer.

## Final Results

<img alt="Finished Project alone" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Finished%20Project%20alone.jpg" width="700">

<img alt="Finished Project in hand" src="https://github.com/InsaneDev27/DIY-Laptop-Mouse-Project/blob/main/images/Finished%20Project%20in%20Hand.jpg" width="700">

## Conclusion and Final Thoughts

Overall, this project has been a blast for me. I now have a working device that I can use as a mouse whenever I want to use my laptop on my lap. I accomplished what I set out to do. I have learned a lot through this project and there are many ways in which I would approach it differently were I to restart. While this is as far as I am willing to take the concept and project, my hope is that you or someone like you will find this project and modify it or use it as inspiration to create the next generation of Laptop Mouse Projects. If you choose to take that path, I would love if you would share it with me through GitHub. I hope that you have enjoyed this project as much as I have, and Happy Making!

This project is licensed under the [MIT License](LICENSE). See the [LICENSE-MIT](LICENSE-MIT) for further information.
All STL files and images are licensed under the [CC-BY-SA-4.0](LICENSE-CC-BY-SA-4.0). See [LICENSE-CC-BY-SA-4.0](LICENSE-CC-BY-SA-4.0)
