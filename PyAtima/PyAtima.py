#  SPDX-License-Identifier: GPL-3.0+
#
# Copyright © 2023 T. Beck.
#
# This file is part of PyAtima.
#
# PyAtima is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyAtima is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyAtima.  If not, see <http://www.gnu.org/licenses/>.

'''Wrapper for Atima'''

from .utils import run,parse

#---------------------------------------------------------------------------------------#
#		Class
#---------------------------------------------------------------------------------------#

class PyAtima:
	'''PyAtima class

	Arguments:
	----------
	Zp: int
		Proton number of projectile.
	Ap: int
		Mass number of projectile.
	E: float
		Energy of projectile [MeV/u].
	Zt: int
		Proton number of target.
	At: float
		Molar mass of target [u].
	t: float
		Target thickness [mg/cm2].

	Attributes:
	-----------
	results: dict
		Results of Atima run with keys.

	Note:
	-----
	PyAtima is a wrapper for Atima. The Atima source code
	can be found at https://web-docs.gsi.de/~weick/atima/
	PyAtima expects that Atima can be invoked from the 
	command line by calling atimawww.
	See the included documentation for more information.
	'''

	def __init__(self,Zp,Ap,E,Zt,At,t):
		'''Create PyAtima instance.'''

		self.Zp 	= Zp
		self.Ap 	= Ap	#amu
		self.E 		= E 	#MeV/u

		self.Zt 	= Zt
		self.At 	= At 	#g/mol
		self.t 		= t 	#mg/cm2

		output 		= run(self)

		self.results 	= parse(output)

		#dE/dx 		in MeV/(mg/cm2)
		#E 		in MeV/u
		#range		in mg/cm2
		#std_ang 	in mrad
