INSERT INTO COURSE VALUES 
(1001, "Software Engineering"),
(1002, "Data Science"),
(1003, "Cyber Security"); 

INSERT INTO TASK VALUES 
(2001, 1001, 1, "SE Task One", "/se2023/seone"),
(2002, 1001, 2, "SE Task Two", "/se2023/setwo"),
(2003, 1001, 3, "SE Task Three", "/se2023/sethree"),
(2004, 1002, 1, "DS Task One", "/ds2023/dsone"),
(2005, 1002, 2, "DS Task Two", "/ds2023/dstwo"),
(2006, 1002, 3, "DS Task Three", "/ds2023/dsthree"),
(2007, 1003, 1, "CS Task One", "/cs2023/csone"),
(2008, 1003, 2, "CS Task Two", "/cs2023/cstwo"),
(2009, 1003, 3, "CS Task Three", "/cs2023/csthree");

INSERT INTO STUDENT VALUES 
(3001, 1001, "BR202305121349", "Billy Russo", "jiggy@email.com", "", "/students/BR202305121349/work"),
(3002, 1001, "BW202305121350", "Bruce Wayne", "bats@email.com", "", "/students/BW202305121350/work"),
(3003, 1002, "SK202305121349", "Selina Kyle", "kittycat@email.com", "", "/students/SK202305121349/work"),
(3004, 1002, "BB202305121449", "Billy Batson", "captainmarvel@email.com", "", "/students/BB202305121449/work"),
(3005, 1003, "SW202305121349", "Slade Wilson", "ds@email.com", "", "/students/SW202305121349/work"),
(3006, 1003, "RA202305121349", "Ras Al Ghul", "rag@leagueofassassins.com", "", "/students/RA202305121349/work");

INSERT INTO STUDENT_TASK(STUDENT_ID, TASK_ID) VALUES
(3001, 2001),
(3001, 2002),
(3001, 2003),
(3002, 2001),
(3002, 2002),
(3002, 2003),
(3003, 2004),
(3003, 2005),
(3003, 2006),
(3004, 2004),
(3004, 2005),
(3004, 2006),
(3005, 2007),
(3005, 2008),
(3005, 2009),
(3006, 2007),
(3006, 2008),
(3006, 2009);


INSERT INTO Task_Review VALUES (5001, 3001,2001)