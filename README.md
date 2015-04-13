ABOUT
-----
Backend to query DNS based blackhole lists.

QUICK START
-----------
Compatible with python +3.4

Update settings_private.py per the following default config below.

    $ from settings_private import IPS
    $ d = DNSBLCheck(ips=IPS)
    $ d.run()

SETTINGS
--------

Create **settings_private.py** file in your python path::

    EMAIL_FROM = 'from@example.com'
    EMAIL_TO = 'to@example.com'

    IPS = [
        '1.2.3.4',
        '5.6.7.8',
        ...
    ]

LICENSE
-------
Copyright (C) 2015

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

CREDITS
-------
A project by [Water.org](http://water.org/). For more than two decades,
Water.org has been at the forefront of developing and delivering solutions to
the water crisis. Founded by Gary White and Matt Damon, Water.org pioneers
innovative, community-driven and market-based solutions to ensure all people
have access to safe water and sanitation; giving women hope, children health
and communities a future. 
