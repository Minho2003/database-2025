CREATE DATABASE IF NOT EXISTS DeliveryBase
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_unicode_ci;

USE DeliveryBase;

CREATE TABLE `menu` (
	`id`	int	NOT NULL AUTO_INCREMENT,
	`store_id`	int	NOT NULL,
	`menu`	varchar(200)	NOT NULL,
	`price`	int	NOT NULL,
	`created_at`	datetime	NOT NULL,
	`update_at`	datetime	NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `review` (
	`id`	int	NOT NULL AUTO_INCREMENT,
	`user_id`	int	NOT NULL,
	`store_id`	int	NOT NULL,
	`order_id`	int	NULL,
	`rating`	int	NOT NULL,
	`content`	varchar(200)	NULL,
	`created_at`	datetime	NOT NULL,
	`update_at`	datetime	NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `order` (
	`id`	int	NOT NULL AUTO_INCREMENT,
	`user_id`	int	NOT NULL,
	`store_id`	int	NOT NULL,
	`rider_id`	int	NULL,
	`order`	varchar(100)	NOT NULL,
	`total_price`	int	NOT NULL,
	`order_time`	datetime	NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `favorite_store` (
	`id`	int	NOT NULL AUTO_INCREMENT,
	`user_id`	int	NOT NULL,
	`store_id`	int	NOT NULL,
	`created_at`	datetime	NOT NULL,
	`is_deleted`	boolean	NOT NULL DEFAULT FALSE,
	PRIMARY KEY (`id`)
);

CREATE TABLE `rider` (
	`id`	int	NOT NULL AUTO_INCREMENT,
	`rider_id`	varchar(30)	NOT NULL UNIQUE,
	`phone`	varchar(20)	NOT NULL,
	`vehicle`	varchar(30)	NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `payment` (
	`id`	int	NOT NULL AUTO_INCREMENT,
	`payment`	varchar(30)	NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `owner` (
	`id`	int	NOT NULL AUTO_INCREMENT,
	`owner_id`	varchar(30)	NOT NULL UNIQUE,
	`owner_passwd`	varchar(255)	NOT NULL,
	`email`	varchar(30)	NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `coupon` (
	`id`	int	NOT NULL AUTO_INCREMENT,
	`store_id`	int	NOT NULL,
	`period`	int	NULL,
	`discount`	int	NULL,
	`is_deleted`	boolean	NOT NULL DEFAULT FALSE,
	PRIMARY KEY (`id`)
);

CREATE TABLE `category` (
	`id`	int	NOT NULL AUTO_INCREMENT,
	`category`	varchar(30)	NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `user` (
	`id`	int	NOT NULL AUTO_INCREMENT,
	`user_id`	varchar(30)	NOT NULL UNIQUE,
	`passwd`	varchar(255)	NOT NULL,
	`email`	varchar(30)	NOT NULL,
	`name`	varchar(100)	NOT NULL,
	`address`	varchar(100)	NOT NULL,
	`created_at`	datetime	NOT NULL,
	`update_at`	datetime	NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `store` (
	`id`	int	NOT NULL AUTO_INCREMENT,
	`owner_id`	int	NOT NULL,
	`category_id`	int	NOT NULL,
	`payment_id`	int	NULL,
	`store_name`	varchar(50)	NOT NULL,
	`category`	varchar(30)	NOT NULL,
	`phone`	varchar(20)	NOT NULL,
	`minprice`	varchar(30)	NOT NULL,
	`reviewCount`	int	NOT NULL DEFAULT 0,
	`operationTime`	varchar(250)	NOT NULL,
	`closedDay`	varchar(250)	NOT NULL,
	`information`	varchar(500)	NULL,
	`created_at`	datetime	NOT NULL,
	`update_at`	datetime	NULL,
	PRIMARY KEY (`id`)
);

-- PRIMARY KEY는 CREATE TABLE에서 이미 정의됨

-- 외래키 제약조건
ALTER TABLE `store` ADD CONSTRAINT `FK_STORE_OWNER` FOREIGN KEY (`owner_id`) REFERENCES `owner` (`id`);
ALTER TABLE `store` ADD CONSTRAINT `FK_STORE_CATEGORY` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);
ALTER TABLE `store` ADD CONSTRAINT `FK_STORE_PAYMENT` FOREIGN KEY (`payment_id`) REFERENCES `payment` (`id`);
ALTER TABLE `menu` ADD CONSTRAINT `FK_MENU_STORE` FOREIGN KEY (`store_id`) REFERENCES `store` (`id`);
ALTER TABLE `order` ADD CONSTRAINT `FK_ORDER_USER` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
ALTER TABLE `order` ADD CONSTRAINT `FK_ORDER_STORE` FOREIGN KEY (`store_id`) REFERENCES `store` (`id`);
ALTER TABLE `order` ADD CONSTRAINT `FK_ORDER_RIDER` FOREIGN KEY (`rider_id`) REFERENCES `rider` (`id`);
ALTER TABLE `review` ADD CONSTRAINT `FK_REVIEW_USER` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
ALTER TABLE `review` ADD CONSTRAINT `FK_REVIEW_STORE` FOREIGN KEY (`store_id`) REFERENCES `store` (`id`);
ALTER TABLE `review` ADD CONSTRAINT `FK_REVIEW_ORDER` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`);
ALTER TABLE `favorite_store` ADD CONSTRAINT `FK_FAVORITE_USER` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
ALTER TABLE `favorite_store` ADD CONSTRAINT `FK_FAVORITE_STORE` FOREIGN KEY (`store_id`) REFERENCES `store` (`id`);
ALTER TABLE `coupon` ADD CONSTRAINT `FK_COUPON_STORE` FOREIGN KEY (`store_id`) REFERENCES `store` (`id`);

-- 기본 지불방식 데이터 추가
INSERT INTO `payment` (`payment`) VALUES
('만나서 카드결제'),
('만나서 현금 결제');

-- 기본 카테고리 데이터 추가
INSERT INTO `category` (`category`) VALUES
('한식'),
('일식'),
('중식'),
('양식'),
('분식'),
('패스트푸드');

-- StorePayment 테이블 (가게별 여러 지불방식 지원)
CREATE TABLE `store_payment` (
	`id`	int	NOT NULL AUTO_INCREMENT,
	`store_id`	int	NOT NULL,
	`payment_id`	int	NOT NULL,
	`created_at`	datetime	NOT NULL,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`store_id`) REFERENCES `store` (`id`),
	FOREIGN KEY (`payment_id`) REFERENCES `payment` (`id`)
);
