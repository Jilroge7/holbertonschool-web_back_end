-- imported table dump, use to rank country origin
-- of bands, ordered by the number of fans.
SELECT origin AS origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;