import os, time
from os import system, name

# Initialised Variables
global slc1, slc2, slc3, slc4, slc5, slc6, slc7, slc8
slc1 = False
slc2 = False
slc3 = False
slc4 = False
slc5 = False
slc6 = False
slc7 = False
slc8 = False

def clr():
    if name == 'nt':
        system('cls')
    
    else:
        system('clear')
# add middlepart calc
def pizzadrawingengine():
    global slc1, slc2, slc3, slc4, slc5, slc6, slc7, slc8

    if slc1: # first slice
        slice1part1 = "__.--'¨¨¨¨¨'--.__"
        slice1part2 = "'¨  ___,.---.,___  ¨'"
        slice1part3 = "'¨¨             ¨¨'"
        slice1part4 = "    o  o    o    "
        slice1part5 = " o  o   o    o "
        slice1part6 = "  o  o   o   "
        slice1part7 = "     o   o "
        slice1part8 = " o   o   "
        slice1part9 = "  o  o "
        slice1part10 = " o   "
        slice1part11 = "  o"
        slice1part12 = " "

    else:
        slice1part1 = ""
        slice1part2 = "                     "
        slice1part3 = "                   "
        slice1part4 = "                 "
        slice1part5 = "               "
        slice1part6 = "             "
        slice1part7 = "           "
        slice1part8 = "         "
        slice1part9 = "       "
        slice1part10 = "     "
        slice1part11 = "   "
        slice1part12 = " "

    if slc2: # second slice
        slice2part1 = "-._"
        slice2part2 = "_  '-."
        slice2part3 = "  '-.  '-."
        slice2part4 = "o     '-.  '."
        slice2part5 = "o  o  o   '.  '."
        slice2part6 = "  o   o o    '.  \\"
        slice2part7 = "  o  o     o    \  \\"
        slice2part8 = "o     o    o  o "
        slice2part9 = "   o o  o  "
        slice2part10 = "o o  o"
        slice2part11 = " "

    else:
        slice2part1 = ""
        slice2part2 = ""
        slice2part3 = ""
        slice2part4 = ""
        slice2part5 = ""
        slice2part6 = ""
        slice2part7 = ""
        slice2part8 = "                "
        slice2part9 = "           "
        slice2part10 = "      "
        slice2part11 = " "

    if slc3: # third slice
        slice3part1 = "\\"
        slice3part2 = "   .  |"
        slice3part3 = "o   o     . '."
        slice3part4 = "o  o    o   o   ]  ]"
        slice3part5 = "   o    o  o    o     ]  ]"
        slice3part6 = "o    o   o  o   ]  ]"
        slice3part7 = "o   o     . .'"
        slice3part8 = "   '  |"
        slice3part9 = "/"

    else:
        slice3part1 = ""
        slice3part2 = ""
        slice3part3 = ""
        slice3part4 = ""
        slice3part5 = ""
        slice3part6 = ""
        slice3part7 = ""
        slice3part8 = ""
        slice3part9 = ""

    if slc4: # fourth slice
        slice4part1 = "o"
        slice4part2 = " o  o "
        slice4part3 = "  o   o  o "
        slice4part4 = "    o     o   o "
        slice4part5 = " o    o   o     /  /"
        slice4part6 = "  o    o     .'  /"
        slice4part7 = "o    o    .'  .'"
        slice4part8 = " o    .-'  -'"
        slice4part9 = "  .-'  .-'"
        slice4part10 = "¨  .-'"
        slice4part11 = "-'¨"

    else:
        slice4part1 = " "
        slice4part2 = "      "
        slice4part3 = "           "
        slice4part4 = "                "
        slice4part5 = ""
        slice4part6 = ""
        slice4part7 = ""
        slice4part8 = ""
        slice4part9 = ""
        slice4part10 = ""
        slice4part11 = ""

    if slc5: # fifth slice
        slice5part1 = " "
        slice5part2 = " o "
        slice5part3 = "   o "
        slice5part4 = " o     "
        slice5part5 = "    o  o "
        slice5part6 = "  o    o   "
        slice5part7 = "     o     o "
        slice5part8 = "o    o    o   o"
        slice5part9 = "       o  o   o  "
        slice5part10 = ".__             __."
        slice5part11 = "._  ¨¨¨`'---'´¨¨¨  _."
        slice5part12 = "¨¨'--,_____,--'¨¨"

    else:
        slice5part1 = " "
        slice5part2 = "   "
        slice5part3 = "     "
        slice5part4 = "       "
        slice5part5 = "         "
        slice5part6 = "           "
        slice5part7 = "             "
        slice5part8 = "               "
        slice5part9 = "                 "
        slice5part10 = "                   "
        slice5part11 = "                     "
        slice5part12 = ""

    if slc6: # sixth slice
        slice6part1 = " "
        slice6part2 = "o   o "
        slice6part3 = "   o    o  "
        slice6part4 = "  o    o   o   o"
        slice6part5 = "\  \     o    o     "
        slice6part6 = "\  '.       o  o  "
        slice6part7 = "'.  '.       o  "
        slice6part8 = "'.  '-.      "
        slice6part9 = "'-.  '-.  "
        slice6part10 = "'-.  ¨"
        slice6part11 = "¨'-"

    else:
        slice6part1 = " "
        slice6part2 = "      "
        slice6part3 = "           "
        slice6part4 = "                "
        slice6part5 = "                    "
        slice6part6 = "                  "
        slice6part7 = "                "
        slice6part8 = "             "
        slice6part9 = "          "
        slice6part10 = "      "
        slice6part11 = "   "

    if slc7: # seventh slice
        slice7part1 = "/"
        slice7part2 = "|  .  o"
        slice7part3 = ".' '  o   o   "
        slice7part4 = "[  [    o  o  o    o"
        slice7part5 = "[  [     o      o    o   o"
        slice7part6 = "[  [   o   o   o  o "
        slice7part7 = "'. .    o  o  "
        slice7part8 = "|  '   "
        slice7part9 = "\\"

    else:
        slice7part1 = " "
        slice7part2 = "       "
        slice7part3 = "              "
        slice7part4 = "                    "
        slice7part5 = "                          "
        slice7part6 = "                    "
        slice7part7 = "              "
        slice7part8 = "       "
        slice7part9 = " "

    if slc8: # eight slice
        slice8part1 = "_.-"
        slice8part2 = ".-'  _"
        slice8part3 = ".-'  .-'  "
        slice8part4 = ".'  .-'     o"
        slice8part5 = ".'  .'    o o   "
        slice8part6 = "/  .'    o  o  o  "
        slice8part7 = "/  /   o      o    o"
        slice8part8 = " o   o  o    o  "
        slice8part9 = " o   o   o "
        slice8part10 = "  o  o"
        slice8part11 = " "

    else:
        slice8part1 = "   "
        slice8part2 = "      "
        slice8part3 = "          "
        slice8part4 = "             "
        slice8part5 = "                "
        slice8part6 = "                  "
        slice8part7 = "                    "
        slice8part8 = "                "
        slice8part9 = "           "
        slice8part10 = "      "
        slice8part11 = " "

    if slc1 or slc2: # first line
        line1part1 = "/"
        line1part2 = "/"
        line1part3 = "/"
        line1part4 = "/"
        line1part5 = "/"
        line1part6 = "/"
        line1part7 = "/"
        line1part8 = "/"
        line1part9 = "/"
        line1part10 = "/"

    else:
        line1part1 = " "
        line1part2 = " "
        line1part3 = " "
        line1part4 = " "
        line1part5 = " "
        line1part6 = " "
        line1part7 = " "
        line1part8 = " "
        line1part9 = " "
        line1part10 = " "

    if slc2 or slc3: # second line
        line2part1 = "_.--'"
        line2part2 = "_.--'¨"
        line2part3 = "_.--'¨"
        line2part4 = "_.--'¨"

    else:
        line2part1 = "     "
        line2part2 = "      "
        line2part3 = "      "
        line2part4 = "      "

    if slc3 or slc4: # third line
        line3part1 = "¨'--._"
        line3part2 = "¨'--._"
        line3part3 = "¨'--._"
        line3part4 = "¨'--."

    else:
        line3part1 = "      "
        line3part2 = "      "
        line3part3 = "      "
        line3part4 = "     "

    if slc4 or slc5: # fourth line
        line4part1 = "\\"
        line4part2 = "\\"
        line4part3 = "\\"
        line4part4 = "\\"
        line4part5 = "\\"
        line4part6 = "\\"
        line4part7 = "\\"
        line4part8 = "\\"
        line4part9 = "\\"
        line4part10 = "\\"

    else:
        line4part1 = " "
        line4part2 = " "
        line4part3 = " "
        line4part4 = " "
        line4part5 = " "
        line4part6 = " "
        line4part7 = " "
        line4part8 = " "
        line4part9 = " "
        line4part10 = " "

    if slc5 or slc6: # fifth line
        line5part1 = "/"
        line5part2 = "/"
        line5part3 = "/"
        line5part4 = "/"
        line5part5 = "/"
        line5part6 = "/"
        line5part7 = "/"
        line5part8 = "/"
        line5part9 = "/"
        line5part10 = "/"

    else:
        line5part1 = " "
        line5part2 = " "
        line5part3 = " "
        line5part4 = " "
        line5part5 = " "
        line5part6 = " "
        line5part7 = " "
        line5part8 = " "
        line5part9 = " "
        line5part10 = " "

    if slc6 or slc7: # sixth line
        line6part1 = "_.--'¨"
        line6part2 = "_.--'¨"
        line6part3 = "_.--'¨"
        line6part4 = ".--'¨"

    else:
        line6part1 = "      "
        line6part2 = "      "
        line6part3 = "      "
        line6part4 = "     "

    if slc7 or slc8: # seventh line
        line7part1 = "'--._"
        line7part2 = "¨'--._"
        line7part3 = "¨'--._"
        line7part4 = "¨'--._"

    else:
        line7part1 = "     "
        line7part2 = "      "
        line7part3 = "      "
        line7part4 = "      "

    if slc8 or slc1: # eight line
        line8part1 = "\\"
        line8part2 = "\\"
        line8part3 = "\\"
        line8part4 = "\\"
        line8part5 = "\\"
        line8part6 = "\\"
        line8part7 = "\\"
        line8part8 = "\\"
        line8part9 = "\\"
        line8part10 = "\\"

    else:
        line8part1 = " "
        line8part2 = " "
        line8part3 = " "
        line8part4 = " "
        line8part5 = " "
        line8part6 = " "
        line8part7 = " "
        line8part8 = " "
        line8part9 = " "
        line8part10 = " "

    if slc1 or slc2 or slc3 or slc4 or slc5 or slc6 or slc7 or slc8:
        mid2 = "·"

    else:
        mid2 = " "

    if (slc6 and slc8) or slc7:
        mid1 = ":="

    elif (slc8 and not (slc6 and slc7)):
        mid1 = "¨-"

    elif (slc6 and not (slc7 and slc8)):
        mid1 = "_-"

    else:
        mid1 = "  "

    if (slc2 and slc4) or slc3:
        mid3 = "=:"

    elif (slc2 and not (slc3 and slc4)):
        mid3 = "-¨"

    elif (slc4 and not (slc2 and slc3)):
        mid3 = "-_"

    else:
        mid3 = "  "

    middlepart = mid1 + mid2 + mid3
    print("                    " +                                       slice1part1)
    print("               " +               slice8part1  +               slice1part2  +               slice2part1)
    print("            " +                  slice8part2  + line8part1  + slice1part3  + line1part1  + slice2part2)
    print("         " +                     slice8part3  + line8part2  + slice1part4  + line1part2  + slice2part3)
    print("       " +                       slice8part4  + line8part3  + slice1part5  + line1part3  + slice2part4)
    print("     " +                         slice8part5  + line8part4  + slice1part6  + line1part4  + slice2part5)
    print("    " +                          slice8part6  + line8part5  + slice1part7  + line1part5  + slice2part6)
    print("   " +                           slice8part7  + line8part6  + slice1part8  + line1part6  + slice2part7)
    print("  " + slice7part1 + line7part1 + slice8part8  + line8part7  + slice1part9  + line1part7  + slice2part8  + line2part1 + slice3part1)
    print(" " +  slice7part2 + line7part2 + slice8part9  + line8part8  + slice1part10 + line1part8  + slice2part9  + line2part2 + slice3part2)
    print(       slice7part3 + line7part3 + slice8part10 + line8part9  + slice1part11 + line1part9  + slice2part10 + line2part3 + slice3part3)
    print(       slice7part4 + line7part4 + slice8part11 + line8part10 + slice1part12 + line1part10 + slice2part11 + line2part4 + slice3part4)
    print(       slice7part5 +                                           middlepart   +                                           slice3part5)
    print(       slice7part6 + line6part1 + slice6part1  + line5part1  + slice5part1  + line4part1  + slice4part1  + line3part1 + slice3part6)
    print(       slice7part7 + line6part2 + slice6part2  + line5part2  + slice5part2  + line4part2  + slice4part2  + line3part2 + slice3part7)
    print(" " +  slice7part8 + line6part3 + slice6part3  + line5part3  + slice5part3  + line4part3  + slice4part3  + line3part3 + slice3part8)
    print("  " + slice7part9 + line6part4 + slice6part4  + line5part4  + slice5part4  + line4part4  + slice4part4  + line3part4 + slice3part9)
    print("   " +                           slice6part5  + line5part5  + slice5part5  + line4part5  + slice4part5)
    print("    " +                          slice6part6  + line5part6  + slice5part6  + line4part6  + slice4part6)
    print("     " +                         slice6part7  + line5part7  + slice5part7  + line4part7  + slice4part7)
    print("       " +                       slice6part8  + line5part8  + slice5part8  + line4part8  + slice4part8)
    print("         " +                     slice6part9  + line5part9  + slice5part9  + line4part9  + slice4part9)
    print("            " +                  slice6part10 + line5part10 + slice5part10 + line4part10 + slice4part10)
    print("               " +               slice6part11 +               slice5part11 +               slice4part11)
    print("                    " +                                       slice5part12)

def main():
    global slc1, slc2, slc3, slc4, slc5, slc6, slc7, slc8, question1, question2, question3, doing
    slc1 = False
    slc2 = False
    slc3 = False
    slc4 = False
    slc5 = False
    slc6 = False
    slc7 = False
    slc8 = False
    clr()
    print()
    print(' PPPPPPPPPPPPPPPPP     iiii')
    print(' P::::::::::::::::P   i::::i')
    print(' P::::::PPPPPP:::::P   iiii        Demo made by Tristan Hafström in MMXX, v.1.0')
    print(' PP:::::P     P:::::P')
    print('   P::::P     P:::::Piiiiiii zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz    aaaaaaaaaaa')
    print('   P::::P     P:::::Pi:::::i z:::::::::::::::zz:::::::::::::::z  aa:::::::::::a')
    print('   P::::PPPPPP:::::P  i::::i z::::::::::::::z z::::::::::::::z  a:::::aaaa:::::a')
    print('   P:::::::::::::PP   i::::i zzzzzzzz::::::z  zzzzzzzz::::::z   aaaaaa    a::::a')
    print('   P::::PPPPPPPPP     i::::i       z::::::z         z::::::z       aaaaaaa:::::a')
    print('   P::::P             i::::i      z::::::z         z::::::z      aa::::::::::::a')
    print('   P::::P             i::::i     z::::::z         z::::::z      a::::aaaa::::::a')
    print('   P::::P             i::::i    z::::::z         z::::::z      a::::a    a:::::a')
    print(' PP::::::PP          i::::::i  z::::::zzzzzzzz  z::::::zzzzzzzza::::a    a:::::a')
    print(' P::::::::P          i::::::i z::::::::::::::z z::::::::::::::za:::::aaaa::::::a')
    print(' P::::::::P          i::::::iz:::::::::::::::zz:::::::::::::::z a::::::::::aa:::a')
    print(' PPPPPPPPPP          iiiiiiiizzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz  aaaaaaaaaa  aaaa')
    print('/_  __/ /  ___   ___/ /__ / _(_)__  (_) /_(_)  _____   / __/__/ (_) /_(_)__  ___')
    print(' / / / _ \\/ -_) / _  / -_) _/ / _ \\/ / __/ / |/ / -_) / _// _  / / __/ / _ \\/ _ \\')
    print('/_/ /_//_/\\__/  \\_,_/\\__/_//_/_//_/_/\\__/_/|___/\\__/ /___/\\_,_/_/\\__/_/\\___/_//_/')
    print('__________________________________________________________________________________')
    print(' New and improved with all new gamemodes and completely revamped rendering system')
    print(' 1. Spin          2. Two-skip Spin')
    print(' 3. Fill          4. Freeplay                                 Type "quit" to quit')
    print()
    ans = input(' > ')
    ans = ans.lower()
    
    if ans == '1':
        doing = 0
        question1 = True
        question2 = True
        question3 = True

        def spinsetup():
            global question1, question2, question3, repeat, startingslices, timing
            clr()
            print('Type amount of skips you want to happen (1 - 500) (type "quit" to exit to main menu):')

            if question1:
                repeat = input(' > ')

                if repeat == "quit" or repeat == "q":
                    main()

                if repeat:
                    if int(repeat):
                        if (int(repeat) < 501) and (int(repeat) > 0):
                            question1 = False
                            repeat = str(int(repeat) + 1)

                        else:
                            spinsetup()
                    else:
                        spinsetup()
                else:
                    spinsetup()
            else:
                print(" > " + str(int(repeat) - 1))

            print()
            print('Type amount of slices you want to begin with (1 - 7) (type "quit" to exit to main menu):')
            
            if question2:
                startingslices = input(' > ')

                if startingslices == "quit" or startingslices == "q":
                    main()

                if startingslices:
                    if int(startingslices):
                        if (int(startingslices) < 8) and (int(startingslices) > 0):
                            question2 = False

                        else:
                            spinsetup()
                    else:
                        spinsetup()
                else:
                    spinsetup()
            else:
                print(' > ' + startingslices)

            print()
            print('Type amount of time you want between skips (0.1 - 2) (type "quit" to exit to main menu):')

            if question3:
                timing = input(' > ')

                if timing == "quit" or timing == "q":
                    main()

                if timing:
                    if float(timing) and (len(timing) < 4):
                        if (float(timing) < 2.1) and (float(timing) > 0):
                            question3 = False

                        else:
                            spinsetup()
                    else:
                        spinsetup()
                else:
                    spinsetup()
            print()
            print('Press "ENTER" to continue: ')
            input(' > ')
        spinsetup()

        def spin():
            global repeat, startingslices, timing, doing, slc1, slc2, slc3, slc4, slc5, slc6, slc7, slc8, question1, question2, question3

            if startingslices == '1':
                slc1 = True

            if startingslices == '2':
                slc1 = True
                slc2 = True

            if startingslices == '3':
                slc1 = True
                slc2 = True
                slc3 = True

            if startingslices == '4':
                slc1 = True
                slc2 = True
                slc3 = True
                slc4 = True

            if startingslices == '5':
                slc1 = True
                slc2 = True
                slc3 = True
                slc4 = True
                slc5 = True

            if startingslices == '6':
                slc1 = True
                slc2 = True
                slc3 = True
                slc4 = True
                slc5 = True
                slc6 = True

            if startingslices == '7':
                slc1 = True
                slc2 = True
                slc3 = True
                slc4 = True
                slc5 = True
                slc6 = True
                slc7 = True

            while (doing < int(repeat)):
                clr()
                doing += 1
                print(' - Spin -')
                pizzadrawingengine()
                print(' - Spin -')
                print()
                newslc1 = False
                newslc2 = False
                newslc3 = False
                newslc4 = False
                newslc5 = False
                newslc6 = False
                newslc7 = False
                newslc8 = False

                if slc1:
                    newslc2 = True

                if slc2:
                    newslc3 = True

                if slc3:
                    newslc4 = True

                if slc4:
                    newslc5 = True

                if slc5:
                    newslc6 = True

                if slc6:
                    newslc7 = True

                if slc7:
                    newslc8 = True

                if slc8:
                    newslc1 = True

                slc1 = newslc1
                slc2 = newslc2
                slc3 = newslc3
                slc4 = newslc4
                slc5 = newslc5
                slc6 = newslc6
                slc7 = newslc7
                slc8 = newslc8

                time.sleep(float(timing))
            doing = 0
            slc1 = False
            slc2 = False
            slc3 = False
            slc4 = False
            slc5 = False
            slc6 = False
            slc7 = False
            slc8 = False
            question1 = True
            question2 = True
            question3 = True
            spinsetup()
            spin()
        spin()
    
    elif ans == '2':
        doing = 0
        question1 = True
        question2 = True
        question3 = True

        def twoskipspinsetup():
            global question1, question2, repeat, timing
            clr()
            print('Type amount of skips you want to happen (1 - 500) (type "quit" to exit to main menu):')

            if question1:
                repeat = input(' > ')

                if repeat == "quit" or repeat == "q":
                    main()

                if repeat:
                    if int(repeat):
                        if (int(repeat) < 501) and (int(repeat) > 0):
                            question1 = False
                            repeat = str(int(repeat) + 1)

                        else:
                            twoskipspinsetup()
                    else:
                        twoskipspinsetup()
                else:
                    twoskipspinsetup()
            else:
                print(" > " + str(int(repeat) - 1))

            print()
            print('Type amount of time you want between skips (0.1 - 2) (type "quit" to exit to main menu):')

            if question2:
                timing = input(' > ')

                if timing == "quit" or timing == "q":
                    main()

                if timing:
                    if float(timing) and (len(timing) < 4):
                        if (float(timing) < 2.1) and (float(timing) > 0):
                            question2 = False

                        else:
                            twoskipspinsetup()
                    else:
                        twoskipspinsetup()
                else:
                    twoskipspinsetup()
            print()
            print('Press "ENTER" to continue: ')
            input(' > ')
        twoskipspinsetup()

        def twoskipspin():
            global repeat, startingslices, timing, doing, slc1, slc2, slc3, slc4, slc5, slc6, slc7, slc8, question1, question2, question3
            slc1 = True
            slc2 = True

            while (doing < int(repeat)):
                clr()
                doing += 1
                print(' - Two-skip Spin -')
                pizzadrawingengine()
                print(' - Two-skip Spin -')
                print()
                newslc1 = False
                newslc2 = False
                newslc3 = False
                newslc4 = False
                newslc5 = False
                newslc6 = False
                newslc7 = False
                newslc8 = False

                if slc1:
                    newslc4 = True

                if slc2:
                    newslc5 = True

                if slc3:
                    newslc6 = True

                if slc4:
                    newslc7 = True

                if slc5:
                    newslc8 = True

                if slc6:
                    newslc1 = True

                if slc7:
                    newslc2 = True

                if slc8:
                    newslc3 = True

                slc1 = newslc1
                slc2 = newslc2
                slc3 = newslc3
                slc4 = newslc4
                slc5 = newslc5
                slc6 = newslc6
                slc7 = newslc7
                slc8 = newslc8

                time.sleep(float(timing))
            doing = 0
            slc1 = False
            slc2 = False
            slc3 = False
            slc4 = False
            slc5 = False
            slc6 = False
            slc7 = False
            slc8 = False
            question1 = True
            question2 = True
            question3 = True
            twoskipspinsetup()
            twoskipspin()
        twoskipspin()
    
    elif ans == '3':
        doing = 0
        question1 = True
        question2 = True

        def fillsetup():
            global question1, question2, repeat, timing
            clr()
            print('Type amount of skips you want to happen (1 - 500) (type "quit" to exit to main menu):')

            if question1:
                repeat = input(' > ')

                if repeat == "quit" or repeat == "q":
                    main()

                if repeat:
                    if int(repeat):
                        if (int(repeat) < 501) and (int(repeat) > 0):
                            question1 = False
                            repeat = str(int(repeat) + 1)

                        else:
                            twoskipspinsetup()
                    else:
                        twoskipspinsetup()
                else:
                    twoskipspinsetup()
            else:
                print(" > " + str(int(repeat) - 1))

            print()
            print('Type amount of time you want between skips (0.1 - 2) (type "quit" to exit to main menu):')

            if question2:
                timing = input(' > ')

                if timing == "quit" or timing == "q":
                    main()

                if timing:
                    if float(timing) and (len(timing) < 4):
                        if (float(timing) < 2.1) and (float(timing) > 0):
                            question2 = False

                        else:
                            fillsetup()
                    else:
                        fillsetup()
                else:
                    fillsetup()
            print('Press "ENTER" to continue:')
            print()
            input(' > ')
        fillsetup()

        def fill():
            global slc1, slc2, slc3, slc4, slc5, slc6, slc7, slc8, repeat, timing, doing, question1, question2

            while (doing < int(repeat)):
                clr()
                doing += 1
                print(' - Fill -')
                pizzadrawingengine()
                print(' - Fill -')
                print()

                if slc8:
                    if slc1:
                        slc1 = False

                    elif slc2:
                        slc2 = False

                    elif slc3:
                        slc3 = False

                    elif slc4:
                        slc4 = False

                    elif slc5:
                        slc5 = False

                    elif slc6:
                        slc6 = False

                    elif slc7:
                        slc7 = False

                    else:
                        slc8 = False

                else:
                    if slc7:
                        slc8 = True

                    elif slc6:
                        slc7 = True

                    elif slc5:
                        slc6 = True

                    elif slc4:
                        slc5 = True

                    elif slc3:
                        slc4 = True

                    elif slc2:
                        slc3 = True

                    elif slc1:
                        slc2 = True
                    
                    else:
                        slc1 = True
                time.sleep(float(timing))
            doing = 0
            question1 = True
            question2 = True
            fillsetup()
            fill()
        fill()

    elif ans == '4':
        def freeplay():
            global slc1, slc2, slc3, slc4, slc5, slc6, slc7, slc8
            clr()
            print(' - Freeplay -')
            pizzadrawingengine()
            print(' - Freeplay -')
            print()
            print('Type the # of slice you want to show or hide (type "quit" to exit to main menu):')
            ans = input(' > ')
            ans = ans.lower()

            if ans == '1':
                if slc1:
                    slc1 = False

                else:
                    slc1 = True

                freeplay()

            if ans == '2':
                if slc2:
                    slc2 = False

                else:
                    slc2 = True

                freeplay()

            if ans == '3':
                if slc3:
                    slc3 = False

                else:
                    slc3 = True

                freeplay()

            if ans == '4':
                if slc4:
                    slc4 = False

                else:
                    slc4 = True

                freeplay()

            if ans == '5':
                if slc5:
                    slc5 = False

                else:
                    slc5 = True

                freeplay()

            if ans == '6':
                if slc6:
                    slc6 = False

                else:
                    slc6 = True

                freeplay()

            if ans == '7':
                if slc7:
                    slc7 = False

                else:
                    slc7 = True

                freeplay()

            if ans == '8':
                if slc8:
                    slc8 = False

                else:
                    slc8 = True

                freeplay()

            if ans == 'quit' or ans == 'q':
                main()

            else:
                freeplay()
        freeplay()

    elif ans == 'quit' or ans == 'q':
        f = open('save1.txt', 'a+')
        f.truncate(0)
        f.write('1')
        f.close()
        clr()
        print('-----')
        print()
        print('Thank you for playing my demo :)!')
        print()
        print('-----')
        print()
        print('Credits:')
        print('')
        print('Tristan Hafström for Pizza Artwork')
        print('Tristan Hafström for all programming')
        print('\'patorjk.com\' for their \'TAAG\' (Text to ASCII Art Generator)')
        print()
        print('And, as always, my cat Ninja')
        print()
        print('-----')
        print()
        print('Press \'ENTER\' to close this window')
        print()
        input(" > ")
        clr()
        exit(0)

    else:
        main()
main()