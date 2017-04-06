import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
from matplotlib import colors, ticker, cm
from matplotlib.mlab import bivariate_normal


myarray = np.fromfile('bfly_prob01_2cycle_fine.dat',dtype=float)


with open('bfly_prob01_2cycle_fine.dat') as openfileobject:
    for line in openfileobject:
        do_something()


print(myarray)


#fid=fopen(strcat(fpath,'bfly.dat'), 'rb'); % Open the file.

#hr=fread(fid, 1, 'int32'); % Record start tag
#ny=fread(fid, 1, 'int32');
#he=fread(fid, 2, 'int32'); % Record end and start tags
#th=fread(fid, ny, 'float64');
#hr=fread(fid, 1, 'int32'); % Record end tag
#t=[]; bx=[]; bz=[]; bpol=[];
#while ~feof(fid)
#    hr=fread(fid, 1, 'int32'); % Record start tag
#    t=[t fread(fid, 1, 'float64')];
#    hr=fread(fid, 2, 'int32'); % Record end and start tags
#    bx=[bx fread(fid, ny, 'float64')];
#    hr=fread(fid, 2, 'int32'); % Record end and start tags
#    bz=[bz fread(fid, ny, 'float64')];
#    hr=fread(fid, 2, 'int32');
#    bpol=[bpol fread(fid, ny, 'float64')];
#    hr=fread(fid, 1, 'int32'); % Record end tag
#end
#fclose(fid); % Close file.
#t = t*L0^2/ETA0/86400.0/365.25;
#lat = 90. - th*180/pi;
#bx=bx*bCorrect; bz=bz*bCorrect; bpol=bpol*bCorrect;

