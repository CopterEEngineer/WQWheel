import scipy.stats as ss

def MyRank(a, method):
    
    return (ss.rankdata(a, method=method)-1.0)*1.0 / np.count_nonzero(~np.isnan(ss.rankdata(a, method=method)))
