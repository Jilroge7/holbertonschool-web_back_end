-- stored procedure 'AddBonus' takes 3 inputs:
-- user_id, project_name, score. Procedure will add a new correction to a student.
DELIMITER //
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score FLOAT)
BEGIN
    INSERT INTO projects (name) SELECT project_name FROM DUAL
    WHERE project_name NOT IN (SELECT name FROM projects);
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END//    
DELIMITER ;