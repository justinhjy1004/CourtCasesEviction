library(tidyverse)

df <- read_csv("UpdatedCourtCases.csv")

x <- grepl("Real", df$CLASSIFICATION, ignore.case=T)
sum(x)

evict <- df[x,]

evict$state <- substr(evict$CASE_ID, 4,5)
evict$year <- substr(evict$CASE_ID, 7, 8)
evict$id <- substr(evict$CASE_ID, 10, 100)

df$state <- substr(df$CASE_ID, 4,5)
df$year <- substr(df$CASE_ID, 7, 8)
df$id <- substr(df$CASE_ID, 10, 100)

df |>
  group_by(year, state) |>
  summarize(
    count = n(),
    max = max(as.numeric(id)),
    resti = sum(RESTITUTION, na.rm = T)
  )

df$year <- as.numeric(df$year)
df |>
  ungroup() |>
  group_by(year, CLASSIFICATION) |>
  summarize(
    count = n()
  ) -> class

colnames(class) <- c("YEAR", "CLASSIFICATION", 'COUNT')
write.csv(class, )