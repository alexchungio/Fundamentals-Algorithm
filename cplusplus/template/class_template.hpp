
template <class T1, class T2>
class Pair
{
    public:
        Pair() {};
        Pair(T1 k, T2 v): _key(k), _value(v) {};
        bool operator < (const Pair<T1, T2> &p) const;
    private:
        T1 _key;
        T2 _value;
};

template<class T1, class T2>
bool Pair<T1, T2>::operator < (const Pair<T1, T2> &p) const
{
    return _value < p._value;
}