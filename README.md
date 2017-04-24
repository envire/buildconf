## Envire "Standalone" Installation
This repository contains a minimal buildconfig to build and install the envire ***core*** package.


### Step by step
1. Create a folder for the project. It will contain the autoproj_bootstrap script, 
envire/core/ plus all needed dependencies and an 'install'-directory with binaries and includes.
2. Download the autoproj bootstrap script:
   ```
   wget http://rock-robotics.org/autoproj_bootstrap
   ```
3. Run the script and give it this repository as input config:
   ```
   ruby autoproj_bootstrap git git@github.com:envire/buildconf.git branch=minimalInstall
   ```
4. Set environment variables for the project:
   ```
   source env.sh
   ```
5. Update it:
   ```
   aup
   ```
6. Build it:
   ```
   amake
   ```
7. You will be asked how to access gitorius, github and the dfki gitlab. Choose wisely! (Or just use the default settings by pressing [ENTER])
8. **Which flavor of Rock do you want to use?** -- Choose "**master**". It won't install all of Rock, just some dependencies like base-types etc.
9. Further decisions I made (always default!)
   - Do you need compatibility with OCL ? (yes or no) [no] no
   - the target operating system for Orocos/RTT (gnulinux, xenomai, or macosx) [gnulinux] gnulinux
   - which CORBA implementation should the RTT use ? [omniorb] omniorb
   - whether C++11 should be enabled for Rock packages [no] no
10. Done! See `./install/`
