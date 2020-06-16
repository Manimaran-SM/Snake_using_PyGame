<h1 align="center">
  <img src="https://im.indiatimes.in/media/content/2018/Aug/snake_game_1533210447.jpg" alt="Snake Game"><br>
  Snake_using_PyGame
</h1>

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/Manimaran-SM/Snake_using_PyGame/blob/master/LICENSE)

* [Overview](#Overview)
   * [Introduction](#Introduction)
   * [PyGame](#PyGame)
   * [Challenges Faced](#Challenges_Faced)
   * [Limitation](#Limitation)
   
* [Guide](#Guide)
  * [Procedure](#Procedure)
  * [Pre-requisite](#Prerequisite)


# Overview:
## Introduction
>* Snake is the common name for a video game concept where the player maneuvers a line which grows in length, with the line itself being a primary obstacle. 
>* The player controls a dot, square, or object on a plane. As it moves forward, it leaves a trail behind, resembling a moving snake. In this game, the end of the trail is not a fixed position, so the snake continually gets longer as it moves. and there is a moving tail a fixed number of units away from the head which is the apple being eaten. The player loses when the snake runs into the screen border, a trail or other obstacle, or itself.
>* There is an apple in the game which the snake eats to get bigger. Apple spawns randomly at any place within the boundary of the game. Though it is not an advanced version of the snake game. it sure is a replica of the basic version.

## PyGame
>* Pygame is a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language.
Pygame is highly portable and runs on nearly every platform and operating system.
>* <b>Multi core CPUs can be used easily.</b> With dual core CPUs common, and 8 core CPUs cheaply available on desktop systems, making use of multi core CPUs allows you to do more in your game. Selected pygame functions release the dreaded python GIL, which is something you can do from C code.
>* <b>Uses optimized C and Assembly code for core functions.</b> C code is often 10-20 times faster than python code, and assembly code can easily be 100x or more times faster than python code.
>* <b>Comes with many operating systems.</b> Just an apt-get, emerge, pkg_add, or yast install away. No need to mess with installing it outside of your operating system's package manager. Comes with binary pos system installers (and uninstallers) for Windows or MacOSX. Pygame does not require setup tools with even ctypes to install.
>* <b>Truly portable.</b> Supports Linux (pygame comes with most main stream linux distributions), Windows (95, 98, ME, 2000, XP, Vista, 64-bit Windows, etc), Windows CE, BeOS, MacOS, Mac OS X, FreeBSD, NetBSD, OpenBSD, BSD/OS, Solaris, IRIX, and QNX. The code contains support for AmigaOS, Dreamcast, Atari, AIX, OSF/Tru64, RISC OS, SymbianOS and OS/2, but these are not officially supported. You can use it on hand held devices, game consoles and the One Laptop Per Child (OLPC) computer.
>* <b>It's Simple and easy to use</b>. Kids and adults make shooter games with pygame. Pygame is used in the OLPC project and has been taught in essay courses to young kids and college students. It's also used by people who first programmed in z80 assembler or c64 basic.
>* <b>Does not require a GUI to use all functions.</b> You can use pygame from a command line if you want to use it just to process images, get joystick input, or play sounds.
>* <b>Fast response to reported bugs.</b> Some bugs are patched within an hour of being reported. Do a search on our mailing list for BUG... you'll see for yourself. Sometimes we suck at bug fixes, but mostly we're pretty good bug fixers. Bug reports are quite rare these days, since a lot of them have been fixed already.
>* <b>Small amount of code.</b> It does not have hundreds of thousands of lines of code for things you won't use anyway. The core is kept simple, and extra things like GUI libraries, and effects are developed separately outside of pygame.
>* Refer this site for any PyGame related modules [info](https://devdocs.io/pygame/).

## Challenges_Faced
>* Figuring out the dimension was a quite a tough task. 

## Limitation
>* It has a bit of an issue when the snake figure goes out of the border it doesn't gets game over until you press a key.

# Guide:
## Procedure
>* Click clone/download
>* If you github desktop click open in desktop hit the clone button. 
>* If you use download zip, then extract the zip file  
>* If you want to use HTTPS say (https://github.com/Manimaran-SM/Snake_using_PyGame.git), then use the command
``` 
$ git clone https://github.com/Manimaran-SM/Snake_using_PyGame.git
```
>* After completing the above steps, Now run the [snake_game.py](https://github.com/Manimaran-SM/Snake_using_PyGame/blob/master/snake_game.py) file. 
>* You wil get output as shown below.
>* If you have any problems regarding this repository while opening feel free ask me [here](https://github.com/Manimaran-SM/Snake_using_PyGame/issues/new)

## Output:
<p align="center">
  <img src="https://github.com/Manimaran-SM/Snake_using_PyGame/blob/master/output1.png" height="400" width="800" alt="Output">
  <br>
  <img src="https://github.com/Manimaran-SM/Snake_using_PyGame/blob/master/output.png" height="400" width="800" alt="Output">
</p>

### Note:
* If you have problem related with git command refer this documentation [link](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

## Prerequisite
Install PyGame with:

```
pip install pygame
```
## Note:
>* Given commands works only for windows.
>* python IDE and Following packages must be installed in system.
    
