#include <stdio.h>
#include "class_template.h"

template<class T1, class T2>
bool Pair<T1, T2>::operator < (const Pair<T1, T2> &p) const
{
    return _value < p._value;
}
