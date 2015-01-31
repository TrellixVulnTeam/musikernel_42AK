#What is MusiKernel ?

MusiKernel is DAWs, plugins, and a new approach to developing an audio software ecosystem.  By promoting centralized development and quality control with maximal code re-use, MusiKernel aims to avoid many of the compatibility problems that have plagued traditional host/plugin architectures.

#How to build:

#Ubuntu/Debian distros:

cd [musikernel src dir]/src

./ubuntu_deps.sh

make deps

make deb

cd ../ubuntu

sudo dpkg -i musikernel[your_version].deb

#Fedora based distros:

cd [musikernel src dir]/src

./fedora_deps.sh

make rpm

cd ~/rpmbuild/RPMS/[your arch]

sudo yum localinstall musikernel[version number].rpm

#All others:

 # [figure out the dependencies based on the Fedora or Ubuntu dependencies]

cd [musikernel src dir]/src

make

 # You can specify DESTDIR or PREFIX if packaging, the result is fully relocatable

make install

