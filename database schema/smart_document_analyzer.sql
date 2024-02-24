CREATE TABLE `users` (
  `user_ID` int PRIMARY KEY,
  `username` text,
  `email` varchar(255),
  `password` varchar(255)
);

CREATE TABLE `Access_Control` (
  `access_ID` int PRIMARY KEY,
  `user_id` int,
  `file_id` int
);

CREATE TABLE `files` (
  `file_ID` int PRIMARY KEY,
  `file_name` text,
  `file_type` varchar(255),
  `file_size` int
);

CREATE TABLE `Text_Document` (
  `Doc_ID` int PRIMARY KEY,
  `user_id` int,
  `user_upload_time` date,
  `document_content` text,
  `file_id` int,
  `NLP_analysis_id` int
);

CREATE TABLE `NLP_Analysis` (
  `Analysis_ID` int PRIMARY KEY,
  `Author` text,
  `document_published_date` date,
  `keywords` text,
  `Summary` text,
  `conclusion` text,
  `text_document_id` int
);

ALTER TABLE `NLP_Analysis` ADD FOREIGN KEY (`text_document_id`) REFERENCES `Text_Document` (`Doc_ID`);

ALTER TABLE `Access_Control` ADD FOREIGN KEY (`access_ID`) REFERENCES `files` (`file_ID`);

ALTER TABLE `Access_Control` ADD FOREIGN KEY (`file_id`) REFERENCES `files` (`file_ID`);

ALTER TABLE `Access_Control` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`user_ID`);

ALTER TABLE `files` ADD FOREIGN KEY (`file_ID`) REFERENCES `users` (`user_ID`);

ALTER TABLE `Text_Document` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`user_ID`);

ALTER TABLE `Text_Document` ADD FOREIGN KEY (`file_id`) REFERENCES `files` (`file_ID`);

ALTER TABLE `Text_Document` ADD FOREIGN KEY (`NLP_analysis_id`) REFERENCES `NLP_Analysis` (`Analysis_ID`);
