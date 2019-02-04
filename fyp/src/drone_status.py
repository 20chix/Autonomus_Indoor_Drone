#!/usr/bin/env python

# An enumeration of drone statuses for the drone

class DroneStatus(object):
	Emergency = 0
	Inited    = 1
	Landed    = 2
	Flying    = 3
	Hovering  = 4
	Test      = 5
	TakingOff = 6
	GotoHover = 7
	Landing   = 8
	Looping   = 9