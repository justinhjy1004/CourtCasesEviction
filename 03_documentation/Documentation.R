library(tidyverse)
library(knitr)

#======================================================
# Classification Distribution 
#======================================================
cases <- read_csv("../02_cleaning/clean_all_cases.csv")

classification <- as.data.frame(table(cases$CLASSIFICATION))

kable(x, format = "latex")

#=========================================================
# Writ vs Judgement of Restitution
#=========================================================

cases |>
  mutate( 
    WRIT_ACC = ifelse(is.na(WRIT), "NO WRIT", "WRIT"),
    JUD = ifelse(RESTITUTION, "JUDGE", "NO JUDGE")
    ) -> cases
y <- prop.table(table(cases$WRIT_ACC, cases$JUD))
y

kable(y, format = "latex")

#======================================================
# Continuation and Attorney
#======================================================

cases |>
  mutate(
    HAS_ATTORNEY = ifelse(is.na(DEFENDANT_ATTORNEY),
                          "No Attorney",
                          "Has Attorney"),
    IS_CONTINUED = ifelse(CONTINUED, "Continued", "Not Continued")
  ) -> cases

x <- prop.table(table(cases$IS_CONTINUED, cases$HAS_ATTORNEY))

attorney_and_continued <- x[1,1]
attorney_and_notcontinued <- x[2,1]
noattorney_and_continued <- x[1,2]
noattorney_and_notcontinued <- x[2,2]

p_continued_given_attorney <- attorney_and_continued/ (attorney_and_continued + attorney_and_notcontinued)
p_continued_given_noattorney <- noattorney_and_continued / (noattorney_and_continued + noattorney_and_notcontinued)

#=======================================================
# Race Prediction
#=======================================================
race <- read_csv("../06_demographics/pred_race.csv")

kable(table(race$PRED_RACE_FIRST, race$PRED_RACE_LAST), format = "latex")

kable(table(race$PRED_GENDER), format="latex")

match <- read_csv("../04_geocoding/matches.csv")
nrow(match)

kable(prop.table(table(match$Exact)))

