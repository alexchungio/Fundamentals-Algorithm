#ifndef STOCK_H_
#define STOCK_H_

#include <string>


class Stock{
    private:
        std::string name_corporation;
        long num_shares;
        double price_shares;
        double val_shares;
        void set_total_val(){ val_shares = num_shares * price_shares;}

    public:
        Stock(); // default construct 
        Stock(const std::string &, long, double); //construct
        ~ Stock(); // deconstruct
        // void acquire(const std::string & , long, double);
        void buy(long num, double price);
        void sell(long num, double price);
        void update_price(double price);    
        void show_info() const;
        const Stock & get_top_stock(const Stock &);
        Stock operator +(const Stock &) const;
        Stock operator *(double) const;
        friend Stock operator *(double n, const Stock & s){ return s * n; };
        friend std::ostream & operator << (std::ostream &, const Stock &);
 

};

#endif


