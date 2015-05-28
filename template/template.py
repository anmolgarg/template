"""This is the docstring for the example.py module.  Modules names should
have short, all-lowercase names.  The module name may have underscores if
this improves readability.

Every module should have a docstring at the very top of the file.  The
module's docstring may extend over multiple lines.  If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceeded by a blank line.

"""

# uncomment the following line to use python 3 features
#from __future__ import division, absolute_import, print_function

# standard library imports first
import shutil
import sys
import os  

import numpy as np
import random


def foo(var1, var2, long_var_name='hi'):
    """
    A one-line summary that does not use variable names or the
    function name.

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.

    Parameters
    ----------------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.
    var2 : int
        The type above can either refer to an actual Python type
    Long_variable_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.

    Returns
    ----------------
    type
        Explanation of anonymous return value of type ``type``.
    describe : type
        Explanation of return value named `describe`.
    out : type
        Explanation of `out`.

    Other Para
    ----------------
    only_seldom_used_keywords : type
        Explanation
    common_parameters_listed_above : type
        Explanation

    Raises
    ------
    BadException
        Because you shouldn't have done that.

    See Also
    --------
    otherfunc : relationship (optional)
    newfunc : Relationship (optional), which could be fairly long, in which
              case the line wraps here.
    thirdfunc, fourthfunc, fifthfunc

    Notes
    -----
    Notes about the implementation algorithm (if needed).

    This can have multiple paragraphs.

    You may include some math:

    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

    And even use a greek symbol like :math:`omega` inline.

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> a=[1,2,3]
    >>> print [x + 3 for x in a]
    [4, 5, 6]
    >>> print "a\n\nb"
    a
    b

    """

    pass


# functions are easy to build
def simple_function(x, y=3, letter='b', tf=True, none=None, *args, **kwargs):
    '''
    example simple function

    '''

    print 'x = ' + str(x)
    print 'x*y = ' + str(x * y)
    print 'the letter is: ' + letter
    if tf:
        print 'the boolean variable is True :-)'
    else:
        print 'the boolean variable is was not True :-('
    if none is not None:
        print 'none is not None'
        print 'none is: ' + str(none)
    print "also...."
    print args
    print kwargs
    return x * y


# classes are also easy to build
class GeneralClass:
    '''
    GeneralClass provides a simple interface for initalizing arguments passed in kwargs
    and a runMethod method for running a class method by name

    '''

    def __init__(self, **kwargs):
        self.set_attributes(kwargs)

    def set_attributes(self, kwargs):
        '''
        Initalizes the given argument structure as properties of the class
        to be used by name in specific method execution.

        Parameters
        ----------
        kwargs : dictionary
            Dictionary of extra attributes,
            where keys are attributes names and values attributes values.

        '''
        for key, value in kwargs.items():
            setattr(self, key, value)
            # print key, value

    def run_method(self, method):
        '''call a specied method by name using runMethod'''
        methodToCall = getattr(self, method)
        result = methodToCall()
