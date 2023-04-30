library(tidyverse)

# Get all csv files to be combined
files <- list.files(path = "./CourtCases/", pattern = "*.csv")

# Rename file path
files <- sapply(files, function(x) paste0("./CourtCases/", x))

# Bind all data
df <- lapply(files, read_csv) |>
  bind_rows()

# Write CSV
write.csv(df, file = "all_cases.csv", row.names = FALSE)
