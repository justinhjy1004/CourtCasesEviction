library(tidyverse)
library(knitr)
library(lubridate)

#======================================================
# Classification Distribution 
#======================================================
cases <- read_csv("../02_cleaning/clean_all_cases.csv")

classification <- as.data.frame(table(cases$CLASSIFICATION))

kable(classification, format = "latex")

#=========================================================
# Writ vs Judgement of Restitution
# Classification vs Judgement of Restitution
#=========================================================

cases |>
  mutate( 
    WRIT_ACC = ifelse((WRIT), "WRIT", "NO WRIT"),
    JUD = ifelse(RESTITUTION, "JUDGE", "NO JUDGE")
    ) -> cases
y <- prop.table(table(cases$WRIT_ACC, cases$JUD))
y

kable(y, format = "latex")

z <- prop.table(table(cases$CLASSIFICATION, cases$JUD), margin = 1)
kable(z, format = "latex")

#======================================================
# Continuation and Attorney
# Continuation and Length of Case
#======================================================

cases |>
  mutate(
    HAS_ATTORNEY = ifelse(is.na(DEFENDANT_ATTORNEY),
                          "No Attorney",
                          "Has Attorney"),
    IS_CONTINUED = ifelse(CONTINUED, "Continued", "Not Continued")
  ) -> cases

x <- prop.table(table(cases$IS_CONTINUED, cases$HAS_ATTORNEY))
kable(x, format = "latex")

attorney_and_continued <- x[1,1]
attorney_and_notcontinued <- x[2,1]
noattorney_and_continued <- x[1,2]
noattorney_and_notcontinued <- x[2,2]

p_continued_given_attorney <- attorney_and_continued/ (attorney_and_continued + attorney_and_notcontinued)
p_continued_given_noattorney <- noattorney_and_continued / (noattorney_and_continued + noattorney_and_notcontinued)


cases |>
  mutate(
    CLOSING_DATE = as.Date(CLOSING_DATE, format = "%m/%d/%Y"),
    FILING_DATE = as.Date(FILING_DATE, format = "%m/%d/%Y"),
    length_case = as.numeric(difftime(CLOSING_DATE, FILING_DATE, units="days"))) -> cases

reg1 <- lm(length_case ~ CONTINUED, cases)
summary(reg1)

library(stargazer)
stargazer(reg1)
#=======================================================
# Race Prediction
#=======================================================
race <- read_csv("../06_demographics/pred_race.csv")

kable(table(race$PRED_RACE_FIRST, race$PRED_RACE_LAST), format = "latex")

kable(table(race$PRED_GENDER), format="latex")

match <- read_csv("../04_geocoding/matches.csv")
nrow(match)

kable(prop.table(table(match$Exact)))

