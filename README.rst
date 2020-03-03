openmodelica fmu export c
=========================

Dependencies:

  - omc compiler
  - gcc compiler
  - Python/OpenTURNS/otfmi

Compile C::

    mkdir -p /tmp/deviation
    gcc -static -o /tmp/deviation/libcwrapper.a -c wrapper.c

Generate fmu::

    ./mo2fmu.sh deviation_c.mo

Run::

    python run.py
    
