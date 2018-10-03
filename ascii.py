import random
import os
i = random.randrange(10) + 1 
website="https://raw.githubusercontent.com/veritas06/ASCII-Art-Splash-Screen/master/art/"+ str(i) + ".txt"
os.system("curl " +  website)
