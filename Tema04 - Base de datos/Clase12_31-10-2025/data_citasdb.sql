INSERT INTO pacientes (nombre, correo, telefono) VALUES 
('Ana Gomez', 'ana.gomez@mail.com', '555-1234'),
('Luis Ramirez', 'luis.ramirez@mail.com', '555-4567'),
('Karen Mendoza', 'karen.mendoza@mail.com', '333-1234');

INSERT INTO doctores (nombre, especialidad) VALUES 
('Dra Carmen Lopez', 'Cardiología'),
('Sr Juan Morales', 'Dermatología'),
('Karen Mendoza', 'Medicina General');

INSERT INTO citas (paciente_id, doctor_id, fecha_cita) VALUES 
(1, 3, '2025-10-30'),
(2, 1, '2025-10-31'),
(3, 2, '2025-10-30'),
(1, 2, '2025-10-31'),
(3, 2, '2025-10-31');