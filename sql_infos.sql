Common MySQL date functions useful for intermediate SQL:

-- Extraction
YEAR(date)
MONTH(date)
DAY(date)
HOUR(datetime)
MINUTE(datetime)
SECOND(datetime)
WEEK(date)
QUARTER(date)
DAYOFWEEK(date)
DAYOFYEAR(date)

-- Conversion and formatting
DATE(date)
TIME(datetime)
DATE_FORMAT(date, format)
STR_TO_DATE(string, format)

-- Date arithmetic
DATE_ADD(date, INTERVAL n unit)
DATE_SUB(date, INTERVAL n unit)
ADDDATE(date, INTERVAL n unit)
SUBDATE(date, INTERVAL n unit)
DATEDIFF(date1, date2)
TIMESTAMPDIFF(unit, start, end)

-- Current date/time
NOW()
CURDATE()
CURTIME()



SELECT 
    EMPNAME,
    DEPTNAME,
    DOB
FROM employee_info ei
JOIN dept_info di ON ei.DEPTID = di.DEPTID
WHERE YEAR(ei.DOB) < 1990
  AND MONTH(ei.DOB) = 5
  AND DAY(ei.DOB) = 12;










































































