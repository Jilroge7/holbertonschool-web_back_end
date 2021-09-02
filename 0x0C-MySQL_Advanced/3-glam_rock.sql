-- lists all bands with glam rock as main style,
-- ranked by their longevity
SELECT band_name AS band_name, ifnull(split, 2020)-formed AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;