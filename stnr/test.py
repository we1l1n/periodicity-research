# coding: utf-8

from suffix_tree import SuffTree
from algorithm import STNRAlgorithm


def test():

    STNRAlgorithm.s = 'abcdeabcdeabcdeabcdeabcdeabcdeabcde' + '$'
    print '01234567890123456789'
    print

    stnr_instance = STNRAlgorithm()

    st = SuffTree(
        stnr_instance=stnr_instance,
        T=STNRAlgorithm.s,
        minThreshold=STNRAlgorithm.minTh,
        tolWin=STNRAlgorithm.tolWin,
        dmax=STNRAlgorithm.dmax,
        minLengthOfSegment=STNRAlgorithm.minLengthSegment,
        specificPeriod=-2
    )

    print st.specificPeriod

    st.PrintTree()

    print 'Candidate Period Count: ', STNRAlgorithm.candPerCount
    print 'Added Period Count: ', STNRAlgorithm.addPerCount
    print 'Occur Vector Count: ', STNRAlgorithm.occVecCount
    print

    print st.periods


if __name__ == '__main__':
    test()