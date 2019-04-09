library(dplyr)
library(ggplot2)
library(grid)
library(gridExtra)
library(jsonlite)

# Changing JSON to CSV (in case of later analysis)
jsonData <- fromJSON("../input/university-statistics/schoolInfo.json")
jsonData <- as.data.frame(do.call(cbind, jsonData))

write.csv(x = jsonData, file = "schoolInfo.csv")