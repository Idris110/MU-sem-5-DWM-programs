-- queries v2

create materialized view mv
AS
select uni_name , course_name , gre_score
from university INNER JOIN fact_table
on university.uni_id = fact_table.uni_id
inner join ex_score
on ex_score.score_id = fact_table.score_id
Inner Join cources
on cources.course_id = fact_table.course_id;

select * from mv;


--Slice
select * from mv
where uni_name = 'Harvard University';


--Dice
select * from mv
where (uni_name = 'Harvard University' or uni_name = 'North Carolina State University')
and
(gre_score < 330 or gre_score >300)
and
(course_name = 'Data Science' or course_name = 'Computer Science')
group by mv.course_name, mv.uni_name, mv.gre_score;

--Rollup
select uni_name, course_name , sum(gre_score) as "gre_1score" from mv
group by Rollup( uni_name , course_name)
order by mv.uni_name, mv.course_name;

--Drill down
select uni_name, course_name , sum(gre_score) as "gre_1score" from mv
group by Rollup( uni_name , course_name)

--pivot
select * from mv;

select gre_score , course_name , uni_name from mv;
