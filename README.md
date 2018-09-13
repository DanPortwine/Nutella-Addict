# Nutella Addict

Files:

The .zip file contains an .exe version of the game as well as some starter maps. If you just want to play the game then download and extract this file then run the .exe.
The .py file can be run if you have python installed as well as the required modules: random, time, os, winsound, colorama, smtplib, email.mime.multipart and email.mime.text.

! USE THE NUMPAD ON YOUR KEYBOARD FOR THE BEST EXPEREIENCE !

Note: This game uses a command line interface (not a GUI). This has severely limited the possibilities for this project.

When you first load the game, it asks for your desired window size. Choose by entering the corresponding number and hitting enter.

On the main menu screen, there are 6 options which each have a corresponding number for you to enter.

1 - Begin game
  By selecting this option you will be able to select a map from a list of .csv files found in /maps. The file size for each map is shown with its name to let you know whether it will be a large or small map. After selecting your map you will be shown the map if it is small enough to fit on your selected window size. There is a key below the map to show what each tile represents. Once you are satisfied with looking at the map, hit enter to continue.
  
2 - Map creator
  By selecting this optionsyou will be able to choose from 3 styles of map or to return to the main menu. After selecting a map style you will be asked to enter the dimensions of the map. If you want to be able to see a preview of the map you must make your dimensions no larger than the displayed limits (depending on your current window size). Once you have entered your desired dimensions a preview will be displayed (if your window resolution allows) as well as the tile key. It will display how long the generation took and ask if you want to save the map. If you select to save the map by entering 'y' then it will ask for the name of the map with a limit of 10 characters. Once the name is entered you will return to the main menu.
  
3 - Instructions
  By selecting this option you will be shown the controls for movement and actions in the game as well as the objectives and the tiles key. Once you are done hit enter to return to the main menu.
  
4 - Options
  By selecting this option you will be able to select the window size. Once you have selected your window size you will return to the main menu.
  
5 - Support/feedback (removed from .py)
  By selecting this option you will be asked to enter your name then optionally your email (in-case a response is desired, if a response isn't then just hit enter to skip). Then enter the message you wish to send. Once it has sent you will return to the main menu.
  
6 - Exit
  By selecting this option the game will close.
  
  
The gameplay:

You will see a 5x5 tile section of your surroundings, with you being on the central tile along with your health, hunger and thirst stats. Use the numpad keys to move tiles and explore the map. Your movement is limited when you first start out to Grassland, Forest and Stone. To move over Mountain or Water you need to craft a Rope or Boat respectively. 
You can enter 'p' to pick the current tile you are on which will provide you with resources relevant to the tile type. These resources can be used for crafting items. Once you have picked on a tile, you must move to different tiles several times before you can pick from that tile again. 
You can enter 'h' to hunt on a tile which will give you 3 options for hunting: bare hand - a chance to catch a turkey; bow - a chance to get a grey squirrel or turkey but requires you to have crafted a bow and have arrows; spear - a chance to get deer or wolf but requires you to have crafted a spear. Animals that are caught can be eaten to recover Hunger. 
You can enter 'c' to be shown the controls, objectives and tiles key (same as '3 - Instructions' but returns to game rather than main menu). 
You can enter 'i' to select crafting or view your inventory. There are 3 categories of items: Tools - items that can be used to advance your progress in the game; Items - items that are used in crafting or aids to help progress the game; Food/Drink - items which can be eaten/drunk to recover Hunger or Thirst respectively. Each item you can craft shows the type and amount of the items that are needed to craft it. When in your inventory you will see the amount of each item that you currently have.
You can enter 'f' to select an item of food/drink to consume. The amount you have and the amount of Hunger/Thirst each food item replenishes is also shown.
You can enter 'l' when on a mountain tile to use a Trig Point which will display coordinates relative to your current tile to where the Jar is.
The main objective of the game is to craft a breadstick and a jar of Nutella and then consume a Nutella coated breadstick. In order to do this you must collect Wheat to craft a Breadstick (which can also be eaten for Hunger recovery); Sugar, Hazelnuts and the Jar (placed on a random tile at the start of a new game) to craft the Jar of Nutella.
Once a game has been completed, the map that was used will now create a new game when selected from the '1- Begin game' option.
