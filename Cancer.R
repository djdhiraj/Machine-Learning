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
