CREATE TABLE product(
    id INTEGER PRIMARY KEY ,
    expiration_date DATE NOT NULL,
    price INTEGER
);

CREATE TABLE store(
                      id INTEGER PRIMARY KEY,
                      store_name VARCHAR(100) NOT NULL UNIQUE ,
                      city VARCHAR(100),
                      address VARCHAR(100),
                      phone VARCHAR(15)
);

CREATE TABLE groupp (
    id INTEGER PRIMARY KEY ,
    type VARCHAR (256) ,
    number INTEGER ,
    product_id INTEGER NOT NULL REFERENCES product (id) ON DELETE SET NULL,
    store_id INTEGER NOT NULL REFERENCES store (id) ON DELETE SET NULL
);

CREATE TABLE chek (
    id INTEGER PRIMARY KEY ,
    date DATE NOT NULL ,
    time TIME NOT NULL,
    total INTEGER NOT NULL,
    store_id INTEGER NOT NULL REFERENCES store (id) ON DELETE CASCADE,
    product_group_id INTEGER NOT NULL REFERENCES groupp (id) ON DELETE CASCADE ,
    number_sold_group INTEGER
);

CREATE TABLE employee (
    id INTEGER PRIMARY KEY ,
    store_id INTEGER NOT NULL REFERENCES store (id) ON DELETE SET NULL ,
    name VARCHAR (100) NOT NULL ,
    job VARCHAR (100) NOT NULL,
    phone VARCHAR(15)
            CONSTRAINT phone_check
            CHECK (substring(phone from 1 for 2) LIKE '+7'
                AND "right"(phone, 10) ~ '^[0-9]+$')

);

INSERT INTO store(id,store_name,city,address,phone)
VALUES (1,'walmart','Moscow','Hanover 23','+79877654321'),
       (2,'top shop','Belgorod','Broad Street 1', '+789995554433'),
       (3,'amazon','Belgorod','Pearl Street 367 ','+79865431234'),
       (4,'tt','Bongladesh', 'Primary 8', '+79877899878');

INSERT INTO product(id,expiration_date,price)
VALUES (1,'8970-06-23',11),
       (2,'2345-08-09',22),
       (3,'1234-12-23',33);

INSERT INTO groupp(id,type,number,product_id,store_id)
VALUES (1,'sausage',8800,1,1),
       (2,'cheese',800,2,3),
       (3,'bread',88,3,2),
       (4,'tea', 78, 2, 4);

-- INSERT INTO chek(id,date,time,total, store_id,product_group_id,number_sold_group)
-- VALUES (1,'2023-10-28','11:45:34',6765,1,1,615),
--        (2,'2020-10-27','07:11:01',8514,2,3,258),
--        (3,'2023-10-24','19:23:56',990,3,2,45);

INSERT INTO employee(id,store_id,name,phone,job)
VALUES (1,1,'Ann','+79707455645','salesman'),
       (2,2,'Jhon','+79436785234','security guard'),
       (3,3,'Alice','+79088766787','loader');

UPDATE store
SET store_name='fgtyftd'
WHERE id=1;

-- DELETE FROM product
-- WHERE id=2;

create index idx on chek(number_sold_group);
explain(analyse) select chek.number_sold_group from chek
order by chek.number_sold_group desc ;
drop index idx;

explain select time,avg(total) from( select
       case when time < '06:00:00' then 'night'
            when time < '12:00:00' then 'morning'
            when time < '18:00:00' then 'day'
            else 'evening'
        end time,total from chek) as totals
group by time;

explain(analyse) select
       case when time < '06:00:00' then 'night'
            when time < '12:00:00' then 'morning'
            when time < '18:00:00' then 'day'
            else 'evening'
        end, avg(total) from chek
group by time;

select groupp.type ,sum(chek.number_sold_group) from chek
join groupp on groupp.id = chek.product_group_id
group by groupp.type,chek.number_sold_group
order by chek.number_sold_group desc;

select store.store_name,groupp.type from groupp
join store on store.id = groupp.store_id
where store.city = 'Белгород' and store.id not in (
    select distinct chek.store_id from chek
        where chek.date > current_date - interval '7 days');

select groupp.type from chek
join store on chek.store_id = store.id
join groupp on chek.product_group_id = groupp.id
join product on groupp.product_id = product.id
where store.city != 'Москва'
group by groupp.type
having sum(chek.number_sold_group * product.price) > ( select avg(summ)
    from (select sum(chek.number_sold_group * product.price) as summ
          from chek
          join store on chek.store_id = store.id
          join groupp on chek.product_group_id = groupp.id
          join product on groupp.product_id = product.id
          where store.city = 'Москва'
          group by chek.id
          ) as scs );



select store.store_name,groupp.type from groupp
join store on store.id = groupp.store_id
where store.city = 'Белгород' and not exists(select chek.id from chek
         where chek.date > current_date - interval '7 days');

INSERT INTO chek (id, date, time, total, store_id, product_group_id, number_sold_group)
SELECT
    GENERATE_SERIES(1, 100,1) AS id,
    CURRENT_DATE AS date,
    CURRENT_TIME AS time,
    ROUND(RANDOM() * 1000) AS total,
    (RANDOM() * 3 + 1)::INT AS store_id,
    (RANDOM() * 3 + 1)::INT AS product_group_id,
    FLOOR(RANDOM() * 100) AS number_sold_group;
