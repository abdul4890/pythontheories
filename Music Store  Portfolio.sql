-- -- 1: Who is the most senior  employee?

-- Select title, last_name, first_name
-- FROM employee
-- ORDER BY levels DESC
-- LIMIT 1

-- -- 2: Which countries have the most of invoices?
-- select * from invoice

-- select count(*) as c, billing_country
-- from invoice
-- group by billing_country
-- order by c desc

-- -- 3: Top 3 invoice value

-- SELECT * FROM INVOICE
-- ORDER BY TOTAL DESC
-- LIMIT 3

-- -- 4: Most customers in the city

-- select sum(total) as invoice_total, billing_city
-- from invoice
-- group by billing_city
-- order by invoice_total desc 

-- -- 5: best customer in the region
-- select customer.customer_id,customer.first_name, customer.last_name, SUM(invoice.total) as total
-- from customer
-- JOIN invoice 
-- ON customer.customer_id = invoice.customer_id
-- group by customer.customer_id
-- order by total desc
-- limit 1

-- -- 6. list of all rock music listners

-- Select distinct email, first_name, last_name
-- FROM customer
-- JOIN invoice ON customer.customer_id = invoice.customer_id
-- JOIN invoice_line ON invoice.invoice_id = invoice_line.invoice_id
-- WHERE track_id IN 
-- (
--     Select track_id from track
-- 	join genre on track.genre_id = genre.genre_id
-- 	where genre.name like 'Rock')

-- order by email


-- 7: length of track more that avg time with name of the song

-- select name, milliseconds
-- from track
-- Where milliseconds > (
-- 	select avg(milliseconds) AS average_length
-- 	From track)
-- order by milliseconds desc
-- )

-- 8: write a query to return customer name, artist name and total spent, find how much amount spent by each customer on artists.

with best_selling_artist AS (
    select artist.artist_id AS artist_id, artist.name as artist_name,
    SUM (invoice_line.unit_price*invoice_line.quantity) as total_sales
	FROM invoice_line
	JOIN track On track.track_id = invoice_line.track_id
	JOIN album ON album.album_id = track.album_id
    JOIN artist ON artist.artist_id = album.artist_id
	GROUP by 1
	Order By 3 desc
	limit 1)

Select c.customer_id, c.first_name, c.last_name, bsc.artist_name,
SUM(il.unit_unitprice*il.quantity) AS total_spent
From invoice i
JOIN customer c on C.customer_id = i.customer_id
JOIN invoice_line il ON il.invoice_id = i.invoice_id
JOIN track t ON t.track_id = il.track_id
JOIN album alb ON alb.album_id = t.album_id
JOIN best_selling_artist bsa ON bsa.artist_id = alb.artist_id
GROUP by 1,2,3,4
order by 5 desc;

	
	
	
	