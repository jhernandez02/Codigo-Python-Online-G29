-- Mostrar la lista de citas: paciente, doctor y fecha
SELECT p.nombre AS paciente, d.nombre AS doctor, 
TO_CHAR(c.fecha_cita, 'DD/MM/YYYY') AS fecha_cita
FROM citas c
INNER JOIN pacientes p ON p.id=c.paciente_id
INNER JOIN doctores d ON d.id=c.doctor_id;

SELECT p.nombre AS paciente, d.nombre AS doctor, 
TO_CHAR(c.fecha_cita, 'DD/MM/YYYY HH24:MI') AS fecha_cita
FROM citas c
INNER JOIN pacientes p ON p.id=c.paciente_id
INNER JOIN doctores d ON d.id=c.doctor_id;

-- Mostrar la lista de citas: paciente, especialidad y fecha
SELECT p.nombre AS paciente, d.especialidad, 
TO_CHAR(c.fecha_cita, 'DD/MM/YYYY HH24:MI') AS fecha_cita
FROM citas c
INNER JOIN pacientes p ON p.id=c.paciente_id
INNER JOIN doctores d ON d.id=c.doctor_id;

-- Mostrar la lista de citas por paciente: doctor, especialidad y fecha
SELECT p.nombre AS paciente, d.nombre AS doctor, d.especialidad, 
TO_CHAR(c.fecha_cita, 'DD/MM/YYYY HH24:MI') AS fecha_cita
FROM citas c
INNER JOIN pacientes p ON p.id=c.paciente_id
INNER JOIN doctores d ON d.id=c.doctor_id
WHERE paciente_id=3;

-- Mostrar la lista de citas por doctor: paciente y fecha
SELECT p.nombre AS paciente, 
TO_CHAR(c.fecha_cita, 'DD/MM/YYYY HH24:MI') AS fecha_cita
FROM citas c 
INNER JOIN pacientes p ON p.id=c.paciente_id
WHERE c.doctor_id=1;

-- Mostrar la lista de consultas de cada doctor
SELECT d.nombre AS doctor, COUNT(c.id) AS total_citas
FROM citas c 
INNER JOIN doctores d ON d.id=c.doctor_id
GROUP BY d.id;

-- Mostar las lista de consultas de todos los pacientes
-- que tienen por lo menos una cita
SELECT p.nombre AS paciente, COUNT(c.id) AS total_citas
FROM citas c 
INNER JOIN pacientes p ON p.id=c.paciente_id
GROUP BY p.id;

-- Mostar las lista de consultas de todos los pacientes
-- tengan o no una cita
SELECT p.nombre AS paciente, COUNT(c.id) as total_citas
FROM pacientes p
LEFT JOIN citas c ON c.paciente_id=p.id
GROUP BY p.id;

-- Mostar las lista de citas pagads de todos los doctores
SELECT d.nombre AS doctor, COUNT(c.id) as total_citas, SUM(c.precio) as total_pago
FROM doctores d
LEFT JOIN citas c ON c.doctor_id=d.id
GROUP BY d.id;
