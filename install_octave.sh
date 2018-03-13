brew tap brewsci/science
brew update && brew upgrade
# install xquartz for X11
brew cask install xquartz
# install gcc for octave
brew install gcc
brew install octave
# install fltk for gnuplot
brew install fltk
brew install gnuplot
echo 'setenv ("GNUTERM", "X11")' > ~/.octaverc
