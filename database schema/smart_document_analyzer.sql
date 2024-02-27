CREATE TABLE [users] (
  [user_ID] int PRIMARY KEY,
  [username] text,
  [email] nvarchar(255),
  [password] nvarchar(255),
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
  [summary] text,
  [authors_ID] String,
  [user_ID] int
)
GO

CREATE TABLE [paragraphs] (
  [paragraphs_ID] int PRIMARY KEY,
  [user_id] int,
  [keywords] nvarchar(255),
  [document_ID] int
)
GO

CREATE TABLE [keywords] (
  [keyword_ID] int PRIMARY KEY,
  [paragraphs_ID] int,
  [words] String
)
GO

CREATE TABLE [authors] (
  [authors_ID] int PRIMARY KEY,
  [author_names] String,
  [year_of_Written] String
)
GO

ALTER TABLE [documents] ADD FOREIGN KEY ([user_ID]) REFERENCES [users] ([user_ID])
GO

ALTER TABLE [paragraphs] ADD FOREIGN KEY ([document_ID]) REFERENCES [documents] ([document_ID])
GO

ALTER TABLE [keywords] ADD FOREIGN KEY ([paragraphs_ID]) REFERENCES [paragraphs] ([paragraphs_ID])
GO

ALTER TABLE [authors] ADD FOREIGN KEY ([authors_ID]) REFERENCES [documents] ([authors_ID])
GO
