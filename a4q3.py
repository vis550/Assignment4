#NAME - VIKHYAT SINGH
#NSID - VIS550
#STUDENT NUMBER - 11300244
#INSTRUCTOR - PROFFESOR ERIC

class Statistics(object):
    def __init__(self):
        """
        Purpose:
            Initialize a Statistics object instance.
        """
        self.__count = 0      # how many data values seen so far
        self.__avg = 0        # the running average so far
        self.__max = None
        self.__min = None
        self.__range = None
        self.__mode = None
        self.__frequency = {}


    def add(self, value):
        """
        Purpose:
            Use the given value in the calculation of mean and 
            variance.
        Pre-Conditions:
            :param value: the value to be added
        Post-Conditions:
            none
        Return:
            :return none
        """
        self.__count += 1
        k = self.__count           # convenience
        diff = value - self.__avg  # convenience
        self.__avg += diff / k

        # To Calculate maximum value 
        if self.__max is None or self.__max < value:
            self.__max = value

        # To Calculate minimum value 
        if self.__min is None or self.__min > value:
            self.__min =  value

        # To Calculate mode 
        if value in self.__frequency:
            self.__frequency[value]+=1
        else:
            self.__frequency[value]=1




    def mean(self):
        """
        Purpose:
            Return the average of all the values seen so far.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """
        return self.__avg

    def count(self):
        """
        Purpose:
            Return the number of values seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """
        return self.__count

    def range(self):
        """
            Purpose:
                Return the range between the highest and lowest number.
            Post-conditions:
                (none)
            Return:
                The range of values seen so far.
                Note: if no data has been seen, None is returned.
        """

        # calculating range by subtracting max from min
        self.__range= self.__max-self.__min
        return self.__range

    def mode(self):
        """
            Purpose:
                Return the value which is seen most often.
            Post-conditions:
                (none)
            Return:
                The number of values seen so far.
                Note: if no data has been seen, None is returned.
        """

        # calculates the most frequently occured element in the frequency dictionary
        self.__mode = max(self.__frequency, key= lambda x: self.__frequency[x])          
        return self.__mode

    def max(self):
        """
            Purpose:
                Return the value which is the maximum among given values.
            Post-conditions:
                (none)
            Return:
                The maximum from number of values seen so far.
                Note: if no data has been seen, None is returned.
        """
        return self.__max

    def min(self):
        """
            Purpose:
                Return the value which is the minimum among given values.
            Post-conditions:
                (none)
            Return:
                The minimum from number of values seen so far.
                Note: if no data has been seen, None is returned.
        """
        return self.__min



