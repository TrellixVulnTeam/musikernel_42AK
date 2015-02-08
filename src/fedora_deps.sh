#dependencies
sudo yum install python3-qt5 gcc alsa-lib-devel liblo-devel \
libsndfile-devel gcc-c++ git python3-numpy python3-scipy \
fftw-devel portmidi-devel portaudio-devel libsamplerate-devel python3-devel \
@development-tools fedora-packager livecd-tools spin-kickstarts \
system-config-kickstart vorbis-tools gettext

# Now run:
#
#   make clean
#   make
#
# followed by this command as root
#
#   make install

# or this command if packaging
#
#   make DESTDIR=/your/packaging/dir install
#
