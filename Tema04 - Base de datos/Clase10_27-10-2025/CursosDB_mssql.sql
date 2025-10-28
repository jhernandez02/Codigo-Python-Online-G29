CREATE TABLE [categorias] (
  [id] integer PRIMARY KEY IDENTITY(1, 1),
  [nombre] nvarchar(255)
)
GO

CREATE TABLE [instructores] (
  [id] integer PRIMARY KEY IDENTITY(1, 1),
  [nombres] nvarchar(255),
  [apellidos] nvarchar(255)
)
GO

CREATE TABLE [horarios] (
  [id] integer PRIMARY KEY IDENTITY(1, 1),
  [nombre] nvarchar(255),
  [descripcion] nvarchar(255)
)
GO

CREATE TABLE [cursos] (
  [id] integer PRIMARY KEY IDENTITY(1, 1),
  [codigo] char(8),
  [nombre] varchar(150),
  [descripcion] text,
  [temario] text,
  [precio] decimal(7,2),
  [horas] integer,
  [categoria_id] integer NOT NULL,
  [horario_id] integer NOT NULL,
  [instructor_id] integer NOT NULL
)
GO

ALTER TABLE [cursos] ADD FOREIGN KEY ([categoria_id]) REFERENCES [categorias] ([id])
GO

ALTER TABLE [cursos] ADD FOREIGN KEY ([horario_id]) REFERENCES [horarios] ([id])
GO

ALTER TABLE [cursos] ADD FOREIGN KEY ([instructor_id]) REFERENCES [instructores] ([id])
GO
