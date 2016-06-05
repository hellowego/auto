create table `link` ( 
	`id` int(11)  NOT NULL AUTO_INCREMENT,
	`uid` int(10) NOT NULL DEFAULT '0',
	`title` varchar(128) DEFAULT NULL,
	`url` varchar(256) DEFAULT NULL,
	`add_time` int(10) DEFAULT NULL,
	PRIMARY KEY (`id`)
)DEFAULT CHARSET=utf8;

create table `catalog` ( 
	`id` int(3)  NOT NULL AUTO_INCREMENT,
    `name` varchar(32) default null unique,
	`url` varchar(32) DEFAULT NULL unique,
	`add_time` int(10) DEFAULT NULL,
	PRIMARY KEY (`id`)
)DEFAULT CHARSET=utf8;
