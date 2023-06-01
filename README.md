# PyAtima

[![License](https://img.shields.io/badge/License-GPL%20v3+-blue.svg)](LICENSE)

PyAtima is a [python](https://www.python.org/) wrapper for the program Atima [[1]](#AtimaWeb)
which is used for the calculation of the slowing down of ions in matter.

## Dependencies

* Atima [[1]](#AtimaWeb)
* python (tested with 3.9, 3.10, and 3.11)

`PyAtima` expects that Atima can be invoked from the command line by calling 

```
atimawww {input}
```

with the appropriate input.

## Install

`PyAtima` can be obtained by cloning this repository to the local system and running

```
python3 setup.py install
```

in the command line.

## Usage

`PyAtima` expects the same input quantities as Atima:

* Zp: Proton number of projectile.
* Ap: Mass number of projectile.
* E:  Energy of projectile [MeV/u].
* Zt: Proton number of target.
* At: Molar mass of target [u].
* t:  Target thickness [mg/cm2].

For instance, the stopping of <sup>64</sup>Fe ions at 100 MeV/u in 
100 mg/cm<sup>2</sup> of beryllium is calculated via

```
import PyAtima as pa

atima = pa.PyAtima(Zp=26,Ap=64,E=100,
					Zt=4,At=9.01,t=100)
```

Results of the calculation are stored in the dictionary

```
atima.results
```

A minimal example can be found in the [example](example) directory.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.

Copyright (C) 2023 Tobias Beck (beck@frib.msu.de)

## References

<a name='AtimaWeb'>[1]</a> [`Atima web page at GSI`](https://web-docs.gsi.de/~weick/atima/).\