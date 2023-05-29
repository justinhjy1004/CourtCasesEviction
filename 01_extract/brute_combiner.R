library(tidyverse)

args <- commandArgs(trailingOnly=TRUE)

dir_path <- paste0("./", args[1], "/")

# Get all csv files to be combined
files <- list.files(path = dir_path, pattern = "*.csv")

# Rename file path
files <- sapply(files, function(x) paste0(dir_path, x))

# Bind all data
df <- lapply(files, read_csv) |>
  bind_rows()

# Write CSV
write.csv(df, file = paste0(args[1], ".csv"), row.names = FALSE)
