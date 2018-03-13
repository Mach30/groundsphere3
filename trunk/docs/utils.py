
import os

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
def atmloss_at_elev(elev):
    return -4.6 if elev < 5  * ureg.degrees else \
           -2.1 if elev < 10 * ureg.degrees else \
           -1.1 if elev < 30 * ureg.degrees else \
           -0.4 if elev < 45 * ureg.degrees else \
           -0.3 if elev < 90 * ureg.degrees else 0.0
# ---------------