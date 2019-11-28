==================================
           Mac Gyver Maze
==================================

----------------------------------
       Goal of the game
----------------------------------
    This is a game where you drive Mac Gyver out of a maze. For that you have to drive Mac Gyver with arrows (down, up, left and right). 
    But at the exit, a dangerous Guard block the passage. To reach the exit you must gather three objet, a needle, a tube and a flask of ether. Thanks to this three objets, because you are Mac Gyver, you will be able to make a syringe full of ether to get to sleep the guard. Without this three objet your meet with the guard will be lethal. 

----------------------------------
    Organisation of the Code
----------------------------------
    All files for modules are in the same folder. In this main folder the folder assets contain sub folder: fonts, images, music and sounds, which contain files useful for the game. 
    The program is composed be one main files (main.py) and six modules. 
    + The main.py files contain the main function for general game cook: initialisation of the game, instantiation of objet, calls of different methods, the loop to listen user command…
    + The maze.py contain a class TheMaze wish to allow to control the maze: maze loading from txt files, action in case of victory or death, condition to end the game. This model doesn’t use pygame. 
    + The artefact.py contains the class Artefact which is the mother class for Aiguille class, Tube class and Ether class. The methods of this class allow to represent the artefact in the maze. 
    + The mac_gyver.py model contain class with methods for load Mac Gyver in the maze, move Mac Gyver, gather the artefact. 
    + The constantes.py modules contain constants variable useful for the program. 
    + The build_maze.py modules contain mother class and daughter class which use pygame to display the maze and maze elements (artefact, Mac Gyver and Guard) in pygame screen. 
    + The sound_music_and_messages.py model contains class with method working with pygame for play music of sound and display message on the screen. 
    
----------------------------------
      How to launch the game
----------------------------------
    This game was tested on a computer running with Linux Mint 19.1 Cinnamon. This game was developed in a virtual environment under Python 3.7.O and pygame 1.9.6 (as describe in requierment.txt file). 
    The common behaviour for running the game, consists to go in the folder containing the main.py files with a terminal. Then enter the command ‘python3 main.py’ and it should work…

