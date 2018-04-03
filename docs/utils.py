
import os
import ephem
import datetime
import urllib.request as urllib
import math

# ---------
# add lib folder to the path
def is_root(path):
    """
    Determine whether the path passed is the root directory for the file system
    """
    return not os.path.split(os.path.normpath(os.path.abspath(path)))[1]

def is_root_project_dir(path):
    """
    Determine whether the path specified is the root project directory by looking for 
    __mtk__.py in the directory. If the root file system directory is encountered, throw
    an exception
    """
    PROJECT_ROOT_FILE = '__mtk__.py'
    
    # make sure the path is in an OK format (ends with a directory separator)
    search_path = str(path)
    if (not search_path.endswith(os.sep)):
        search_path += os.sep
        
    # make sure the path isn't the root. if it is, there's a problem
    if (is_root(search_path)):
        raise Exception('Failed to locate root MTK directory (directory containint %s)' % PROJECT_ROOT_FILE)
        
    # check to see whether we can find the project root file in this path
    return os.path.isfile(search_path + PROJECT_ROOT_FILE)

def get_project_root():
    """
    Locate the project's root directory and return its location. If the root file system
    directory is encountered, throw an exception
    """
    search_path = os.getcwd() + os.sep
    count = 0
    while (not is_root_project_dir(search_path)):
        search_path = os.path.normpath(os.path.abspath(search_path + '..' + os.sep)) + os.sep
    return search_path
	
# ----------------

# ----------------
# atmospheric loss at given elevation (for our frequency)
# these values were found using the AMSAT link budget calculator
# see documentation for further information
def atmloss_at_elev(ureg, elev):
    return -4.6 if elev < 5  * ureg.degrees else \
           -2.1 if elev < 10 * ureg.degrees else \
           -1.1 if elev < 30 * ureg.degrees else \
           -0.4 if elev < 45 * ureg.degrees else \
           -0.3 if elev < 90 * ureg.degrees else 0.0
# ---------------

# ---------------------------------------------------------------------------------------
# look angles for NOAA-19 satellite pass
# uses pyephem and online TLEs for next pass on given datetime
def compute_angles(date=None):
	# handle the date argument
	date = date if date is not None else datetime.datetime.now()

	# fetch the tle from celestrak online
	response = urllib.urlopen('http://www.celestrak.com/NORAD/elements/noaa.txt')
	html = response.read()

	# split the html by new lines
	# we want NOAA 19, which was these indices as of April 4th, 2018
	name = str(html).split('\\r\\n')[57]
	line1 = str(html).split('\\r\\n')[58]
	line2 = str(html).split('\\r\\n')[59]

	# read in the tle
	tle_rec = ephem.readtle(name, line1, line2)

	# make a new ephem observer
	obs = ephem.Observer()
	obs.lon = 37.2725
	obs.lat = -80.4327
	obs.elev = 400
	obs.date = date

	# compute the orbit trajectory stuff
	tle_rec.compute(obs)

	# find the next pass
	next_pass = obs.next_pass(tle_rec)
	
	# move the current time to the next pass
	obs.date = next_pass[0]
	tle_rec.compute(obs)

	# empty lists to start
	alts  = []
	azs   = []
	times = []

	# loop through entire pass
	while tle_rec.alt > 0:
		# save results to list in radians
		alts.append(math.degrees(float(tle_rec.alt)))
		azs.append(math.degrees(float(tle_rec.az)))
		times.append(obs.date.datetime())

		# compute next second timestep
		obs.date = obs.date.datetime() + datetime.timedelta(seconds=1)
		# compute next pointing angle
		tle_rec.compute(obs)

	# return a tuple with the lists
	# format is (az, el, time)
	return (azs, alts, times)
# -------------------------------------------------------------------------------