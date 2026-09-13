-- Synthetic legacy checkpoint. Adapt table names only after documenting the mapping.
CREATE TABLE legacy_products (sku text PRIMARY KEY, name text NOT NULL, price numeric(12,2));
INSERT INTO legacy_products VALUES ('LEG-1', 'Legacy Keyboard', 19.99), ('LEG-2', 'Legacy Mouse', 9.50);
