##  https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
##  http://www.berkeleyinternet.com/perl/node30.html
##  https://codegolf.stackexchange.com/questions/135936/ascii-hangman-in-progress

'''
  +---+
  |   |
      |
      |
      |
      |
=========

  +---+
  |   |
  O   |
      |
      |
      |
=========

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
while (<>) { # <> puts the keyboard entry into $_
        gallows($_);# inside gallows $_[0] is the 1st argument 
                    # which is our keyboard entry $_
    }
    sub gallows { 
        # First the crossbar of the gallows 
            print "_____________   \n"; 
            print "|           |   \n"; 
        if ($_[0] == 0){ # Now the head 
            print "|               \n"; 
            print "|               \n"; 
            print "|               \n"; 
            print "|               \n"; 
        } else { 
            print "|           o   \n"; 
            print "|          o o  \n"; 
            print "|          o o  \n"; 
            print "|           o   \n"; 
        } 
        if ($_[0] <= 1) { # The body and arms
            print "|               \n"; 
            print "|               \n"; 
            print "|               \n"; 
        } elsif ($_[0] == 2) { 
            print "|           |    \n"; 
            print "|           |    \n"; 
            print "|           |    \n"; 
        } elsif ($_[0] == 3) { 
            print "|           |    \n"; 
            print "|          /|    \n"; 
            print "|         / |    \n"; 
        } elsif ($_[0] >3) { 
            print "|           |    \n"; 
            print "|          /|\\  \n"; 
            print "|         / | \\ \n"; 
        } 
        # Excercise: Write the code to print the legs here.   
    }