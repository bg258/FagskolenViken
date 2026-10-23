-- 1. INNER JOIN: Viser bare bestillinger som har en kunde tilknyttet dem. ---
SELECT
    b.bestilling_id,
    k.navn,
    k.by,
    b.dato,
    b.belop
FROM bestillinger AS b
INNER JOIN kunder AS k
    ON b.kunde_id = k.kunde_id
ORDER BY b.bestilling_id;

-- 2. LEFT JOIN: Viser alle kunder i tillegg til kunder uten bestillinger. ---
SELECT
    k.kunde_id,
    k.navn,
    COUNT(b.bestilling_id) AS antall_bestillinger,
    COALESCE(ROUND(SUM(b.belop), 2), 0) AS totalbelop
FROM kunder AS k
LEFT JOIN bestillinger AS b
    ON k.kunde_id = b.kunde_id
GROUP BY k.kunde_id, k.navn
ORDER BY k.kunde_id;
