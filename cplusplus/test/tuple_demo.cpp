#include <iostream>
#include <tuple>

using namespace std;

tuple <int, string, string> city_record(int year, string city, string corporation)
{
    return make_tuple(year, city, corporation);
}


int main()
{
    // construct tuple
    tuple<int, string, string> xiamen(make_tuple(2021, "xiamen", "meitu"));

    // get tuple value
    int year_0 = get<0>(xiamen);
    string city_0 = get<1>(xiamen);
    string corporation_0 = get<1>(xiamen);
    cout << "year: " << get<0>(xiamen) << "|city: " << get<1>(xiamen)<< get<2>(xiamen) << endl;
    cout << "year: " << year_0 << "|city: " << city_0 << "|corporation: " << corporation_0 << endl;

    // get tuple size
    auto s_0 = std::tuple_size<decltype(xiamen)>::value;
	std::cout << "the element size of size is " << s_0 << std::endl;

    // tie
    int year_1;
    string city_1, corporation_1;
    tie(year_1, city_1, corporation_1) = xiamen;
    cout << "year: " << year_1 << "|city: " << city_1 << "|corporation: " << corporation_1 << endl;

    // return multi value
    int year_2;
    string city_2, corporation_2;
    tie(year_2, city_2, corporation_2) = city_record(2019u, "fuzhou", "fzu");
    cout << "year: " << year_2 << "|city: " << city_2 << "|corporation: " << corporation_2 << endl;

    return 0;
}
