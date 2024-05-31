#!/usr/bin/env python

import os

import clawpack.geoclaw.surge.storm

name = os.getenv("USER")
CLAW = os.getenv("CLAW")
print(clawpack.geoclaw.surge.storm.__file__)
print(f"howdy {name}")
print(f"My claw is at: {CLAW}")