import sys
import os
import os.path

my_dirname, my_filename = os.path.split(os.path.abspath( __file__ ) )


# print my_dirname  + "\n"
# print my_filename + "\n"


#my_curr_dir = os.path.dirname(os.path.realpath(__file__))

sys.path.append( "".join( [ my_dirname, os.sep, 'App_code' ] ) )
sys.path.append( "".join( [ my_dirname, os.sep, 'App_data' ] ) )

#for path in sys.path:
#    print path + "\n"


import App_code.WAP_V.constants
import App_data.GLOBALS



print App_code.WAP_V.constants.mod_vers + "\n"

print App_code.WAP_V.constants.Continue
print App_data.GLOBALS.mod_vers


print dir( App_code )
print dir( App_data )
print dir( App_code.WAP_V )

#print __builtins__
#print code.__builtins__
#print data.__builtins__








# xpto = WAP_V.constants.py.TRUE


# print WAP_V.mod_vers()

# print WAP_V.__NAME__

# print __name__


# print __file__

