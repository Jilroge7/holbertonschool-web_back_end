-- stored procedure 'AddBonus' takes 3 inputs:
-- user_id, project_name, score. Procedure will add a new correction to a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections as increased where increased.user_id=user_id)
    WHERE id = user_id;
END//    
DELIMITER ;