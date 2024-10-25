/* Write your T-SQL query statement below */
SELECT 
    start.machine_id,
    ROUND(AVG(end_activity.timestamp - start.timestamp), 3) AS processing_time
FROM 
    Activity AS start
JOIN 
    Activity AS end_activity
ON 
    start.machine_id = end_activity.machine_id
    AND start.process_id = end_activity.process_id
    AND start.activity_type = 'start'
    AND end_activity.activity_type = 'end'
GROUP BY 
    start.machine_id;