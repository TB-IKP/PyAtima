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

'''Functions for PyAtima'''

import re

from subprocess import check_output

#---------------------------------------------------------------------------------------#
#		Run Atima
#---------------------------------------------------------------------------------------#

def run(self):
	'''Run Atima with the given parameters and return output.'''

	var_string 	= '%i %f %f %i %f %f'% (self.Zp,self.Ap,self.E,
						self.Zt,self.At,self.t)

	output 		= check_output(f'atimawww {var_string}',shell=True)

	return output.decode('utf-8')

#---------------------------------------------------------------------------------------#
#		Parse Atima output
#---------------------------------------------------------------------------------------#

def parse(output):
	'''Parse output of Atima run.'''

	Dic_quantities = {'dE/dx':	'dE/dx at entrance',
			  'E':		'exit energy',
			  'std_E':	'energy straggling',
			  'range':	'range',
			  'std_range':	'range straggling',
			  'std_ang':	'angular straggling',
			  #'q_p':	'q_p in - out',
			 }

	values 	= {}

	for name,string in Dic_quantities.items():

		identifier 	= string+'[ \t]*:[ \t]*[+-]*[ \t]*[0-9]+.[0-9]+'
		part_line 	= re.search(identifier,output)

		if part_line is None:

			identifier 	= string+'[ \t]*:[ \t]*inf'
			part_line 	= re.search(identifier,output)

			values[name] 	= 1e9

		else:

			values[name] 	= float(re.search('[0-9]+.[0-9]+',part_line.group(0)).group(0))

	return values
