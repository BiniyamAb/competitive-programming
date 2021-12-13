def merge(intervals):
    intervals.sort(key =lambda x: x[0])
    mergedIntervals =[]
    for i in intervals:
        if not mergedIntervals or mergedIntervals[-1][-1] < i[0]:
            mergedIntervals.append(i)
        else:
            mergedIntervals[-1][-1] = max(mergedIntervals[-1][-1], i[-1])
    return mergedIntervals
