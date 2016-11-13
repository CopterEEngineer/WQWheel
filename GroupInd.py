import scipy as sp
import numpy as np
import scipy.stats as ss

def GroupInd(a, di, group):
    
    # list of all groups
    grouplist = np.unique(np.where(group[di-delay, :] > 0 , group[di-delay, :], 0))
    a[np.isnan(a)] = 0
    groupmean = np.zeros(a.size)
    for igrp in grouplist:
        tmp_grp = np.where(np.logical_and(group[di-delay,:] == igrp, valid[di,:]), a, 0)
        tmp_mean = sum(tmp_grp) / np.count_nonzero(tmp_grp)
        groupmean[:] = np.where(np.logical_and(group[di-delay,:] == igrp, valid[di,:]), tmp_mean, groupmean)
    return a - groupmean
