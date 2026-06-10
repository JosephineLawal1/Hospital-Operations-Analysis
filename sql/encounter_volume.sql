SELECT
    CAST(start_time AS DATE) AS encounter_date,
    COUNT(*) AS encounter_count
FROM encounters
GROUP BY CAST(start_time AS DATE)
ORDER BY encounter_date;
