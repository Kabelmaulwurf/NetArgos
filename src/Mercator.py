'''

Mercator.py: NetArgos (c) 2013 Kabelmaulwurf

This file is part of NetArgos.

NetArgos.py is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

NetArgos is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

'''

from math import log, tan, pi


class Mercator(object):

    """ Mercator Projection Converter to convert Latitude/Longitude coordinates to absolute pixel coordinates"""

    def __init__(self, width, height, leftlon, botlat, rightlon, toplat):
        self.width = width
        self.height = height
        self.toplat = toplat
        self.botlat = botlat
        self.leftlon = leftlon
        self.rlonight = rightlon

        # calc relative values
        self.toplat_rel = self.relativeY(toplat)
        self.botlat_rel = self.relativeY(botlat)
        self.leftlon_rad = self.deg2rad(leftlon)
        self.rightlon_rad = self.deg2rad(rightlon)

    def relativeY(self, lat):
        """ assuming lat in degrees """
        return log(tan(lat / 360.0 * pi + pi / 4.0))

    def deg2rad(self, lon):
        return lon * pi / 180.0

    def screenY(self, lat):
        return self.height * (self.relativeY(lat) - self.toplat_rel) / (self.botlat_rel - self.toplat_rel)

    def screenX(self, lon):
        lon_rad = self.deg2rad(lon)
        return self.width * (lon_rad - self.leftlon_rad) / (self.rightlon_rad - self.leftlon_rad)

    def screenCoords(self, lon, lat):
        return self.screenX(lat), self.screenY(lon)



