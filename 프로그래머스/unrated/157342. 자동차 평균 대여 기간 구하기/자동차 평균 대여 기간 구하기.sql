SELECT CAR_ID, START_DATE, END_DATE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATEDIFF(END_DATE, START_DATE) >= 7