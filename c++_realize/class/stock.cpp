
#include <iostream>
#include "stock.hpp"


// void Stock::acquire(const std::string &  name, long num, double price)
// {
//     name_corporation = name;
//     num_shares =  num;
//     price_shares = price;
//     set_total_val();
    
// }

Stock::Stock()
{
    std::cout << "default construct called" << std::endl;
    name_corporation = "none";
    num_shares =  0;
    price_shares = 0.0;
    set_total_val();
    
}

Stock::Stock(const std::string &  name, long num, double price)
{
    std::cout << "construct called" << std::endl;
    name_corporation = name;
    num_shares =  num;
    price_shares = price;
    set_total_val();
    
}

Stock::~Stock()
{
    std::cout << "deconstruct called" << std::endl;
    
}

void Stock::buy(long num, double price)
{
    num_shares += num;
    val_shares = price;
    set_total_val();    
}

void Stock::sell(long num, double price)
{
    num_shares -= num;
    val_shares = price;
    set_total_val();
}

void Stock::update_price(double price)
{
    price = price;
    set_total_val();
}

void Stock::show_info() const
{

    std::cout << "Corporation: " << this -> name_corporation
              << "\tNum shares: " << this -> num_shares
              << "\tPrice shares: " << this -> price_shares
              << "\tTotal val shares: " << this -> val_shares << std::endl;

}

const Stock & Stock::get_top_stock(const Stock & s)
{
   if(s.val_shares > val_shares)
       return s;
   else
       return * this;
}


Stock Stock::operator +(const Stock & s) const
{
    
    Stock sum;
    sum.val_shares = val_shares + s.val_shares;
    
    return sum;
    
}

Stock Stock::operator *(double n) const
{   
    Stock multi = *this;
    multi.num_shares *= n;
    multi.set_total_val();
    return multi;

}

std::ostream & operator << (std::ostream & os, const Stock & s)
{
    os << "\tcorporation:" << s.name_corporation << "\tnum_shares:" << s.num_shares << "\tprice:" << s.price_shares
       << "\tval shares:" << s.val_shares;
    return os;
}