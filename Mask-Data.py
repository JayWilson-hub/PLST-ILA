import os
import numpy as np
from osgeo import gdal, gdalconst


remote_sensing_folder = r" "
mask_image_path = r" "
output_folder = r" "
nodata_value = -9999

os.makedirs(output_folder, exist_ok=True)


mask_ds = gdal.Open(mask_image_path, gdalconst.GA_ReadOnly)
mask_array = mask_ds.ReadAsArray()
mask_rows, mask_cols = mask_array.shape
mask_gt = mask_ds.GetGeoTransform()
mask_proj = mask_ds.GetProjection()


for filename in os.listdir(remote_sensing_folder):
    if filename.lower().endswith(".tif"):
        file_path = os.path.join(remote_sensing_folder, filename)
        print(f"Processing：{file_path}")


        remote_sensing_ds = gdal.Open(file_path, gdalconst.GA_ReadOnly)
        remote_sensing_array = remote_sensing_ds.ReadAsArray()


        masked_array = np.where(mask_array == 1, remote_sensing_array, nodata_value)


        output_path = os.path.join(output_folder, filename)
        driver = gdal.GetDriverByName('GTiff')
        out_ds = driver.Create(
            output_path,
            mask_cols,
            mask_rows,
            1,
            gdalconst.GDT_Float32
        )
        out_ds.SetGeoTransform(mask_gt)
        out_ds.SetProjection(mask_proj)

        out_band = out_ds.GetRasterBand(1)
        out_band.WriteArray(masked_array)
        out_band.SetNoDataValue(nodata_value)


        out_band = None
        out_ds = None
        remote_sensing_ds = None

        print(f"Saving：{output_path}")

mask_ds = None
