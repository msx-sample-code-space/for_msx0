#!/usr/bin/env python3
# coding=utf-8

import math

fish_pattern = [
	[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
	[ 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1 ],
	[ 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1 ],
	[ 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1 ],
	[ 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
	[ 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
	[ 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
	[ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
	[ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
	[ 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
	[ 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1 ],
	[ 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1 ],
	[ 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1 ],
	[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
]

def main():
	line = 1000
	with open( "fish.txt", "w" ) as f:
		# 左向き: 0～31 の 32通り
		for theta in range( 0, 32 ):
			rad = theta * math.pi / 16
			vx = math.cos( rad )
			vy = math.sin( rad )
			left = []
			right = []
			for y in range( 0, 16 ):
				d = 0
				for x in range( 0, 8 ):
					sx = (x - 8) * vx + (y - 8) * vy + 8
					sy =-(x - 8) * vy + (y - 8) * vx + 8
					if sx < 0:
						sx = 0
						p = 0
					elif sy < 0:
						sy = 0
						p = 0
					elif sx > 15:
						sx = 15
						p = 0
					elif sy > 15:
						sy = 15
						p = 0
					else:
						p  = fish_pattern[ int(sy) ][ int(sx) ]
					d = (d << 1) + p
				left.append( d )
				d = 0
				for x in range( 8, 16 ):
					sx = (x - 8) * vx + (y - 8) * vy + 8
					sy =-(x - 8) * vy + (y - 8) * vx + 8
					if sx < 0:
						sx = 0
						p = 0
					elif sy < 0:
						sy = 0
						p = 0
					elif sx > 15:
						sx = 15
						p = 0
					elif sy > 15:
						sy = 15
						p = 0
					else:
						p  = fish_pattern[ int(sy) ][ int(sx) ]
					d = (d << 1) + p
				right.append( d )
			left.extend( right )
			f.write( "%d DATA &H%02X" % ( line, left[0] ) )
			left = left[1:]
			line = line + 10
			for i in left:
				f.write( ",&H%02X" % i )
			f.write( "\n" )
		# 右向き: 32～63 の 32通り
		for theta in range( 0, 32 ):
			rad = theta * math.pi / 16
			vx = math.cos( rad )
			vy = math.sin( rad )
			left = []
			right = []
			for y in range( 0, 16 ):
				d = 0
				for x in range( 0, 8 ):
					sx = 15 - (8 + (x - 8) * vx + (y - 8) * vy)
					sy =       8 - (x - 8) * vy + (y - 8) * vx
					if sx < 0:
						sx = 0
						p = 0
					elif sy < 0:
						sy = 0
						p = 0
					elif sx > 15:
						sx = 15
						p = 0
					elif sy > 15:
						sy = 15
						p = 0
					else:
						p  = fish_pattern[ int(sy) ][ int(sx) ]
					d = (d << 1) + p
				left.append( d )
				d = 0
				for x in range( 8, 16 ):
					sx = 15 - (8 + (x - 8) * vx + (y - 8) * vy)
					sy =       8 - (x - 8) * vy + (y - 8) * vx
					if sx < 0:
						sx = 0
						p = 0
					elif sy < 0:
						sy = 0
						p = 0
					elif sx > 15:
						sx = 15
						p = 0
					elif sy > 15:
						sy = 15
						p = 0
					else:
						p  = fish_pattern[ int(sy) ][ int(sx) ]
					d = (d << 1) + p
				right.append( d )
			left.extend( right )
			f.write( "%d DATA &H%02X" % ( line, left[0] ) )
			left = left[1:]
			line = line + 10
			for i in left:
				f.write( ",&H%02X" % i )
			f.write( "\n" )


if __name__ == "__main__":
	main()
