create table _time(
    time_id int primary key,
    order_date varchar(255) not null,
    order_week varchar(255) not null,
    order_month varchar(255) not null,
    order_quarter varchar(255) not null,
    order_year varchar(255) not null
);

create table address_(
    address__id int not null primary key,
    pin int not null,
    city varchar(255) not null,
    region varchar(255) not null
);

create table product(
    product_id int primary key,
    product_name varchar(255) not null,
    product_brand varchar(255) not null,
    product_type varchar(255) not null
);

create table referrer(
    referrer_id int primary key,
    referrer_name varchar(255) not null,
    campaign_id int not null,
    campaign_source varchar(255) not null,
    campaign_medium varchar(255) not null
);

create table sales(
    order_id int primary key,
    time_id int not null,
    address__id int not null,
    referrer_id int not null,
    product_id int not null,
    quantity int not null,
    foreign key (time_id) references _time(time_id),
    foreign key (address__id) references address_(address__id),
    foreign key (product_id) references product(product_id),
    foreign key (referrer_id) references referrer(referrer_id)
);

select * from sales;
select * from _time;
select * from address_;
select * from referrer;
select * from product;

-- materialized views
-- create materialized view item
-- storage(initial 50k next 50k pct increase)
-- tablespace users
-- start with sysdate next sysdate+1
-- as
-- select * from address_ where city="Mumbai";

-- ROLL UP
select sum(sales.quantity) as sales_qty, _time.order_month
from sales inner join _time
on sales.time_id  = _time.time_id group by _time.order_month with rollup;

-- Slice
select product.product_id, sum(sales.quantity) as sales_qty, _time.order_month, product.product_name, address_.city from sales
inner join _time on sales.time_id  = _time.time_id
inner join product on sales.product_id = product.product_id
inner join address_ on sales.address__id = address_.address__id
where address_.city = "Mumbai"
group by _time.order_month, product.product_id, address_.city;

-- Drill down
select _time.order_month, _time.order_week, sum(sales.quantity) as sales_qty, product.product_name, address_.city from sales
inner join _time on sales.time_id  = _time.time_id
inner join product on sales.product_id = product.product_id
inner join address_ on sales.address__id = address_.address__id
group by _time.order_month, _time.order_week;

-- pivot table
select _time.order_month, _time.order_week, sum(sales.quantity) as sales_qty, product.product_name, address_.city from sales
inner join _time on sales.time_id  = _time.time_id
inner join product on sales.product_id = product.product_id
inner join address_ on sales.address__id = address_.address__id
group by _time.order_month, _time.order_week;


select distinct(city) from address_;
select product_type, count(product_type) from product group by product_type;

select order_month, sum(quantity) from
_time inner join sales on _time.time_id = sales.time_id
inner join address_ on address_.address__id = sales.address__id
where address_.city = "Mumbai"
    group by order_month;

-- dice
select _time.order_month, product.product_type, product.product_name, address_.city, sum(sales.quantity) as sales_qty from sales
inner join _time on sales.time_id  = _time.time_id
inner join product on sales.product_id = product.product_id
inner join address_ on sales.address__id = address_.address__id
where (address_.city = "Mumbai" or address_.city="Bengaluru")
    and (product.product_type = "Skin Care" or product.product_type="Hair Care") 
    and (_time.order_month = "2022-06" or _time.order_month = "2022-07")
group by address_.city, product.product_type, _time.order_month;
