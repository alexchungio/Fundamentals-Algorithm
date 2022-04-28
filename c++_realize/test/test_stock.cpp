#include <iostream>
#include "stock.h"
#include <map>


int main()
{

    std::cout << __cplusplus << std::endl;
    
    Stock byte_dance_stock("byte_dance", 1000, 120.0);
    Stock baidu_stock("baidu", 500, 200.0);

    byte_dance_stock.show_info();
    baidu_stock.show_info();
    
    Stock sum_stock = baidu_stock + byte_dance_stock;
    sum_stock.show_info();

    Stock multi_stock_2 = baidu_stock * 2;
    multi_stock_2.show_info();

    Stock multi_stock_4 = 4 * baidu_stock;
    multi_stock_4.show_info();

    std::cout << baidu_stock << std::endl << multi_stock_2 << std::endl;

    return 0; 
  
}


