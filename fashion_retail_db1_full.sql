CREATE DATABASE IF NOT EXISTS fashion_retail_db1;
USE fashion_retail_db1;

-- Customers Table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(10),
    region VARCHAR(50),
    signup_date DATE
);

-- Orders Table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Products Table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    price DECIMAL(10,2)
);

-- Order Items Table
CREATE TABLE order_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    discount DECIMAL(5,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Inventory Table
CREATE TABLE inventory (
    product_id INT,
    stock_level INT,
    warehouse VARCHAR(50),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Returns Table
CREATE TABLE returns (
    return_id INT AUTO_INCREMENT PRIMARY KEY,
    return_date DATE,
    order_id INT,
    reason VARCHAR(100),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
 INSERT INTO customers (customer_id, name, gender, region, signup_date) VALUES
(1, 'Swati Sharma', 'Female', 'North', '2023-01-10'),
(2, 'Amit Verma', 'Male', 'West', '2023-02-15'),
(3, 'Riya Sen', 'Female', 'South', '2023-03-20');
INSERT INTO orders (order_id, customer_id, order_date, status) VALUES
(101, 1, '2023-03-25', 'Delivered'),
(102, 2, '2023-04-02', 'Shipped'),
(103, 3, '2023-05-10', 'Cancelled');
INSERT INTO products (product_id, product_name, category, sub_category, price) VALUES
(1001, 'Denim Jeans', 'Clothing', 'Bottomwear', 1200.00),
(1002, 'Leather Jacket', 'Clothing', 'Outerwear', 3500.00),
(1003, 'Sneakers', 'Footwear', 'Casual', 2200.00);
 INSERT INTO order_items (item_id, order_id, product_id, quantity, discount) VALUES
(1, 101, 1001, 2, 100.00),
(2, 102, 1002, 1, 0.00),
(3, 103, 1003, 1, 200.00);
 INSERT INTO inventory (product_id, stock_level, warehouse) VALUES
(1001, 50, 'Delhi'),
(1002, 30, 'Mumbai'),
(1003, 70, 'Bangalore');
 INSERT INTO returns (return_id, return_date, order_id, reason) VALUES
(4, '2023-05-12', 103, 'Wrong Size'),
(5, '2023-04-05', 102, 'Late Delivery');
 -- Example for customers table

 DESCRIBE customers;

