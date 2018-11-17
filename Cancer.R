raw_breast_cancer <- read.csv(data_url)
raw_breast_cancer %>% head(3)
raw_breast_cancer <- read.csv(data_url, header = FALSE)
raw_breast_cancer %>% head(3)
names(raw_breast_cancer) <- names(BreastCancer)
raw_breast_cancer %>% head(3)
raw_breast_cancer <- read.csv(data_url, header = FALSE,
col.names = names(BreastCancer))
raw_breast_cancer %>% head(3)
map_class <- function(x) {
ifelse(x == 2, "bening",
ifelse(x == 4, "malignant",
NA))
}
mapped <- formatted_breast_cancer$Class %>% map_class
mapped %>% table
map_class <- function(x) {
ifelse(x == 2, "bening", "malignant")
}
mapped <- formatted_breast_cancer$Class %>% map_class
mapped %>% table
dict <- c("2" = "benign", "4" = "malignant")
map_class <- function(x) dict[as.character(x)]
mapped <- formatted_breast_cancer$Class %>% map_class
mapped %>% table
mapped %<>% unname
raw_breast_cancer$Class %>%
{ dict <- c("2" = "benign", "4" = "malignant")
dict[as.character(.)]
} %>%
unname %>%
factor(levels = c("benign", "malignant")) %>%
table
formatted_data <- BreastCancer %>%
  mutate(Cl.thickness.numeric =
           as.numeric(as.character(Cl.thickness)),
         Cell.size.numeric =
           as.numeric(as.character(Cell.size))) %>%
  mutate(IsMalignant = ifelse(Class == "benign", 0, 1))
fitted_model <- formatted_data %>%
  glm(IsMalignant ~ Cl.thickness.numeric + Cell.size.numeric, data = .)
predict(fitted_model, formatted_data, type = "response") %>% head
classify <- function(probability) ifelse(probability < 0.5, 0, 1)
classified_malignant <- classify(predict(fitted_model, formatted_data))
table(formatted_data$IsMalignant, classified_malignant)
table(formatted_data$IsMalignant, classified_malignant,
      dnn=c("Data", "Predictions"))
classify <- function(probability)
  ifelse(probability < 0.5, "benign", "malignant")
classified <- classify(predict(fitted_model, formatted_data))
table(formatted_data$Class, classified,
      dnn=c("Data", "Predictions"))
confusion_matrix <- table(formatted_data$Class, classified,dnn=c("Data", "Predictions"))
(accuracy <- sum(diag(confusion_matrix))/sum(confusion_matrix))
table(BreastCancer$Class)
tbl <- table(BreastCancer$Class)
tbl["benign"] / sum(tbl)
table(BreastCancer$Class, sample(BreastCancer$Class))
accuracy <- function(confusion_matrix)
 sum(diag(confusion_matrix))/sum(confusion_matrix)
replicate(8, accuracy(table(BreastCancer$Class,
 sample(BreastCancer$Class))))
(specificity <- confusion_matrix[1,1]/
 (confusion_matrix[1,1] + confusion_matrix[1,2]))
(sensitivity <- confusion_matrix[2,2]/
 (confusion_matrix[2,1] + confusion_matrix[2,2]))
specificity <- function(confusion_matrix)
 confusion_matrix[1,1]/(confusion_matrix[1,1]+confusion_matrix[1,2])
sensitivity <- function(confusion_matrix)
 confusion_matrix[2,2]/(confusion_matrix[2,1]+confusion_matrix[2,2])
prediction_summary <- function(confusion_matrix)
 c("accuracy" = accuracy(confusion_matrix),
 "specificity" = specificity(confusion_matrix),
 "sensitivity" = sensitivity(confusion_matrix))
random_prediction_summary <- function()
 prediction_summary(table(BreastCancer$Class,
 sample(BreastCancer$Class)))
replicate(3, random_prediction_summary())
confusion_matrix[2,1] / sum(confusion_matrix[,1])
confusion_matrix[1,1] / sum(confusion_matrix[,1])
confusion_matrix[2,2] / sum(confusion_matrix[,2])
confusion_matrix[1,2] / sum(confusion_matrix[,2])
