CREATE TABLE [users] (
  [user_ID] int PRIMARY KEY,
  [username] string,
  [email] string,
  [password] string,
  [user_created] String,
  [user_deleted] String
)
GO

CREATE TABLE [documents] (
  [document_ID] int PRIMARY KEY,
  [document_name] text,
  [document_type] nvarchar(255),
  [document_size] int,
  [document_location] string,
  [time_upload] String,
  [user_ID] int
)
GO

CREATE TABLE [paragraphs] (
  [paragraphs_ID] int PRIMARY KEY,
  [keywords] string,
  [document_ID] int
)
GO

CREATE TABLE [keywords] (
  [paragraphs_ID] int,
  [words] String
)
GO

CREATE TABLE [authors] (
  [document_ID] int,
  [author_names] String,
  [year_of_Written] String
)
GO

CREATE TABLE [summary] (
  [document_ID] int,
  [summary_paragraph] text
)
GO

ALTER TABLE [documents] ADD FOREIGN KEY ([user_ID]) REFERENCES [users] ([user_ID])
GO

ALTER TABLE [paragraphs] ADD FOREIGN KEY ([document_ID]) REFERENCES [documents] ([document_ID])
GO

ALTER TABLE [keywords] ADD FOREIGN KEY ([paragraphs_ID]) REFERENCES [paragraphs] ([paragraphs_ID])
GO

ALTER TABLE [authors] ADD FOREIGN KEY ([document_ID]) REFERENCES [documents] ([document_ID])
GO

ALTER TABLE [summary] ADD FOREIGN KEY ([document_ID]) REFERENCES [documents] ([document_ID])
GO
