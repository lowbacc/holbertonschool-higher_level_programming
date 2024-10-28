-- This script changes the class of the students who have a score of 5 or less to 'Fail'.
DELETE FROM second_table
WHERE score <= 5;