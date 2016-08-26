drop table link;

-- 连接
create table `link` ( 
	`id` int(11)  NOT NULL AUTO_INCREMENT,
	`uid` int(10) NOT NULL DEFAULT '0',
	`title` varchar(128) DEFAULT NULL,
	`url` varchar(256) DEFAULT NULL,
	`likecount` int(10) DEFAULT 0,
	`dislikecount` int(10) DEFAULT 0,
	`add_time` int(10) DEFAULT NULL,
	PRIMARY KEY (`id`)
)DEFAULT CHARSET=utf8;

alter table `link` add `readcount` int(10) default '0';


-- 分类
create table `catalog` ( 
	`id` int(3)  NOT NULL AUTO_INCREMENT,
    `name` varchar(32) default null unique,
	`url` varchar(32) DEFAULT NULL unique,
	`add_time` int(10) DEFAULT NULL,
	PRIMARY KEY (`id`)
)DEFAULT CHARSET=utf8;

-- insert into catalog (`name`, `url`) values('新手上路','/newdriver');


-- 验证码
create table `captcha` (
	`session_id` varchar(64) NOT NULL ,
    `value` varchar(32) NOT NULL,
    `add_time` int(10) ,
    `status` smallint default 0,
    primary KEY (`session_id`)
)DEFAULT CHARSET=utf8;


-- 
drop table user_vote;
create table `user_vote` (	
    `user_id` int,
    `link_id` int,
    `type` smallint comment ' 0 disageree,   1 agree',
    `add_time` int(10) ,
    primary KEY (`user_id`, `link_id`)
)DEFAULT CHARSET=utf8;