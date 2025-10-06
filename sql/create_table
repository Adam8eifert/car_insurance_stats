-- Drop table if it already exists to ensure a clean start
DROP TABLE IF EXISTS public.car_insurance_claim;

-- Create the main table structure
CREATE TABLE public.car_insurance_claim (
    -- Primary key and categorical (text) data columns
    id BIGINT PRIMARY KEY,
    age VARCHAR(50) NULL,
    gender VARCHAR(50) NULL,
    race VARCHAR(50) NULL,
    driving_experience VARCHAR(50) NULL,
    education VARCHAR(50) NULL,
    income VARCHAR(50) NULL, 
    vehicle_year VARCHAR(50) NULL,
    vehicle_type VARCHAR(50) NULL,
    
    -- TEMPORARY FIX: Columns with dirty data (' ') are set to VARCHAR
    -- This allows the import to succeed without errors (Cannot convert ' ' to Double)
    credit_score VARCHAR(50) NULL, 
    annual_mileage VARCHAR(50) NULL,
    
    -- Numerical/Boolean (INTEGER) columns
    vehicle_ownership INTEGER NULL, 
    married INTEGER NULL,           
    children INTEGER NULL,          
    outcome INTEGER NULL,           
    postal_code INTEGER NULL,
    speeding_violations INTEGER NULL,
    duis INTEGER NULL,
    past_accidents INTEGER NULL
);