library(tidyverse)
library(predictrace)

df <- read_csv("clean_all_cases.csv")

#=============================================================
# Split names based on First and Last
# Predict Gender and Race from Name
#=============================================================
df <- df |>
  select(CASE_ID, DEFENDANT) |>
  extract(
    DEFENDANT, c("D_FIRST", "D_LAST"), "([^ ]+) (.*)"
    ) |>
  mutate(
    PRED_RACE_FIRST = predict_race(D_FIRST, surname = FALSE, probability = FALSE)[[3]],
    PRED_RACE_LAST = predict_race(D_LAST, surname = TRUE, probability = FALSE)[[3]],
    PRED_GENDER = predict_gender(D_FIRST, probability = FALSE)[[3]]
  )

write.csv(df, file = "pred_race.csv", row.names = FALSE)
