CREATE TABLE product (
ID INT AUTO_INCREMENT PRIMARY KEY,
ProdName VARCHAR(50),
Price INT,
ManuDate DATE,
ExpDate DATE,
Brand VARCHAR(50)
);
INSERT INTO product (ProdName,Price,ManuDate,ExpDate,Brand)
Values ('LAYS','10','2023-05-23','2023-06-25','CHIPS');
INSERT INTO product (ProdName,Price,ManuDate,ExpDate,Brand)
VALUES ('TOFFY','5','2022-09-3','2022-12-31','NESTLE');
INSERT INTO product (ProdName,Price,ManuDate,ExpDate,Brand)
VALUES ('DRINKS','20','2021-05-22','2021-09-6','COCO-COLA');
INSERT INTO product (ProdName,Price,ManuDate,ExpDate,Brand)
Values ('fruits','100','2023-08-9','2023-08-14','DRAGON');
INSERT INTO product (ProdName,Price,ManuDate,ExpDate,Brand)
VALUES ('GRAINS','500','2000-09-14','2024-08-15','ASHIRWAS');
SELECT * FROM product
UPDATE product
SET Price='80'
WHERE ID = 2;
DELETE FROM product
WHERE ID=3;