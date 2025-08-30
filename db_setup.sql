-- Dimension: Customer
CREATE TABLE IF NOT EXISTS dim_customer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    Region VARCHAR(50)
);

-- Dimension: Product
CREATE TABLE IF NOT EXISTS dim_product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50)
);

-- Fact: Sales
CREATE TABLE IF NOT EXISTS fact_sales (
    SalesID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT,
    CustomerID INT,
    ProductID INT,
    OrderDate DATE,
    Quantity INT,
    Revenue DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES dim_customer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES dim_product(ProductID)
);
