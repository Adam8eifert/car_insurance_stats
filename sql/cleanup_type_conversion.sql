-- CLEANUP AND TYPE CONVERSION

-- 1. Replace the incorrect single space (' ') and empty string ('') with NULL (missing value)

-- CREDIT_SCORE cleanup:
UPDATE public.car_insurance_claim
SET credit_score = NULL
WHERE credit_score = ' ' OR credit_score = ''; 

-- ANNUAL_MILEAGE cleanup:
UPDATE public.car_insurance_claim
SET annual_mileage = NULL
WHERE annual_mileage = ' ' OR annual_mileage = ''; 

-- 2. Convert the data types back to their correct numerical types

-- CREDIT_SCORE: Convert from VARCHAR to FLOAT 
-- The ::FLOAT cast is safe now because all non-numeric values (' ' and '') are NULL
ALTER TABLE public.car_insurance_claim
ALTER COLUMN credit_score TYPE FLOAT USING credit_score::FLOAT;

-- ANNUAL_MILEAGE: Convert from VARCHAR -> FLOAT -> INTEGER (This handles "12000.0" and is now safe from empty strings)
ALTER TABLE public.car_insurance_claim
ALTER COLUMN annual_mileage TYPE INTEGER USING annual_mileage::FLOAT::INTEGER;

-- Final check
SELECT COUNT(*) AS total_rows, 
       COUNT(credit_score) AS non_null_credit_score 
FROM public.car_insurance_claim;