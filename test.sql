.open test_db.db

select * from gaming;

 update gaming
 set 
    session_end = julianday('now'), 
    time_played = (julianday('now') - session_start)
order BY
    session_start desc
LIMIT 1;

--insert into gaming values ('MK11.exe', julianday('now'), null, null)

 SELECT * from gaming
 ORDER by session_end desc;