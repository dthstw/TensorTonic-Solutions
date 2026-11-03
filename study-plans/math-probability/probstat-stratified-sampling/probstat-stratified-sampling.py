from math import floor, sqrt
import numpy as np

def stratified_sample(strata_means: list, strata_stds: list, strata_sizes: list, total_sample: int) -> dict:
    """
    Returns exact allocations, the stratified mean, and its standard error.
    """
    stratas_size = np.sum(strata_sizes)
    W_h_arr = np.asarray(strata_sizes, dtype=np.float64) / stratas_size
    a_h_arr = total_sample * W_h_arr
    a_h_arr_int = np.floor(a_h_arr)
    reminders = a_h_arr - a_h_arr_int
    order = np.argsort(-reminders, kind="stable")
    a_h_arr_int = np.maximum(a_h_arr_int, 1).astype(int)
    k = total_sample - np.sum(a_h_arr_int)
    a_h_arr_int[order[:k]]+= 1
    strat_mean = round(np.sum(strata_means * W_h_arr), 4)
    strat_se = round(np.sqrt(np.sum(np.power(strata_stds, 2) * np.power(W_h_arr, 2) / a_h_arr_int)), 4)
    res = {"allocations":a_h_arr_int,"stratified_mean":strat_mean,"stratified_se": strat_se}
    return res
    
    
        
    
    
